def estimate_improvement(errors):

    score = 100

    penalty = len(errors) * 5

    new_score = score - penalty

    improvement = penalty

    return {
        "current_score": new_score,
        "improvement_if_fixed": improvement
    }