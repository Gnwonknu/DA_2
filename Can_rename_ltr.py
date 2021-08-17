import requests

url = 'http://www.ite.edu.sg'
r = requests.get(url)
print(r.text)

print("Status code:") #get status code
print("/t*", r.status_code)

h = requests.head(url)
print("Header:")

for x in h.headers:
    print("/t", x, ":", h.headers[x])

headers = {
    'User-Agent': 'Mobile'
}

rh = requests.get(url, headers=headers)
print(rh.request.headers)

import scrapy

class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ["https://www.ite.edu.sg"]
    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield{
                'image LInk': x.xpath(newsel).extract_first()
            }
        Page_selector = '.next a::attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )


import unittest







class Can_rename_ltr(unittest.TestCase):







    def test_EngineType(selfself):

        print("Testing")

        if __name__=='__main__':

            unittest.main()