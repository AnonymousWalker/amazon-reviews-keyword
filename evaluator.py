import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from rake_nltk import Rake
from rake_nltk import Metric
import json
import re

# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('vader_lexicon')

# Sample product review
# review = "This product is amazing! It's very easy to use and has all the features I need. I especially love the design and the quality of the materials used. The only downside is that it's a bit expensive."

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Initialize RAKE
rake = Rake(
    min_length=2,
    max_length=4
)

def evaluate(review: str):
    # Extract keywords with sentiment
    sentiment_keywords = []
    review = review.replace('\'', "")
    review = review.replace('\"', "")
    review = re.sub('\.\.+', '.', review)
    review = re.sub('\.(?!\s|\d|$)', '. ', review)

    for sentence in nltk.sent_tokenize(review):
        # Extract keywords
        rake.extract_keywords_from_text(sentence)
        keywords = rake.get_ranked_phrases_with_scores()
        
        # Get sentence sentiment
        sentiment = sia.polarity_scores(sentence)['compound']
        
        # Add sentiment to each keyword
        for score, keyword in keywords:
            sentiment_keywords.append({
                "keyword": keyword, 
                "score": round(score, 2), 
                "sentiment": round(sentiment, 2),
                "sentence": sentence
            })

    sorted_list = sorted(sentiment_keywords, key=lambda x: (x['score'],x['sentiment']), reverse=True)
    
    return sorted_list # list of {keyword, score, sentiment, sentence}

def evaluate_reviews(reviews: list[str]):
    all_results = []
    for text in reviews:
        result = evaluate(text)
        all_results.extend(result)
        
    return sorted(all_results, key = lambda res: (res['score'], res['sentiment']), reverse=True)

def evaluate_full_text(text):
    # Extract keywords with sentiment
    rake.extract_keywords_from_text(text)
    keywords = rake.get_ranked_phrases_with_scores()
    
    keywords = sorted(keywords, key=lambda item: item[0], reverse=True)
    
    # Get sentence sentiment
    sentiment = sia.polarity_scores(text)['compound']
    # keys = list(map(lambda item: item[1], keywords))
    
    result_json = {
        "keyword": keywords,
        "sentiment": sentiment,
    }
    return result_json

# text = "This product is amazing! It's very easy to use and has all the features I need. I especially love the design and the quality of the materials used. The only downside is that it's a bit expensive."
# evaluate(text)