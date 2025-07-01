from textblob import TextBlob

def txt_analyze(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity # type: ignore
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"
    
print(txt_analyze("I love this"))
print(txt_analyze("I hate this"))
    