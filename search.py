import json
import gensim
import time
from typing import List, Dict

print("Loading model...")
model = gensim.models.KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)
print("Model loaded.")

with open('articles_clean.json') as f:
    articles = json.load(f)[:1000]

#@jit
def find_similarity(keyA: Dict[str, float], keyB: Dict[str, float]):
    """
    :return the distance between keyword list A and keyword list B
    """
    total = 0
    for kw_a in keyA:
        # list of top keywords in B
        b_keywords: List[str] = list(keyB.keys())
        # distance from kw_a to all of the b_keywords
        distances: List[float] = model.distances(kw_a, b_keywords)

        for i,dist in enumerate(distances):
            total += dist * keyA[kw_a] * keyB[b_keywords[i]]
    return total / 10


def main():
    reference_keywords = articles[0]['keywords']
    t = time.time()
    best = None
    bsc= 0
    for i,article in enumerate(articles):
        print(f'{i}/{len(articles)}', end='\r')
        s = find_similarity(reference_keywords, article['keywords'])
        if s > bsc: 
            bsc = s
            best = article
    print()
    print(article)
    print(articles[0])
    print(bsc)

    print(time.time() - t)

if __name__ == '__main__':
    main()
