
from nltk.corpus import stopwords

stopwords.words('english')[:10]

import nltk

entries = nltk.corpus.cmudict.entries()
len(entries)
for entry in entries[100:125]:
    print(entry)

from nltk.corpus import wordnet as wn
wn.synsets('motorcar') #We'll get an ID for subsets.
wn.synset('car.n.01').lemma_names()

import nltk
texts = ["Hello i study computer science and my name is anant sakalle"]
for text in texts:
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        tagged_words = nltk.pos_tag(words)
        print(tagged_words)

import nltk
from nltk.tokenize import TweetTokenizer
text = "Hello people! I love to play football and listen to music. I also love spicy food"
twtkn = TweetTokenizer()
st = list(twtkn.tokenize(text))
print(st)
