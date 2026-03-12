def optimize_for_aio(keywords):

    questions = []

    for k,_ in keywords[:10]:

        questions.append(f"Что такое {k}?")

    return questions