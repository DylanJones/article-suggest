import spacy

nlp = spacy.load('en_trf_bertbaseuncased_lg')

while True:
    try:
        article = input()
        if len(article.strip()) > 5:
            article = nlp(article)
            vecs = article.vector
            print([a for a in vecs])
        else:
            print([0 for a in vecs])
    except EOFError:
        break
