import spacy

# Load the small English NLP model
nlp = spacy.load("en_core_web_sm")

# Input text
text = "Elon Musk founded SpaceX in 2002. The company is worth over $100 billion."

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