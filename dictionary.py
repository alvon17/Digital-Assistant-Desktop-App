import nltk
from nltk.metrics.distance import jaccard_distance
from nltk.util import ngrams

correct_words = ['my', 'is', 'it', 'on', 'are', 'bye', 'how', 'you', 'find', 'hello', 'open', 'play', 'stop', 'time', 'wait', 'what', 'abort', 'gmail', 'music', 'laptop', 'google', 'search', 'nothing', 'youtube', 'facebook', 'location', 'shutdown', 'something']

def check_words(query):
    final_words = []
    for word in query:
        temp = [(jaccard_distance(set(ngrams(word, 2)),
                                set(ngrams(w, 2))),w)
                for w in correct_words if w[0]==word[0]]
        
        final_words.append(sorted(temp, key = lambda val:val[0])[0][1])
    final = ' '.join(final_words)
    return final

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    return tokens
