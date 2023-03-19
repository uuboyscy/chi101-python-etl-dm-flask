from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.ptt.cc/bbs/joke/index.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

req = request.Request(url=url)
print(123)
# res = request.urlopen(url=url)
res = request.urlopen(req)

html = res.read().decode("utf-8")

print(html)
