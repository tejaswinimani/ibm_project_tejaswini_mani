import spacy

# Load the medium-sized English model
nlp = spacy.load("en_core_web_md")

# Define Blooms taxonomy verbs and their levels
blooms_taxonomy = {
    "Knowledge": ["define", "describe", "identify", "label", "list", "match", "name", "recall", "recognize", "reproduce", "select", "state"],
    "Comprehension": ["classify", "convert", "defend", "distinguish", "estimate", "explain", "extend", "generalize", "give", "infer", "paraphrase", "predict", "rewrite", "summarize", "translate"],
    "Application": ["apply", "change", "compute", "construct", "demonstrate", "discover", "manipulate", "modify", "operate", "predict", "prepare", "produce", "relate", "show", "solve", "use"],
    "Analysis": ["analyze", "appraise", "breakdown", "calculate", "categorize", "compare", "contrast", "criticize", "diagram", "differentiate", "discriminate", "distinguish", "examine", "experiment", "identify", "illustrate", "infer", "model", "outline", "point out", "question", "relate", "select", "separate", "subdivide", "test"],
    "Synthesis": ["arrange", "assemble", "collect", "compose", "construct", "create", "design", "develop", "formulate", "manage", "organize", "plan", "prepare", "propose", "set up", "write"],
    "Evaluation": ["appraise", "argue", "assess", "attach", "choose", "compare", "defend", "estimate", "evaluate", "judge", "predict", "rate", "score", "select", "support", "value"]
}

def classify_blooms_level(sentences):
    results = {}
    for text in sentences:
        text = text.strip()
        if not text:
            continue
        doc = nlp(text.lower())
        for token in doc:
            for level, verbs in blooms_taxonomy.items():
                if token.lemma_ in verbs:
                    results[text] = level
                    break
            if text in results:
                break
        if text not in results:
            results[text] = "Not Classified"
    return results
