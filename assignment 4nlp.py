from nltk.corpus import reuters
from nltk.tokenize import TreebankWordTokenizer

import nltk
print(reuters.categories())

freqDist = nltk.ConditionalFreqDist((genre,word) for genre in reuters.categories() for word in reuters.words(categories=genre))
print(freqDist.tabulate())
