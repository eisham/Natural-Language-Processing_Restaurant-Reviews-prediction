# Part-2 --> Creating Bag of Words model

from sklearn.feature_extraction.text import CountVectorizer


# CountVectorizer is used to create a sparse matrix of unique words as features and each row corresponding to a review 
cv = CountVectorizer(max_features = 1500) # max_features parameter indicates how many most frequent words we want to take


# Take 'corpus' from the previous file named 'Preprocessing_NLP.py'
X = cv.fit_transform(corpus).toarray() # X is our Input independent features
y = dataset.iloc[:, 1].values          # y is the target variable
