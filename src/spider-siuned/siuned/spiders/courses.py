import scrapy
from os import getenv as env

def authentication_failed(response):
    title = response.css('title::text').get()
    return title == 'Login'

class CoursesSpider(scrapy.Spider):
    name = 'courses'
    main_domain = 'w3.neuquen.gov.ar'
    main_url = f'http://{main_domain}'
    allowed_domains = [main_domain]
    start_urls = [f'{main_url}/siuned/servlet/hlogin']

    def parse(self, response):
        formdata = self.make_formdata_login()
        return scrapy.FormRequest.from_response(
            response,
            formdata=formdata,
            callback=self.after_login,
        )

    def after_login(self, response):
        msg = 'Login failed'
        if authentication_failed(response):
            self.logger.error(msg)
            return
        return self.parse_school(response)

    def parse_school(self, response):
        query = '//tr[@class]'
        name = 'ESCUELACUE'
        cb_kwargs = {}
        for selector in response.xpath(query):
            formdata = self.make_formdata_event(selector, name)
            item_school = self.make_item_school(selector)
            cb_kwargs['item_school'] = item_school
            yield scrapy.FormRequest.from_response(
                response,
                formdata=formdata,
                callback=self.follow_school,
                cb_kwargs=cb_kwargs,
            )

    def follow_school(self, response, item_school):
        name = 'Cursos'
        url = self.make_url_tab(response, name)
        cb_kwargs = {}
        cb_kwargs['item_school'] = item_school
        yield scrapy.Request(
            url,
            callback=self.parse_course,
            cb_kwargs=cb_kwargs,
        )

    def parse_course(self, response, item_school):
        query = '//tr[@class]'
        name = 'CURSOCOD'
        cb_kwargs = {}
        cb_kwargs['item_school'] = item_school
        for selector in response.xpath(query):
            url = self.make_url_row(response, name)
            item_course = self.make_item_course(selector)
            cb_kwargs['item_course'] = item_course
            yield scrapy.Request(
                url,
                callback=self.follow_course,
                cb_kwargs=cb_kwargs,
            )
        yield self.follow_course_next(response, item_school)

    def follow_course_next(self, response, item_school):
        query = './/a[contains(@onclick, "NEXT")]/@onclick'
        name = 'NEXT'
        formdata = self.make_formdata_event(response, name, query)
        cb_kwargs = {}
        cb_kwargs['item_school'] = item_school
        if formdata:
            yield scrapy.FormRequest.from_response(
                response,
                formdata=formdata,
                callback=self.parse_course,
                cb_kwargs=cb_kwargs
            )

    def follow_course(self, response, item_school, item_course):
        name = 'Alumnos'
        url = self.make_url_tab(response, name)
        cb_kwargs = {}
        cb_kwargs['item_school'] = item_school
        cb_kwargs['item_course'] = item_course
        yield scrapy.Request(
            url,
            callback=self.parse_student,
            cb_kwargs=cb_kwargs,
        )

    def parse_student(self, response, item_school, item_course):
        query = '//tr[@class]'
        name = 'ALUAPENOM'
        cb_kwargs = {}
        cb_kwargs['item_school'] = item_school
        cb_kwargs['item_course'] = item_course
        for selector in response.xpath(query):
            url = self.make_url_row(selector)
            yield scrapy.Request(
                url,
                callback=self.parse_student,
                cb_kwargs=cb_kwargs,
            )

    def parse_student(self, response, item_school, item_course):
        query = '//table[@id="TABLEWC"]'
        selector = response.xpath(query)
        item_student = self.make_item_student(selector)
        query = '//table[contains(@id, $name)]//img/@src'
        name = 'TABLEFOTO'
        item_student['student_img'] = response.xpath(query, name=name).get()
        item_student.update(item_school)
        item_student.update(item_course)
        return item_student

    def make_formdata_login(self):
        formdata = {
            '_EventName': 'EENTER.',
            '_EventGridId': '',
            '_EventRowId': '',
            '_OPERCOD': env('USERNAME'),
            '_OPERPASS': env('PASSWORD'),
            'BUTTON1': '',
            'W0020_CONTENTNAME': '',
            'sCallerURL': f'{self.main_url}/siuned/servlet/hwwescuelausuario',
        }
        return formdata

    def make_url(self, response, query, name):
        url = response.xpath(query, name=name).get()
        url = response.urljoin(url)
        return url

    def make_url_tab(self, response, name):
        query = './/span[contains(@id, "TAB")]/a[text()=$name]/@href'
        url = self.make_url(response, query, name)
        return url

    def make_url_row(self, response, name):
        query = './/span[contains(@id, $name)]/a/@href'
        url = self.make_url(response, query, name)
        return url

    def make_formdata_event(self, selector, name, query=None):
        if not query:
            query = './/span[contains(@id, $name)]/a/@href'
        regex = r"'(.+)'"
        selector = selector.xpath(query, name=name)
        event = selector.re_first(regex)
        event = event.replace('\\', '')
        formdata = {'_EventName': event} if event else {}
        return formdata

    # def make_formdata_event(self, selector, name):
    #     if name == 'NEXT':
    #         query = '//input[contains(@onclick, $name)]/@onclick'
    #     else:
    #         query = './/span[contains(@id, $name)]/a/@href'
    #     regex = r"'(.+)'"
    #     key = '_EventName'
    #     formdata = {}
    #     selector = selector.xpath(query, name=name)
    #     event = selector.re_first(regex)
    #     event = event.replace('\\', '')
    #     formdata[key] = event
    #     return formdata

    def make_item(self, selector, attrs):
        query = './/input[contains(@name, $name)]/@value'
        item = {}
        for key, value in attrs.items():
            value = selector.xpath(query, name=value).get()
            # item[key] = value.strip()
            item[key] = value
        return item

    def make_item_school(self, selector):
        attrs = {
            'school_cue': 'ESCUELACUE',
            'school_anexo': 'ESCUELAANEXOREAL',
            'school_educacion': 'EDUCACIONDSC',
            'school_escuela': 'ESCUELANOMBRECORTO',
            'school_distrito': 'ESCUELADISTRITONRO',
            'school_nivel': 'ESCUELANIVEL',
            'school_localidad': 'LOCALIDADDSC',
            'school_matricula': 'MTRALU',
            'school_recursantes': 'ESCUELAANEXOREAL',
            'school_fecha': 'ESCUELAANEXOREAL',
            'school_id': 'ESCUELAANEXOREAL',
        }
        item = self.make_item(selector, attrs)
        return item

    def make_item_course(self, selector):
        attrs = {
            'course_curso': 'CURSOCOD',
            'course_tipo': 'TIPOCURSODSC',
            'course_multiple': 'CURSOMULTIPLE',
            'course_turno': 'TURNODSC',
            'course_seccion': 'CURSOSECCION',
            'course_matricula': 'MTRALU',
            'course_recursantes': 'MTRREC',
            'course_fecha': 'MTRFCH',
            'course_planes': 'CURSOPLANES',
            'course_preceptor': 'CURSOPRECEPTOR',
            'course_asistencia': 'CURSOASISTENCIA',
        }
        item = self.make_item(selector, attrs)
        return item

    def make_item_student(self, selector):
        attrs = {
            'student_codigo': 'PERID',
            'student_apellido': 'PERAPELLIDO',
            'student_nombre': 'PERNOMBRES',
            'student_dni': 'PERDOCUMENTO',
            'student_estado_civil': 'ESTADOCIVILDSC',
            'student_sexo': 'PERSEXO',
            'student_fecha_nacimiento': 'PERFECHANAC',
            'student_pais': 'PERPAISNACIMIENTODSC',
            'student_provincia': 'PERPROVNACIMIENTODSC',
            'student_localidad': 'PERLOCALIDADNAC',
            'student_nacionalidad': 'PERPAISNACIONALIDADDSC',
        }
        item = self.make_item(selector, attrs)
        return item

