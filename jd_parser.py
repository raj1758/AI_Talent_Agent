def parse_jd(jd_text: str):
    jd_text = jd_text.lower()

    known_skills = ["python", "sql", "react", "django", "javascript", "flask"]

    found_skills = []
    for skill in known_skills:
        if skill in jd_text:
            found_skills.append(skill)

    experience = 3  # default

    for word in jd_text.split():
        if word.isdigit():
            experience = int(word)

    return {
        "skills": found_skills,
        "experience": experience
    }