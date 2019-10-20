import spacy
import csv
import sys

csv.field_size_limit(sys.maxsize)

def read_corpus(*fnames):
    article_texts = []
    # read texts
    for fn in fnames:
        with open(fn) as f:
            f.readline() # get rid of headers
            reader = csv.reader(f)
            for line in reader:
                if len(line[9]) > 50:
                    yield line[9]


train = list(read_corpus('articles.csv'))
#train = list(read_corpus('articles1.csv', 'articles2.csv'))

with open('articles.txt', 'w') as f:
    f.write('\n'.join(train))
