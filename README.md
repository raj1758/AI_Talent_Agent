AI-Powered Talent Scouting & Engagement Agent

# Overview

Recruiters spend hours filtering candidates and manually assessing their interest.
This project automates candidate discovery, matching, and engagement using an AI-inspired scoring system.

# Features

Extracts skills and experience from Job Description (JD)
Matches candidates based on skill overlap and experience
Simulates candidate interest using realistic recruiter-facing responses
Generates a ranked shortlist using combined scoring

# Tech Stack
Python
FastAPI
JSON (mock database)

# How to Run Locally

python -m venv .venv
.\.venv\Scripts\activate
python -m pip install fastapi uvicorn
python -m uvicorn app:app --reload

Open:
http://127.0.0.1:8000/docs

# API Endpoint

POST /process_jd

# Sample Input

"Looking for a Python developer with SQL and React, 3 years experience"

# Sample Output

{
  "jd_parsed": {
    "skills": ["python", "sql", "react"],
    "experience": 3
  },
  "ranked_candidates": [
    {
      "name": "Kiran",
      "match_score": 92,
      "interest_score": 88,
      "final_score": 90
    }
  ]
}


# Architecture

JD Parser → Extracts skills and experience
Candidate Matcher → Compares candidates with JD
Engagement Module → Simulates candidate intent
Scoring Engine → Combines match and interest scores


# Scoring Logic

Match Score
Skills → 50%
Experience → 30%
Keyword similarity → 20%
Final Score
Final Score = 0.7 × Match Score + 0.3 × Interest Score
