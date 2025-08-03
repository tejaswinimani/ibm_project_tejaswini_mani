import spacy

nlp = spacy.load("en_core_web_sm")

def extract_key_sections(text):
    doc = nlp(text)
    course_title = None
    objectives = []
    outcomes = []
    
    lines = text.split('\n')
    for line in lines:
        lower = line.lower()
        if "course title" in lower:
            course_title = line
        elif "objective" in lower:
            objectives.append(line)
        elif "outcome" in lower:
            outcomes.append(line)

    return {
        "title": course_title,
        "objectives": objectives,
        "outcomes": outcomes
    }
