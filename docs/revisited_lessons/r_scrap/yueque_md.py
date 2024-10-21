import json
import re
import urllib

import requests

BASE_URL="https://www.yuque.com/"
ERUPT_URL="https://www.yuque.com/erupts/erupt"

def get_book(book_path:str):
    req_url = f'{BASE_URL}book/{book_path}'
    raw_docs_data = requests.get(req_url)
    print(raw_docs_data.content.decode('utf-8'))
    data = re.findall(r"decodeURIComponent\(\"(.+)\"\)\);", raw_docs_data.content.decode('utf-8'))
    docs_json = json.loads(urllib.parse.unquote(data[0]))
    return docs_json

if __name__ == '__main__':
    result = get_book("erupts/erupt")
