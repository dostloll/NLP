from textblob import TextBlob

def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity#type: ignore
    print(polarity)
    if polarity > 0.2 :
        return "positive"
    elif polarity < -0.2:
        return "negative"
    else:
        return "neutral"

def analyze_comments(comments):
    counts = {"positive": 0, "negative": 0, "neutral": 0}
    for comment in comments:
        sentiment = get_sentiment(comment)
        counts[sentiment] += 1
    return counts