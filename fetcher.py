import requests
import json
import os

review_API_url = "https://amazon23.p.rapidapi.com/reviews"

headers = {
    # API KEY
}

def build_json_path(asin, page):
    return f'./api_data/{asin}_p{page}.json'


def query(asin, page=1):
    querystring = {"asin": asin,"sort_by":"helpful","country":"US"}
    response = requests.request(
        "GET", 
        review_API_url, 
        headers=headers, 
        params=querystring
    )

    with open(build_json_path(asin,page), "w",encoding="utf8", errors='ignore') as f:
        f.write(response.text)

    return response.text

def get_reviews(asin, page=1):
    data = None
    json_file = build_json_path(asin, page)
    already_downloaded = os.path.exists(json_file)
    if already_downloaded:
        print("== Cache hit for asin ", asin)
        with open(json_file, 'r', encoding="utf8", errors='ignore') as f:
            data = f.read()
    else:
        print("== Fetching API for asin ", asin)
        data = query(asin)
    
    res_obj = json.loads(data)
    reviews = []
    for obj in res_obj['result']:
        reviews.append(obj['review'].replace("\"", ""))
    
    return reviews
