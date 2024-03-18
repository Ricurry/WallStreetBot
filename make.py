import pandas as pd 
import csv

from textblob import TextBlob 
from textblob.classifiers import NaiveBayesClassifier 

WSBWords =  [
    ('Good', 'pos'),
    ('Great', 'pos' ), #Yolo is the worst fucking thing you can see in a WSB post.
    ('Bad', 'neg'),
    ('Awesome', 'pos'),
    ('OK',  'neu'),
    ('Amazing', 'pos'),
    ('Weird', 'neg'),
    ('Bad Smell', 'neg' ),
    ('Low Rating', 'neg')
]
cl = NaiveBayesClassifier(WSBWords) 

sym = pd.read_csv('csv/perfume.csv')
symlist = list(sym['Symbol'])
symlen = len(symlist)

posts = pd.read_csv('csv/Posts.csv')
postlist = list(posts['Posts By WSB'])
post_new = []

postlen = len(postlist)
i = 0
f = 0
while i< postlen:
    print(postlist[i])
    print(cl.classify(postlist[i]))
    if (cl.classify(postlist[i]) == 'pos'):
        post_new.extend(postlist[i].split())
                    

    i+=1

for someposts in post_new:
    for syms in symlist:
        if syms == someposts:
            print(syms)