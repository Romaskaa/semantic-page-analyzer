from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def cluster_keywords(keywords):
    words = [k[0] for k in keywords]

    if not words:
        return {"0": ["нет слов для кластеризации"]}

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(words)

    kmeans = KMeans(n_clusters=min(5, len(words)))
    kmeans.fit(X)

    clusters = {}
    for word, label in zip(words, kmeans.labels_):
        clusters.setdefault(str(label), []).append(str(word))

    return clusters