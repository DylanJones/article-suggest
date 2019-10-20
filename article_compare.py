#!/usr/bin/env python3
import csv
import json
import sys
import numpy as np
from numpy.linalg import norm
import spacy

csv.field_size_limit(sys.maxsize)
print("Loading model...")
nlp = spacy.load('en_trf_bertbaseuncased_lg')
print("Model Loaded.")

def read_csv(*fnames):
    article_texts = []
    # read texts
    for fn in fnames:
        with open(fn) as f:
            f.readline() # get rid of headers
            reader = csv.reader(f)
            for line in reader:
                yield line

def find_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (norm(vec1) * norm(vec2))


db = []
vectors = []
for item in read_csv('final_vectors.csv'):
    item[2] = [float(x) for x in item[2].split(' ')]
    db.append(item)
    vectors.append(item[2])

vectors = np.asarray(vectors)

text = nlp(input())

vec = text.vector

# find the closest one


