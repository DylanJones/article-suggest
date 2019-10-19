import csv, sys, re, string,json
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
csvfile1 = open("all-the-news/articles1.csv")
csvfile2 = open("all-the-news/articles2.csv")
csvfile3 = open("all-the-news/articles3.csv")
myText1 = csv.reader(csvfile1)
myText2 = csv.reader(csvfile2)
myText3 = csv.reader(csvfile3)
csv.field_size_limit(sys.maxsize)
titles = []
textList = []
for item in myText1:
    titles.append(item[2])
    textList.append(item[9].lower())
for item2 in myText2:
    titles.append(item2[2])
    textList.append(item2[9].lower())
for item3 in myText3:
    titles.append(item3[2])
    textList.append(item3[9].lower())
# print(len(textList))
textList.pop(0)
titles.pop(0)

#remove all unnecessary words from dataset
pattern = re.compile('[^a-z A-Z]')
cleanText = []
for i, item in enumerate(textList):
    print(i)
    item = pattern.sub('', item)
    lem = WordNetLemmatizer()
    text = [lem.lemmatize(word) for word in item.split() if word not in stopWords]
    text = " ".join(text)
    cleanText.append(text)

#vectorize words
print("vectorizing words")
cv=TfidfVectorizer(max_df=0.85,stop_words=list(stopWords), ngram_range=(1,3))
print("fitting to model")
X=cv.fit_transform(cleanText)

print("getting feature names")
feature_names=cv.get_feature_names()
tfidf_lists = []
count = 0
#tf-idf convert to keywords ranking
for tfidf_calc in cleanText:
    print(count)
    count +=1
    sorted_items=sort_coo(X.transform([tfidf_calc]).tocoo())
    keywords=extract_results(feature_names,sorted_items)
    tfidf_lists.append(keywords)

titles_file = open("all-title.txt", "w")
#article_file = open("article.txt", "w")
results_file = open("all-keywords.txt", "w")

#save to file
#for q in range(len(titles)):
#    titles_file.write(titles[q])
#    #article_file.write(cleanText[q])
#    results_file.write(tfidf_lists[q])
titles_file.write(json.dumps(titles))
results_file.write(json.dumps(tfidf_lists))


print("len(titles)", len(titles))# list
print("len(cleanText)", len(cleanText))#print length
print("len(tfidf_lists)", len(tfidf_lists))#list of dicts

