import requests

headers ={'User-Agent':'Mobile'}

url = 'https://www.httpbin.org/headers'

r = requests.get(url)

rh = requests.get(url, headers=headers)


print(rh.text)

print("Status code:")
print("\t *", r.status_code)

h = requests.head(url)
print("Header:")
print("******")
for x in h.headers:
    print("\t", x, ":", h.headers[x])
print("*******************************")

hello world
