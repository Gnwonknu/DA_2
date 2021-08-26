import requests
import scrapy
import unittest

url = 'https://brickset.com/sets/year-1999'
r = requests.get(url)
print(r.text)

print("Status code:") #get status code
print(r.status_code)

h = requests.head(url)
print("Header:")

for x in h.headers:
    print(x, ":", h.headers[x])

headers = {
    'User-Agent': 'Mobile'
}

rh = requests.get(url, headers=headers)
print(rh.request.headers)


class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ["https://brickset.com/sets/year-1999"]
    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield{
                'image Link': x.xpath(newsel).extract_first()
            }
        Page_selector = '.next a::attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
            
import Can_rename_ltr as prog

url = 'https://brickset.com/sets/year-1999'
r = requests.get(url)

class Hello(unittest.TestCase):

    def test_login_requests(self):
        self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()
