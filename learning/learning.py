import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

dataset = pd.read_csv('learning\\spam_ham_dataset.csv')
dataset.drop(['values', 'label'], axis='columns', inplace=True)
X = dataset.iloc[:, [0]].values
y = dataset.iloc[:, [-1]].values

cv = CountVectorizer()
X_modify = cv.fit_transform(X.ravel())

X_train, X_test, y_train, y_test = train_test_split(X_modify, y, test_size=0.3)

mb = MultinomialNB()
mb.fit(X_train, y_train)
# print(mb.score(X_test, y_test))
def test(data):
    data_tr=cv.transform(data)
    y_pred = mb.predict(data_tr)
    #SPAM = 1 AND HAM = 0
    return y_pred

# test(["how are you man are you doing great"])