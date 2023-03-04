import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

def load_article(article_url: str):
    res = requests.get(article_url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    article_tag = soup.select_one('div[id="main-content"]')
    for tag in article_tag.select('div'):
        tag.extract()
    print(article_tag)
    # print("==============")
    # print(article_tag.select_one('div[class="article-metaline"]').extract())
    # print("========")
    # print(article_tag)
    pass


if __name__ == "__main__":
    article_url = "https://www.ptt.cc/bbs/movie/M.1677862363.A.7AE.html"
    load_article(article_url)