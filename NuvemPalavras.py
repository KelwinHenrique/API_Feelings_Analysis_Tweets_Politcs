import matplotlib.pyplot as plt
import nltk
import re
from nltk.corpus import wordnet
from wordcloud import WordCloud
import pandas as pd

dataset = pd.read_csv('TweetsPoliticos.csv',encoding='latin-1')

total = dataset['tweet'].values
text = ""

for i in range(len(total)):
    text = text + " " + str(dataset['tweet'].values[i])

text = text.replace("lula", '').replace("de", '').replace("da", '').replace("que", '').replace("nao", '').replace("ou", '').replace("na", '').replace("em", '').replace("para", '').replace("os", '').replace("dos", '')
text = text.replace("eu", '').replace("ja", '').replace("ele", '').replace("ao", '').replace("uma", '').replace("um", '').replace("por", '').replace("era", '')



wordcloud = WordCloud(max_font_size=100,width = 1520, height = 535).generate(text)

plt.figure(figsize=(16,9))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()