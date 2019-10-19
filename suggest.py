import gensim.downloader as api
import json
import random
#input: model, keywords associated with article titles, keywords for current article
#iterate through database of article titles vs keywords, return articles with
#largest & betw two sets (curr article keywords & curr element in database)

NUM_WORDS = 10 #the top keywords from each article to compare against each other
with open("keywords.txt", "r") as read_file:
    keywords = json.load(read_file)

with open("title.txt", "r") as read_file2:
    titles = json.load(read_file2)

og_index = random.randint(0, len(titles))
kywds = set(list(keywords[og_index].keys())[:NUM_WORDS])

max = 0
index = 0
for i in range (0, len(keywords)):
    temp = set(list(keywords[i].keys())[:NUM_WORDS])
    if len(kywds.intersection(temp)) > max and i != og_index:
        max = len(kywds.intersection(temp))
        index = i
print("ORIGINAL: \n" + titles[og_index])
print("\nSUGGESTED: \n" + titles[index])
