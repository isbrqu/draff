from bs4 import BeautifulSoup
from glob import iglob
from pandas import DataFrame
from ppath import PPath

def extract(filename, main_tag, item_tag, func):
    with open(filename) as xml:
        soup = BeautifulSoup(xml, 'xml')
        for item in soup.select_one(main_tag).find_all(item_tag, recursive=False):
            yield from func(item)

def xmltocsv(filename, main_tag, item_tag, func):
    dataframe = DataFrame(extract(filename, main_tag, item_tag, func))
    dataframe.to_csv(gpath.file_output)

path = 'mbz/students/*'
gpath = PPath(
    root='csv',
    ext_input='xml',
    ext_output='csv',
    exist_ok=True,
    delete=['mbz', 'course']
)

for folder in iglob(path):

    print(f'process: {folder}')

    gpath.folder_input = folder
    gpath.mkdir_folder_output()

    gpath.filename = 'users'
    main_tag = 'users'
    item_tag = 'user'
    xmltocsv(gpath.file_input, main_tag, item_tag, lambda item: [{
        'id': item['id'],
        'contextid': item['contextid'],
        'username': item.username.text,
        'username': item.idnumber.text,
        'email': item.email.text,
        'city': item.city.text,
        'country': item.country.text,
        'firstname': item.firstname.text,
        'lastname': item.lastname.text,
    }])

    # gpath.filename = 'moodle_backup'
    # main_tag = 'moodle_backup'
    # item_tag = 'information'
    # xmltocsv(gpath.file_input, main_tag, item_tag, lambda item: [{
    #     'name': item.select_one('name').text,
    #     'hash': item.original_site_identifier_hash.text,
    #     'course_id': item.original_course_id.text,
    #     'fullname': item.original_course_fullname.text.strip(),
    #     'shortname': item.original_course_shortname.text.strip(),
    #     'backup_id': item.details.detail['backup_id'],
    #     'contents': item.course.courseid.text,
    # }])

    # gpath.folder_input += 'course'
    # gpath.mkdir_folder_output()

    # gpath.filename = 'roles'
    # main_tag = 'roles role_assignments'
    # item_tag = 'assignment'
    # xmltocsv(gpath.file_input, main_tag, item_tag, lambda item: [{
    #     'id': item['id'],
    #     'roleid': item.roleid.text,
    #     'userid': item.userid.text,
    # }])

    # gpath.filename = 'enrolments'
    # main_tag = 'enrolments enrols'
    # item_tag = 'enrol'
    # xmltocsv(gpath.file_input, main_tag, item_tag, lambda item: [{
    #     'id': item['id'],
    #     'roleid': item.roleid.text,
    #     'userid': item.userid.text,
    #     'enrolementid': subitem['id'],
    #     'userid': subitem.userid.text,
    # } for subitem in item.user_enrolments.find_all('enrolment')])

    # gpath.filename = 'inforef'
    # main_tag = 'inforef userref'
    # item_tag = 'user'
    # xmltocsv(gpath.file_input, main_tag, item_tag, lambda item: [{
    #     'userid': item.id.text,
    # }])
