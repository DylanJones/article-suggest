import gensim.downloader as api
import json
import random
import csv, sys, re, string
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from scipy.sparse import coo_matrix
import numpy as np
#input: model, keywords associated with article titles, keywords for current article
#iterate through database of article titles vs keywords, return articles with
#largest & betw two sets (curr article keywords & curr element in database)

NUM_WORDS = 10 #the top keywords from each article to compare against each other
with open("all-keywords.txt", "r") as read_file:
    keywords = json.load(read_file)

with open("all-title.txt", "r") as read_file2:
    titles = json.load(read_file2)

def sort_coo(coo_matrix):
    tuples = zip(coo_matrix.col, coo_matrix.data)
    return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)

def extract_results(feature_names, sorted_items):  
    score_vals = []
    feature_vals = []
    # word index and corresponding tf-idf score
    for idx, score in sorted_items:
        #keep track of feature name and its corresponding score
        score_vals.append(round(score, 3))
        feature_vals.append(feature_names[idx])
    #create a tuples of feature,score
    #results = zip(feature_vals,score_vals)
    results= {}
    for idx in range(len(feature_vals)):
        results[feature_vals[idx]]=score_vals[idx]
    return results


def get_keywords(text):
    #get english stopwords from nltk
    from nltk.corpus import stopwords
    stopWords = set(stopwords.words('english'))

    #read the news articles and titles from dataset
    textList = [text]

    #remove all unnecessary words from dataset
    pattern = re.compile('[^a-z A-Z]')
    cleanText = []
    textList[0] = pattern.sub('', textList[0])
    lem = WordNetLemmatizer()
    text = [lem.lemmatize(word) for word in textList[0].split() if word not in stopWords]
    text = " ".join(text)
    cleanText.append(text)

    #vectorize words
    # print("vectorizing words")
    cv=CountVectorizer(max_df=1,stop_words=list(stopWords), max_features=10000, ngram_range=(1,3))
    # print("fitting to model")
    X=cv.fit_transform(cleanText)

    #tf-idf calculation
    # print("transform tfidf to model")
    tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
    # print("fit model to tfidf values")
    tfidf_transformer.fit(X)
    # print("getting feature names")
    feature_names=cv.get_feature_names()

    #tf-idf convert to keywords ranking
    tf_idf_vector=tfidf_transformer.transform(cv.transform([cleanText[0]]))
    sorted_items=sort_coo(tf_idf_vector.tocoo())
    keywords=extract_results(feature_names,sorted_items)

    return keywords


def get_similar(text):
    orig_keywords = get_keywords(text)
    kywds = set(list(orig_keywords.keys())[:NUM_WORDS])

    max = 0
    index = 0
    
    n_intersects = []

    for i in range (0, len(keywords)):
        temp = set(list(keywords[i].keys())[:NUM_WORDS])
        n_intersects.append(len(kywds.intersection(temp)))
        if len(kywds.intersection(temp)) > max:
            max = len(kywds.intersection(temp))
            index = i

    n_intersects = np.asarray(n_intersects)
    #print("ORIGINAL: \n" + title)
    for i in np.flip(np.argsort(n_intersects))[:5]:
        print(titles[i])

if __name__ == '__main__':
    text= input("Enter Text >>> ")
    get_similar(text)
