from nltk.corpus import brown
from nltk.probability import FreqDist, ConditionalFreqDist
from nltk.tokenize import RegexpTokenizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud


distCondFreq = ConditionalFreqDist()
for word in RegexpTokenizer(r'\w+').tokenize(" ".join(brown.words())):
    length = len(word)
    distCondFreq[length][word] +=1

for length in distCondFreq:
    for word in distCondFreq[length]:
        if(length>1 and length < 5):
            print(word,distCondFreq[length].freq(word)," ",length)

freqDist = FreqDist(word for word in RegexpTokenizer(r'\w+').tokenize(" ".join(brown.words())))

mat = freqDist.most_common(20)
freqDist.plot(30, cumulative=False)
print(" \n".join([str(i) for i in mat]))

distinct = (" ").join(brown.words())
cloudofwords = WordCloud(width = 1500, height = 1500).generate(distinct)
plt.imshow(cloudofwords)
plt.axis("off")
plt.show()
plt.close()
