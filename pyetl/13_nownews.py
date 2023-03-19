import json
import pprint

import requests


url = "https://www.nownews.com/nn-client/api/v1/cat/column/?pid=6085672"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

res = requests.get(url, headers=headers)

# json_data = json.loads(res.text)
# pprint.pprint(json_data)

# pprint.pprint(res.json())

for article_obj in res.json()["data"]["newsList"]:
    post_title = article_obj["postTitle"]
    post_url = "https://www.nownews.com" + article_obj["postUrl"]
    image_url = article_obj["imageUrl"]
    print(post_title)
    print(post_url)
    print(image_url)
    print("=======")