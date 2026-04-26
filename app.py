from fastapi import FastAPI
import json

from jd_parser import parse_jd
from matcher import match_candidate
from engagement import simulate_conversation
from scoring import calculate_final_score

app = FastAPI(title="AI Talent Scouting Agent")

# Load candidates
with open("candidates.json") as f:
    candidates = json.load(f)


@app.get("/")
def home():
    return {"message": "AI Talent Scouting Agent is running"}


@app.post("/process_jd")
def process_jd(jd_text: str):
    jd = parse_jd(jd_text)

    results = []

    for candidate in candidates:
        match_score, matched_skills = match_candidate(candidate, jd)

        engagement = simulate_conversation(candidate["name"])

        interest_score = engagement["interest_score"]

        final_score = calculate_final_score(match_score, interest_score)

        results.append({
            "name": candidate["name"],
            "skills": candidate["skills"],
            "matched_skills": matched_skills,
            "match_score": match_score,
            "interest_score": interest_score,
            "final_score": final_score,
            "ai_response": engagement["response"]
        })

    # Sort by final score
    ranked = sorted(results, key=lambda x: x["final_score"], reverse=True)

    return {
        "jd_parsed": jd,
        "ranked_candidates": ranked
    }