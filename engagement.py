import random

def simulate_conversation(candidate_name):
    responses = [
        ("Yes, I am very interested in this role", random.randint(85, 100)),
        ("Sounds interesting, open to discuss", random.randint(60, 80)),
        ("Not looking for a change right now", random.randint(20, 50))
    ]

    response, score = random.choice(responses)

    return {
        "candidate": candidate_name,
        "response": response,
        "interest_score": score
    }