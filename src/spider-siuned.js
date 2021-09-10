let username = document.getElementById('_OPERCOD');
let password = document.getElementById('_OPERPASS');
let button = document.getElementsByName('BUTTON1')[0];
username.value = '';
password.value = '';
button.submit();

let xpath;
let result;
xpath = '//span[contains(@id, "span__ESCUELACUE_")]'
result = XPathResult.UNORDERED_NODE_ITERATOR_TYPE
let a = document.evaluate(xpath, document, null, result, null);
let span = a.iterateNext();
link = span.getElementByTagName('a')[0];
link.click();

xpath = '//a[contains(text(), "Alumnos")]';
let iterator = document.evaluate(xpath, document, null, result, null);
let link = iterator.iterateNext();
link.click();

xpath = '//a[contains(text(), "Cursos")]';
let iterator = document.evaluate(xpath, document, null, result, null);
let link = iterator.iterateNext();
link.click();


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
formdata = {
    '_EventName': 'EENTER.',
    '_EventGridId': '',
    '_EventRowId': '',
    '_OPERCOD': env('USERNAME'),
    '_OPERPASS': env('PASSWORD'),
    'BUTTON1': '',
    'W0020_CONTENTNAME': '',
    'sCallerURL': '{self.main_url}/siuned/servlet/hwwescuelausuario',
}
