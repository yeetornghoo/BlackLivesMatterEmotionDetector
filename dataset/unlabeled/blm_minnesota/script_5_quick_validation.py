import pandas as pd
import pickle
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.feature_extraction.text import CountVectorizer
from Controller import LogController

dir_path = "C:/workspace/SocialMovementSentiment/dataset/master/"

# LOAD PRETRAINED MODEL
clf_model = pickle.load(open(dir_path+"model/model_linearsvc_bow.sav", 'rb'))
wvc_model = pickle.load(open(dir_path+"model/bow.pickle", 'rb'))

# LOAD TEST DATA
df = pd.read_csv("baseline-dataset.csv", sep=",")
df = df[["sentiment", "tweet_text"]]
X = df['tweet_text'].values.astype('U')
y = df['sentiment'].values

print(X.shape)

# VECTOR
v_X_test = wvc_model.transform(X)

# PREDICTION
pred = clf_model.predict(v_X_test)

ac_value = round(accuracy_score(y, pred), 4)
f1_value = round(f1_score(y, pred, average='macro'), 4)
pr_value = round(precision_score(y, pred, average='macro'), 4)
re_value = round(recall_score(y, pred, average='macro'), 4)

LogController.log('Testing accuracy: {}'.format(accuracy_score(y, pred)))
LogController.log('Testing F1 score: {}'.format(f1_score(y, pred, average='macro')))
LogController.log('Testing Precision score: {}'.format(precision_score(y, pred, average='macro')))
LogController.log('Testing Recall score: {} \n'.format(recall_score(y, pred, average='macro')))