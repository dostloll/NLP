import requests
from bs4 import BeautifulSoup
import spacy

# Load spaCy
nlp = spacy.load("en_core_web_sm")

# Fetch content from website
url = "https://en.wikipedia.org/wiki/Natural_language_processing"
response = requests.get(url)

# Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Extract all paragraph text
paragraphs = soup.find_all("p")
text = "\n".join(p.get_text() for p in paragraphs)

# Run through spaCy
doc = nlp(text)

# Print named entities
for ent in doc.ents:
    print(ent.text, ent.label_)