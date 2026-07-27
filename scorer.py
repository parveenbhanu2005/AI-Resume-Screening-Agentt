import re

def calculate_score(resume_text, job_description):
    """
    Calculate a simple keyword match score.
    """

    resume = resume_text.lower()
    jd = job_description.lower()

    keywords = re.findall(r"\b[a-zA-Z]+\b", jd)

    keywords = list(set(keywords))

    matched = 0

    for word in keywords:
        if word in resume:
            matched += 1

    score = round((matched / len(keywords)) * 100, 2)

    return score, matched, len(keywords)