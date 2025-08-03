import spacy

nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    doc = nlp(text)
    keywords = [chunk.text for chunk in doc.noun_chunks if len(chunk.text) > 3]
    # Optional: deduplicate and sort
    keywords = list(set([word.strip().lower() for word in keywords]))
    return sorted(keywords)
