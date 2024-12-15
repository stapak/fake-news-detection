


import numpy as np
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
import nltk
import joblib

def prepare_model():
  nltk.download('stopwords')
  news_dataset = pd.read_csv('train.csv')
  news_dataset.isnull().sum()
  news_dataset = news_dataset.fillna('')
  
  news_dataset['content'] = news_dataset['text']+' '+news_dataset['title']
  
  X = news_dataset.drop(columns='label', axis=1)
  Y = news_dataset['label']

  print('stage 1 clear')
 
  port_stem = PorterStemmer()

  def stemming(content):
    stemmed_content = re.sub('[^a-zA-Z]',' ',content)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [port_stem.stem(word) for word in stemmed_content if not word in stopwords.words('english')]
    stemmed_content = ' '.join(stemmed_content)
    return stemmed_content

  news_dataset['content'] = news_dataset['content'].apply(stemming) 
  
  #news_dataset['content'] = news_dataset['content']
  X = news_dataset['content'].values
  Y = news_dataset['label'].values
  print('stage 2 clear')
  vectorizer = TfidfVectorizer(max_features=500)
  vectorizer.fit(X)
  X = vectorizer.transform(X)

  X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, stratify=Y, random_state=2)
  model = LogisticRegression(max_iter=100)
  model.fit(X_train, Y_train)

  print('stage 3 clear')
  X_train_prediction = model.predict(X_train)
  training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

  X_test_prediction = model.predict(X_test)
  test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
  print('all clear')
  joblib.dump(vectorizer,'vectorizer.pkl')
  joblib.dump(model,'logistic_regression_model.pkl')
  

def news_testing(article):
  port_stem = PorterStemmer()
  def stemming(content):
      stemmed_content = re.sub('[^a-zA-Z]',' ',content)
      stemmed_content = stemmed_content.lower()
      stemmed_content = stemmed_content.split()
      stemmed_content = [port_stem.stem(word) for word in stemmed_content if not word in stopwords.words('english')]
      stemmed_content = ' '.join(stemmed_content)
      return [stemmed_content]
  X=stemming(article)
  #print("Stage 1",X)

  
  vectorizer = joblib.load('vectorizer.pkl')
  vectorizer.fit(X)
  X = vectorizer.transform(X)
  #print("stage 2",X)
  
  model=joblib.load('logisticRegression.pkl')
  prediction=model.predict(X)
  if (prediction[0]==0):
    print('The news is Real')
  else:
    print('The news is Fake')
  
  return prediction[0]



if __name__=='__main__':
   #prepare_model()
   article1=input('Enter the news article:')
   news_testing(article1)
   pass