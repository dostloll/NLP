import spacy
import re

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

# Example usage
if __name__ == "__main__":
    with open("data/input.txt", "r", encoding="utf-8") as f:
        raw = f.read()
    cleaned = clean_text(raw)
    print("Original:", raw)
    print("Cleaned:", clean_text(raw))
    with open("output.txt","w",encoding="utf-8") as f:
        f.write(cleaned)