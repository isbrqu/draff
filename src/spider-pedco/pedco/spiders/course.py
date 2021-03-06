from datetime import datetime
from pprint import pprint
from scrapy import Spider
from urllib.parse import parse_qs
import urllib.parse as urlparse
from scrapy.linkextractors import LinkExtractor

now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

def _param(url, param):
    parsed = urlparse.urlparse(url)
    value = parse_qs(parsed.query).get(param)
    return value[0] if value else None

class Course(Spider):
    name = 'course'
    start_urls = ['https://pedco.uncoma.edu.ar/course/index.php']
    allowed_domains = ['pedco.uncoma.edu.ar']
    custom_settings = {
        'FEEDS': {
            f'csv/x{name}-{now}.csv': {
                'format': 'csv',
                'encoding': 'utf8',
                'store_empty': False,
                'fields': ['id', 'name', 'category_id'],
            }
        },
        'LOG_FILE': f'log/{name}.log',
        # 'CLOSESPIDER_PAGECOUNT': 10,
    }
    link_extractor_course = LinkExtractor(
        restrict_css='.coursename'
    )
    link_extractor_category = LinkExtractor(
        restrict_css='h3.categoryname',
        process_value=lambda url: f'{url}&perpage=200'
    )

    def parse(self, response):
        courses = self.link_extractor_course.extract_links(response)
        category_id = _param(response.url, 'categoryid') or 0
        for course in courses:
            yield {
                'id': _param(course.url, 'id'),
                'name': course.text.strip(),
                'category_id': category_id,
            } 
        categories = self.link_extractor_category.extract_links(response)
        yield from response.follow_all(urls=categories, callback=self.parse)

