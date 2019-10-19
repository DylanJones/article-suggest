import json
import gensim
import time

print("Loading model...")
model = gensim.models.KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin', binary=True)
print("Model loaded.")

with open('articles.json') as f:
    articles = json.load(f)

def sanitize_keywords(badWords):
    OutWords = []
    for word in badWords:
        word = word.lower().replace(" ", "_")
        if word in model:
            OutWords.append((word, badWords[word.replace('_', ' ')]))
        if len(OutWords) >= 10:
            break
    return dict(OutWords)


def main():
    t = time.time()

    new_articles = []
    
    for i,article in enumerate(articles):
        keywords = sanitize_keywords(article['keywords'])
        if len(keywords) >= 10:
            new_articles.append({"title": article["title"], "keywords": keywords})
    
    print(time.time() - t)

    with open("articles_clean.json", "w") as f:
        json.dump(new_articles, f)

if __name__ == '__main__':
    main()
