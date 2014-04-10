import pandas as pd
from sklearn.externals import joblib
from sklearn import metrics
from sklearn import cross_validation
import pylab as pl
from timeit import Timer, timeit, repeat
from sklearn.ensemble import RandomForestClassifier

X_file = "X.csv"
Y_file = "Y.csv"
X = pd.read_csv(X_file)
Y = pd.read_csv(Y_file,header=None)
Y = Y[1]

ngroup = 5
cpc_list = []
for i in xrange(1,ngroup):
    cpc_list.append(Y.order().iloc[Y.shape[0]/ngroup*i])
cpc_list = list(set(cpc_list))
# print cpc_list.sort(reverse=True)
# print cpc_list

low_lim = None
high_lim = None
counter = 0
Y_mark = Y.copy()
for lim in cpc_list:
    counter += 1
    low_lim = lim
    print counter, lim
    if high_lim == None:
        Y_mark[Y_mark > low_lim] = counter
    else:
        Y_mark[(Y_mark <= high_lim) & (Y_mark > low_lim)] = counter
    high_lim = low_lim
counter += 1
Y_mark[Y_mark <= high_lim] = counter

X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X, Y_mark, test_size = 0.1, random_state = 111)


#     n_features = len(X.columns)
    
    #for m in [0.1*n_features, 0.25*n_features, 0.5*n_features, 0.75*n_features, n_features, log(n_features, 2), sqrt(n_features)]
    #for n in [11, 12, 13, 10, 50,100,1000,2000]:
    # print Y_train
#     print 'max_features:', 0.5*n_features
#     print 'n_estimators:', '500'
def test():
    classif_rf = RandomForestClassifier(n_estimators = 2, n_jobs = -1, oob_score=True, max_features=23)
    classif_rf.fit(X_train, Y_train)

print timeit(test)
	    # print classif_rf.predict(X_train)
	    # print 'logistics regression before tune'

	# print classif_rf.score(X_test, Y_test)
# print 'oob_score:', classif_rf.oob_score_
	# joblib.dump(classif_rf, 'rf_1_23.pkl')
# print 'train:', classif_rf.score(X_train, Y_train)
# print 'test:', classif_rf.score(X_test, Y_test)

# if __name__ == '__main__':	
# 	print(timeit("tune()", setup="from __main__ import test"))