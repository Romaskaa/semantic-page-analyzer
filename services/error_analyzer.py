WEIGHTS = {
    "Отсутствует title": 15,
    "Нет meta description": 10,
    "Нет H1": 10,
    "Слишком много H1": 5,
    "Нет canonical": 5,
    "Нет JSON-LD schema": 10,
    "Мало текста на странице (<300 слов)": 10
}

def estimate_improvement(errors):

    score = 100
    penalty = 0

    for error in errors:

        penalty += WEIGHTS.get(error, 3)

    new_score = max(0, score - penalty)

    return {
        "current_score": new_score,
        "improvement_if_fixed": penalty
    }