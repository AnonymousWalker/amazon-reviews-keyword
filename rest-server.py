from flask import Flask
from flask_cors import CORS
import evaluator
import fetcher
import json

app = Flask(__name__)
CORS(app)

def filter_result(item: tuple, max_score: float):
    return item['score'] > max_score - 1 and (item['sentiment'] > 0.2 or item['sentiment'] < -0.2)

def filter_result_extend(item):
    return item['sentiment'] > 0.3 or item['sentiment'] < -0.3

@app.route('/reviews/<asin>', methods=['GET'])
def get_review_keywords_by_asin(asin):
    reviews = fetcher.get_reviews(asin)
    keyword_scores = evaluator.evaluate_reviews(reviews)
    max_score = max(keyword_scores, key = lambda i: i['score'])['score']
    
    results = list(filter(lambda i: filter_result(i, max_score), keyword_scores))
    if len(results) <= 4:
        results = list(filter(filter_result_extend, keyword_scores))
    
    return json.dumps(results)

if __name__ == '__main__':
    app.run(debug=True)