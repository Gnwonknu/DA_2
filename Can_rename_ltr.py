import requests

url = 'http://54.169.8.122/Python/172.18.58.238/varsity/index.html'
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
    start_urls = ["http://54.169.8.122/Python/172.18.58.238/varsity/index.html"]
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
