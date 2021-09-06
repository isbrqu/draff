import scrapy
from os import getenv as env
from bs4 import BeautifulSoup
import requests

def authentication_failed(response):
    title = response.css('title::text').get()
    return title == 'Login'

class SchoolsSpider(scrapy.Spider):
    name = 'schools'
    main_domain = 'w3.neuquen.gov.ar'
    main_url = f'http://{main_domain}'
    allowed_domains = [main_domain]
    start_urls = [f'{main_url}/siuned/servlet/hlogin']

    def parse(self, response):
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
        return scrapy.FormRequest.from_response(
            response,
            formdata=formdata,
            callback=self.after_login,
        )

    def after_login(self, response):
        formdata = {
            '_EventName': 'EENTER.',
            '_EventGridId': '',
            '_EventRowId': '',
            '_OPERCOD': env('USERNAME'),
            '_OPERPASS': env('PASSWORD'),
            'BUTTON1': '',
        }
        if authentication_failed(response):
            self.logger.error('Login failed')
            return
        # return self.parse_schools(response)
        return self.parse_students(response)

    # def parse_students(self, response):

    def parse_courses(self, response):
        for school in self.parse_schools(response):
            formdata = {
                '_EventName': school['event']
            }
            yield scrapy.FormRequest.from_response(
                response,
                formdata=formdata,
                callback=self.__follow_course_tab,
            )

    def __follow_course_tab(self, response):
        selector = ".//span[contains(@id, 'TAB')]/a[text()=$tab]/@href"
        href = response.xpath(selector, tab='Cursos').get()
        url = response.urljoin(href)
        yield scrapy.Request(
            url,
            callback=self.__parse_courses,
        )

    def __parse_courses(self, response):
        names = {
            'name': 'CURSOCOD',
            'type': 'TIPOCURSODSC',
            'turn': 'TURNODSC',
            'section': 'CURSOSECCION',
            'enrollment': 'MTRALU',
            'recurring': 'MTRREC',
            'date': 'MTRFCH',
            'plan': 'CURSOPLANES',
            'preceptor': 'CURSOPRECEPTOR',
        }
        selector_url = './/span[contains(@id, $name)]/a/@href'
        name = 'CURSOCOD'
        for row, item in self.table_row(response, names):
            url = row.xpath(selector_url, name=name).get()
            item['url'] = response.urljoin(url)
            yield item
        selector_event = '//input[contains(@onclick, "NEXT")]/@onclick'
        regex = r"'(.+)'"
        event = response.xpath(selector_event).re_first(regex)
        if event:
            formdata = {
                '_EventName': event
            }
            yield scrapy.FormRequest.from_response(
                response,
                formdata=formdata,
                callback=self.__parse_courses
            )

    def parse_schools(self, response):
        names = {
            'annexed': 'ESCUELAANEXOREAL',
            'education': 'EDUCACIONDSC',
            'school': 'ESCUELANOMBRECORTO',
            'district': 'ESCUELADISTRITONRO',
            'level': 'ESCUELANIVEL',
            'location': 'LOCALIDADDSC',
            'enrollment': 'MTRALU',
            'recurring': 'MTRREC',
            'date': 'MTRFCH',
            'identifier': 'ESCUELAANEXO',
        }
        selector_url = './/span[contains(@id, $name)]/a/@href'
        name = 'ESCUELACUE'
        regex = r"'(.+)'"
        for row, item in self.table_row(response, names):
            item['event'] = row\
                .xpath(selector_url, name=name)\
                .re_first(regex)\
                .replace('\\', '')
            yield item

    def table_row(self, response, names):
        selector_row = '//tr[@class]'
        selector_value = './/input[contains(@name, $name)]/@value'
        for row in response.xpath(selector_row):
            item = {}
            for key, value in names.items():
                item[key] = row.xpath(selector_value, name=value).get()
            yield (row, item)

