import nltk
from nltk.corpus import brown,reuters
brown.categories()

for category in brown.categories():
    print("\nCategory: ",category,'\nWords: ', brown.words(categories=category))

reuters.categories()

for category in reuters.categories():
    print("\nCategory: ",category,'\nWords: ', reuters.words(categories=category))

