def classify_blooms_level(text):
    blooms_levels = {
        "Remember": ["define", "list", "recall", "identify", "recognize", "describe"],
        "Understand": ["explain", "summarize", "interpret", "discuss", "classify"],
        "Apply": ["use", "implement", "carry out", "execute", "solve"],
        "Analyze": ["differentiate", "organize", "structure", "compare", "contrast"],
        "Evaluate": ["justify", "defend", "critique", "evaluate", "argue"],
        "Create": ["design", "construct", "develop", "formulate", "compile"]
    }

    results = {level: [] for level in blooms_levels}
    lines = text.split(".")  # splitting into sentences
    
    for line in lines:
        lower_line = line.lower()
        for level, verbs in blooms_levels.items():
            for verb in verbs:
                if verb in lower_line and line not in results[level]:
                    results[level].append(line.strip())

    return results
