import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/movie/index.html"
# url = "https://www.ptt.cc/bbs/movie/index%s.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, "html.parser")

print(soup.select('a[class="btn wide"]'))
print(
    "https://www.ptt.cc" + soup.select('a[class="btn wide"]')[1]["href"]
)



a = []
a.sort()