import spacy

# Load the small English NLP model
nlp = spacy.load("en_core_web_sm")

# Input text
with open("data/input.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Process the text
doc = nlp(text)

# Print tokens and their parts of speech
print("🔹 Tokens and POS Tags:")
for token in doc:
    print(f"{token.text:<12} {token.pos_:<10} {token.lemma_:<10}")

# Print named entities
print("\n🔹 Named Entities:")
for ent in doc.ents:
    print(f"{ent.text:<20} {ent.label_}")