import random

def simulate_conversation(candidate_name):
    responses = [
        ("Candidate is actively exploring new opportunities and aligns well with this role.", random.randint(85, 100)),
        ("Candidate is open to relevant opportunities and would like more details about the role.", random.randint(60, 80)),
        ("Candidate is not actively looking for a change but may consider suitable future opportunities.", random.randint(20, 50))
    ]

    response, score = random.choice(responses)

    return {
        "candidate": candidate_name,
        "response": response,
        "interest_score": score
    }
