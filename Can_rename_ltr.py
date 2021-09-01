import requests
import scrapy
import unittest

# Selects url
url = 'https://brickset.com/sets/year-1999'
# Perform "get" request
r = requests.get(url)
print(r.text)
# Display an "OK/200" status
print("Status code:") #get status code
print(r.status_code)
# Display the website header
h = requests.head(url)
print("Header:")

for x in h.headers:
    print(x, ":", h.headers[x])
# Modify user-agent to "Mobile"
headers = {
    'User-Agent': 'Mobile'
}
# Display modified user-agent
rh = requests.get(url, headers=headers)
print(rh.request.headers)
# Creates a spider
class NewSpider(scrapy.Spider):
    name = "new_spider"
    # Selects url
    start_urls = ["https://brickset.com/sets/year-1999"]
    def parse(self, response):
        # Selects "img"
        css_selector = 'img'
        # Display all Image Link found
        for x in response.css(css_selector):
            newsel = '@src'
            yield{
                'image Link': x.xpath(newsel).extract_first()
            }
        # To recurse next page    
        Page_selector = '.next a::attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
            
import Can_rename_ltr as prog
# Selects url
url = 'https://brickset.com/sets/year-1999'
# Perform "get" request
r = requests.get(url)
# Create a unit test
class Hello(unittest.TestCase):
    # Test if the status code returns "OK/200"
    def test_login_requests(self):
        self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()
