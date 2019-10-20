#!/usr/bin/env python3
import json
import numpy as np
from numpy.linalg import norm
import spacy

print("Loading model...")
nlp = spacy.load('en_trf_bertbaseuncased_lg')
print("Model Loaded.")

def read_csv(*fnames):
    article_texts = []
    # read texts
    for fn in fnames:
        with open(fn) as f:
            #f.readline() # get rid of headers
            for line in f:
                try:
                    line = line.strip().split(',')
                    title = ','.join(line[:-2])
                    url = line[-2]
                    vec = line[-1]
                    yield [title, url, vec]
                except: 
                    print('urbad')
                    pass

def find_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (norm(vec1) * norm(vec2))


db = []
vectors = []
for item in read_csv('final_vectors.csv'):
    #print(item)
    item[2] = [float(x) for x in item[2].split(' ')]
    db.append([item[0], item[1]])
    vectors.append(item[2])

vectors = np.asarray(vectors)

text = nlp(input("Enter Article >>> "))

vec = text.vector

sims = np.asarray([find_similarity(vec, x) for x in vectors])
indexes = np.argsort(sims)

for a in indexes[:5]:
    print(db[a])
