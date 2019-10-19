'''
input format: "title", file_name.txt

'''


import csv, sys, re, string
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import coo_matrix

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


#get english stopwords from nltk
from nltk.corpus import stopwords
stopWords = set(stopwords.words('english'))

#read the news articles and titles from dataset
title, file_ = input().split(", ")
f = open(file_)
textList = [f.read()]
titles = [title]

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
cv=TfidfVectorizer(max_df=1,stop_words=list(stopWords), max_features=10000, ngram_range=(1,3))
# print("fitting to model")
X=cv.fit_transform(cleanText)

#tf-idf calculation
# print("getting feature names")
feature_names=cv.get_feature_names()
tf_idf_vector=cv.transform([cleanText[0]])
sorted_items=sort_coo(tf_idf_vector.tocoo())
keywords=extract_results(feature_names,sorted_items)

# titles_file = open("title.txt", "w")
# #article_file = open("article.txt", "w")
# results_file = open("keywords.txt", "w")

# #save to file
# for q in range(len(titles)):
#     titles_file.write(titles[q])
#     #article_file.write(cleanText[q])
#     results_file.write(tfidf_lists[q])

# print("len(titles)", len(titles))
# print("len(cleanText)", len(cleanText))
# print("len(tfidf_lists)", len(tfidf_lists))
print(keywords)
