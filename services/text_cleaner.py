import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

nltk.download('punkt_tab')
nltk.download('stopwords')

stop_words = set(stopwords.words("russian") + stopwords.words("english"))
stemmer_ru = SnowballStemmer("russian")
stemmer_en = SnowballStemmer("english")

def clean_text(text):
    sentences = sent_tokenize(text)
    words = []

    for s in sentences:
        tokens = word_tokenize(s.lower())
        filtered = []
        for w in tokens:
            if w.isalpha() and w not in stop_words:
                if all('а' <= c <= 'я' or 'А' <= c <= 'Я' for c in w):
                    filtered.append(stemmer_ru.stem(w))
                else:
                    filtered.append(stemmer_en.stem(w))
        words.extend(filtered)

    return words