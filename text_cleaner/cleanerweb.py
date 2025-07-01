import spacy
import requests
import re
from bs4 import BeautifulSoup


nlp = spacy.load("en_core_web_sm")

def clean_text(text):

    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)

    doc = nlp(text)

    cleaned_tokens = [
     token.lemma_ for token in doc
     if not token.is_stop and not token.is_punct and not token.is_space
    ]

    return " ".join(cleaned_tokens)

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Natural_language_processing"
    response = requests.get(url)

    # Parse the HTML
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")
    text = "\n".join(p.get_text() for p in paragraphs)
    
    #Original Text
    print("The original text is :",text)

    #Refined Text
    print("The clean text is :",clean_text(text))
    