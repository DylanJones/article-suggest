import gensim

def read_corpus(*fnames, tokens_only=False):
    article_texts = []
    # read texts
    for fn in fnames:
        with open(fn) as f:
            f.readline() # get rid of headers
            for line in f:
                article_texts.append(','.join(f.readline().split(',')[9:]))

    for i, text in enumerate(article_texts):
        if tokens_only:
            yield gensim.utils.simple_preprocessor(text)
        else:
            yield gensim.models.doc2vec.TaggedDocument(gensim.utils.simple_preprocess(text), [i])


def train_model():
    model = gensim.models.doc2vec.Doc2Vec(vector_size=300, min_count=10, epochs=20)
    train_corpus = read_corpus('articles1.csv', 'articles2.csv')
    test_corpus = read_corpus('articles3.csv', tokens_only=True)
    print("Building vocabulary...")
    model.build_vocab(train_corpus)
    print("Training model...")
    model.train(train_corpus, total_examples=model.corpus_count, epochs=model.epochs)
    print("Saving model...")
    model.save("big_d2v.model")
    print("Training done!")



def main():
    train_model()

if __name__ == '__main__':
    main()
