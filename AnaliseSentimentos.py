import nltk
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.model_selection import cross_val_predict

dataset = pd.read_csv('TweetsPoliticos.csv',encoding='latin-1')

dataset = dataset.loc[(dataset["polaridade"]=="negativo") | (dataset["polaridade"]=="positivo"), ["tweet", "polaridade"]]


tweets = dataset['tweet'].values
classes = dataset['polaridade'].values





def PreprocessamentoSemStopWords(instancia):
    #remove links dos tweets
    #remove stopwords
    instancia = re.sub(r"http\S+", "", instancia).lower().replace(',','').replace('.','').replace(';','').replace('-','')
    stopwords = set(nltk.corpus.stopwords.words('portuguese'))
    palavras = [i for i in instancia.split() if not i in stopwords]
    return (" ".join(palavras))

def Preprocessamento(instancia):
    #remove links, pontos, virgulas,ponto e virgulas dos tweets
    #coloca tudo em minusculo
    instancia = re.sub(r"http\S+", "", instancia).lower().replace(',','').replace('.','').replace(';','').replace('-','').replace(':','').replace('é','e').replace('!','').replace('?','').replace('í','i').replace('á','a')
    return (instancia)

print("Todos os Dados")
print(dataset.count())
print("Positivos")
print(dataset[dataset.polaridade=='positivo'].count())
print("Negativos")
print(dataset[dataset.polaridade=='negativo'].count())
print("Neutros")
print(dataset[dataset.polaridade=='neutro'].count())

'''

vectorizer = CountVectorizer(ngram_range=(1,2))
freq_tweets = vectorizer.fit_transform(tweets)
modelo = MultinomialNB()
modelo.fit(freq_tweets,classes)
'''


vectorizer = CountVectorizer(analyzer="word")
freq_tweets = vectorizer.fit_transform(tweets)
modelo = MultinomialNB()
modelo.fit(freq_tweets,classes)


resultados = cross_val_predict(modelo, freq_tweets, classes, cv=10)
percentualAcertos = metrics.accuracy_score(classes,resultados)

print(percentualAcertos)

sentimento=['positivo','negativo']
print (metrics.classification_report(classes,resultados,sentimento))

print (pd.crosstab(classes, resultados, rownames=['Real'], colnames=['Predito'], margins=True))




