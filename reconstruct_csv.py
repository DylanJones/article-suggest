#!/usr/bin/env python3
import os
import csv
import sys
import json

csv.field_size_limit(sys.maxsize)
n = 64

vectors = []

def read_corpus(*fnames):
    article_texts = []
    # read texts
    for fn in fnames:
        with open(fn) as f:
            f.readline() # get rid of headers
            reader = csv.reader(f)
            for line in reader:
                if len(line[9]) > 50:
                    yield line

print('reading files...')
for i in range(n):
    print(f'workin on {i}')
    with open(os.path.join('vectors', f'{i}.txt')) as f:
        for line in f:
            if line.startswith('['):
                vectors.append([float(x) for x in line.replace('[','').replace(']', '').replace(',', '').strip().split(' ')])

print('reading csv')
with open('final_vectors.csv', 'w') as f:
    for i,item in enumerate(read_corpus('articles.csv')):
        vec = ' '.join([str(x) for x in vectors[i]])
        f.write(f'{item[2].strip()},{item[8].strip()},{vec}\n')

print('writing json...')
with open('giggity.json', 'w') as f:
    json.dump(vectors, f)
