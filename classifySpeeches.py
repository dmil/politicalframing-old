from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
import numpy as np

#categories = ['education','health_care','immigration','marriage','middle_east']
categories = ['D','R']
training_set = load_files('/home/dhrumil/Desktop/PoliticalFraming/data/training/immigration',categories=categories,shuffle=True)

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(training_set.data)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

clf = MultinomialNB(alpha=1.0,fit_prior=False).fit(X_train_tfidf,training_set.target)

testing_set = load_files('/home/dhrumil/Desktop/PoliticalFraming/data/testing',categories=categories,shuffle=True)
docs_test = testing_set.data
#X_new_counts = count_vect.transform(docs_test)
#X_new_tfidf = tfidf_transformer.transform(X_new_counts)

##
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')
X_new_tfidf =  vectorizer.fit_transform(testing_set.data)
##

predicted = clf.predict(X_new_tfidf)
predicted_logs = clf.predict_log_proba(X_new_tfidf)

print np.mean(predicted == testing_set.target)

#f = open('classifyFiles.txt','w')
#f.write('The topics are in the following order:\n'+str(categories)+'\n\n')
#f.write('The predicted values for the training set:\n'+str(predicted)+'\n\n')
#f.write('The actual values for the training set:\n0 0 0 0 0 1 1 1 1 1 2 2 2 2 2 3 3 3 3 3 4 4 4 4 4 5 5 5 5 5 6 6 6 6 6\n\n')
#f.write('Log-Likelihoods:\n'+str(predicted_logs)+'\n\n')
#f.close()
