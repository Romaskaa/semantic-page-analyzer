from collections import Counter

def extract_keywords(words, top_n=50):
    counter = Counter(words)
    return [(word, int(count)) for word, count in counter.most_common(top_n)]