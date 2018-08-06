# Natural Language Processing

# Part-1 --> Preprocessing the Reviews


# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Importing the dataset
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)


# Cleaning the texts
# re library is useful when working with strings and text expressions
import re 

# nltk is a very useful library for NLP
import nltk

# stopwords is a list of words of potentially no significance in prediction
nltk.download('stopwords')

# importing the stopwords file
from nltk.corpus import stopwords

# PorterStemmer class is used to keep only the root of a word and remove its variations (loving, loved, loves is changed to love) 
from nltk.stem.porter import PorterStemmer

corpus = []
for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i]) #keeps only the alphabets and removes special characters, numbers, punctuations
    review = review.lower()  # converts all words to lowercase
    review = review.split()  # for further processing each word individually, each review is converted into a list of words using 'split'
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review) # coverts the list of words back to a sentence of words
    corpus.append(review)
    
# corpus is now a preprocessed list of reviews    
    
    