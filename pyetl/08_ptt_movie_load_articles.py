import os

import requests
from bs4 import BeautifulSoup

from load_article_tool import load_article


load_folder = "articles"
if not os.path.exists(f"./{load_folder}"):
    os.mkdir(f"./{load_folder}")

url = "https://www.ptt.cc/bbs/movie/index.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}


for i in range(0, 5):
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, "html.parser")

    # Get all title tags
    title_tag_list = soup.select('div.title')

    for title_tag in title_tag_list:
        if title_tag.select_one('a'):
            title_name = title_tag.select_one('a').text
            article_url = "https://www.ptt.cc" + title_tag.select_one('a')["href"]
            try:
                load_article(
                    article_url=article_url,
                    load_path=f"./{load_folder}/{title_name}.txt",
                )
            except FileNotFoundError:
                load_article(
                    article_url=article_url,
                    load_path=f"./{load_folder}/{title_name.replace('/', '-')}.txt",
                )
            except OSError:
                pass
            print(title_name)
            print(article_url)
        else:
            print("Title is empty.")

        print("========")

    url = "https://www.ptt.cc" + soup.select('a[class="btn wide"]')[1]["href"]

