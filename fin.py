import numpy as np
import pylab as pl
import matplotlib.pyplot as pl

from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
from sklearn import cross_validation, metrics
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import BernoulliNB,GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import maxabs_scale, FunctionTransformer, MaxAbsScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import train_test_split
from inspect import getmembers


data=np.loadtxt(open("data_one.csv","rb"),delimiter=",",skiprows=0)



enc = OneHotEncoder()
enc.fit(data)

print(enc.n_values_)
print(enc.feature_indices_)
print(enc.active_features_)

     #YY=enc.transform(data).toarray()
      #print YY[0]



Tdata = OneHotEncoder(categorical_features=[0,1,2,3,4,5,6,7,8,9,10,11,12,13])
TT=Tdata.fit_transform(data).toarray()






#Tdata = OneHotEncoder(categorical_features=[0,1,2,3,4,6,7,8,9,10,11,12,13,15])
#TT=Tdata.fit_transform(data).toarray()

#logtran = FunctionTransformer(np.log1p, accept_sparse=True)
#MaxAbsScaler().fit_transform(TT)
#YY = maxabs_scale(TT)



print TT[0]
#input('stop')

X, y =TT[:,:76],TT[:,77]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

et=ExtraTreesClassifier(n_estimators=500,verbose=1,max_depth=5,criterion='entropy')
et.fit(X_train,y_train)
importance=et.feature_importances_

print(importance)

#print(et.decision_path(X_train))
#input("stop")
print(et.score(X_test,y_test))
'''

clf = DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)
#tree = clf.fit(X_train, y_train)

print(clf.score(X_test,y_test))

print (clf.tree_.__getstate__())

'''


'''
rf=RandomForestClassifier(criterion='entropy',n_estimators=500,random_state=0,n_jobs=2,max_depth=6,max_features='log2')
rf.fit(X_train,y_train)

print(rf.score(X_test,y_test))
'''
#lr=LogisticRegression(penalty='l2', C=1, random_state=0, max_iter=100100, coef_=[4,76])
#lr.fit(X_train,y_train)

#print(lr.score(X_test,y_test))

#print et.decision_path(TT[:,:76])

#print et.tree_.feature
#zip(TT.columns[et.tree_.feature], et.tree_.threshold, et.tree_.children_left, et.tree_.children_right)


#print getmembers( et.tree_)

'''
kn=KNeighborsClassifier(n_neighbors=3, p=1, metric='minkowski')
kn.fit(X_train,y_train)

print(kn.score(X_test,y_test))

bb= BernoulliNB(alpha=0.8)
bb.fit(X_train,y_train)

print(bb.score(X_test,y_test))


gn=GaussianNB()
gn.fit(X_train,y_train)

print(gn.score(X_test,y_test))

mlp = MLPClassifier(activation='relu',solver='sgd',learning_rate='adaptive', learning_rate_init=0.001, max_iter=2000, hidden_layer_sizes=(50,100,100), random_state=None)
mlp.fit(X_train,y_train)

print(mlp.score(X_test,y_test))
'''
#sc=SVC(C=10, random_state=0,gamma = 0.001, probability=True)
#sc.fit(X_train,y_train)

#print(sc.score(X_test,y_test))

#test=np.loadtxt(open("input.csv","rb"),delimiter=",",skiprows=0)
#predicted=et.predict(test)
#np.savetxt('output.csv',predicted,delimiter=',')

#print et.score(X_test,y_test)
