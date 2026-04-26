def calculate_final_score(match_score, interest_score):
    final = (match_score * 0.7) + (interest_score * 0.3)
    return round(final, 2)