def match_candidate(candidate, jd):
    jd_skills = jd["skills"]

    if not jd_skills:
        return 0

    matched_skills = set(candidate["skills"]) & set(jd_skills)

    skill_match = len(matched_skills) / len(jd_skills)

    exp_match = min(candidate["experience"] / jd["experience"], 1)

    keyword_similarity = 0.8  # fixed for simplicity

    match_score = (
        skill_match * 50 +
        exp_match * 30 +
        keyword_similarity * 20
    )

    return round(match_score, 2), list(matched_skills)