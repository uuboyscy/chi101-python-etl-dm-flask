import requests

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
first_page_url = "https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html"
over_18_url = "https://www.ptt.cc/ask/over18"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

ss = requests.session()
print(ss.cookies)

ss.get(first_page_url, headers=headers)
print(ss.cookies)

data = {
    "from": "/bbs/Gossiping/index.html",
    "yes": "yes",
}

ss.post(over_18_url, headers=headers, data=data)
print(ss.cookies)

res = ss.get(url, headers=headers)
print(res.text)


