from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def extract_keywords_ngram(words, top_n=50, ngram_range=(1,2)):
    text = " ".join(words)
    vectorizer = TfidfVectorizer(ngram_range=ngram_range, stop_words="english")
    X = vectorizer.fit_transform([text])
    scores = np.asarray(X.sum(axis=0)).flatten()
    features = np.array(vectorizer.get_feature_names_out())
    top_idx = scores.argsort()[-top_n:][::-1]
    return [(features[i], round(scores[i],3)) for i in top_idx]

def compute_keyword_density(text, keywords):
    words = text.lower().split()
    total_words = len(words)
    density = {}
    for kw,_ in keywords:
        count = words.count(kw.lower())
        density[kw] = round((count/total_words)*100, 2) if total_words else 0
    return density