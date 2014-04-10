import pandas as pd
from sklearn import cross_validation
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn import grid_search
from sklearn.externals import joblib
import numpy as np
from math import sqrt, log

def find_group_boundary(Y,n_group=20):
	'''
	Find the group boundary, the number of samples in a group should be as close as possible.
	Input:
		Y: find the boundary in Y
		n_group: number of group suggested
	Output:
		boundary_list: list of boundary value, the number of boundary will not be greater than n_group
	'''
	boundary_list = []
	for idx in xrange(1,n_group):
		boundary_list.append(Y.order().iloc[Y.shape[0]/n_group*idx])
	return list(set(boundary_list))


def find_group(Y,boundary_list):
	'''
	Find the mark the input dataset based on the list of boundary.
	Input:
		Y: dataset to mark, numpy array
		boundary_list: list of boundary value
	Output:
		Y_mark: marked numpy array
	'''
	low_lim = None
	high_lim = None
	counter = 0
	Y_mark = Y.copy()
	boundary_list.sort(reverse=True)
	# print boundary_list
	for lim in boundary_list:
		counter += 1
		low_lim = lim
		if high_lim == None:
			Y_mark[Y_mark > low_lim] = counter
		else:
			Y_mark[(Y_mark <= high_lim) & (Y_mark > low_lim)] = counter
		high_lim = low_lim
	counter += 1
	Y_mark[Y_mark <= high_lim] = counter
	# print Y_mark
	return Y_mark


if __name__ == "__main__":
	##--read data from file
	X_file = "../../X.csv"
	Y_file = "../../Y.csv"
	X = pd.read_csv(X_file)
	Y = pd.read_csv(Y_file, header=None)
	Y = Y.drop(0, 1)
	Y = Y[1]
	##--mark data
	n_group = 5
	boundary_list = find_group_boundary(Y,n_group)
	# print boundary_list
	Y_mark = find_group(Y,boundary_list)
	##--split data
	X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X, Y_mark, test_size = 0.1, random_state = 111)
	for idx in xrange(1,len(boundary_list)+2):
		# print idx, sum(Y_test ==  idx)
		# print idx, sum(Y_train ==  idx)
		print idx, sum(Y_mark ==  idx)
	##--random forest
	##Tune two loops of max_features with sqrt, log2, 10%-100% of n features.
	##Tune n_estimators, 10, 50, 100, 500, 1000, 2000)
	##Use MR, EC2, Hadoop or Domino to run.

	# for m in [0.1*n_features, 0.25*n_features, 0.5*n_features, 0.75*n_features, n_features, log(n_features, 2), sqrt(n_features)]
	# 	for n in [10, 50, 100, 500, 1000, 2000]: #[11, 12, 13]:
	#   print Y_train
	# 		print 'max_features:', m
	# 		print 'n_estimators:', n
	# 		classif_rf = RandomForestClassifier(n_estimators = n, n_jobs = -1, oob_score=True, max_features=n_features)
	# 		classif_rf.fit(X_train, Y_train)
	#		print classif_rf.predict(X_train)
	# print 'logistics regression before tune'
		# print classif_rf.score(X_test, Y_test)
		# print 'oob_score:', classif_rf.oob_score_
		# joblib.dump(classif_rf, 'rf_m%s_n%s.pkl'%m, %n)
		# print 'train:', classif_rf.score(X_train, Y_train)
		# print 'test:', classif_rf.score(X_test, Y_test)
		# rf_conf_matrix = metrics.confusion_matrix(Y_test, classif_rf.predict(X_test))
		# print rf_conf_matrix
	##--
	print '0 fine tune'
	n_features = len(X.columns)
	classif_rf = RandomForestClassifier(n_estimators = n, n_jobs = -1, oob_score=True, max_features=n_features)
	# classif_rf.fit(X_train, Y_train)
	#[(100, 500, 1000, 2000), [sqrt, log2, 10%-100%]
	parameters = {'n_estimators':range(10, 50), 'confusion_matrix':range(0.5*n_features, sqrt(n_features))}
	clf = grid_search.GridSearchCV(classif_rf, parameters,cv=5)
	clf.fit(X_train, Y_train)
	print clf.best_estimator_
	print clf.best_score_
	print clf.best_params_
	# rf_conf_matrix = metrics.confusion_matrix(Y_test, clf.predict(X_test))
	# print rf_conf_matrix
	print clf.score(X_test, Y_test)
	joblib.dump(clf, 'rf_max_features%s_n_estimators%s.pkl'%n_estimators, %max_features)
	print("Detailed classification report:")
    print()
    y_true, y_pred = y_test, clf.predict(X_test)
    print(classification_report(y_true, y_pred))
    print()


	# n_old = None
	# counter = 0
	# while n_old != clf.best_params_['estimator__n_estimators'] and counter < 10:
	# 	n_old = clf.best_params_['estimator__n_estimators']
	# 	clf = joblib.load('rf_ft%s.pkl'%counter)
	# 	counter += 1
	# 	print range(clf.best_params_['estimator__n_estimators'] - 5 + counter / 2, clf.best_params_['estimator__n_estimators'] + 5 + counter / 2)
	# 	parameters = {'estimator__n_estimators':range(clf.best_params_['estimator__n_estimators'] - 5 + counter / 2, clf.best_params_['estimator__n_estimators'] + 5 + counter / 2)}
	# 	classif_rf = OneVsRestClassifier(RandomForestClassifier(n_jobs = -1), n_jobs = -1)
	# 	clf = grid_search.GridSearchCV(classif_rf, parameters, cv=5)
	# 	clf.fit(X_train, Y_train)
	# 	print clf.best_estimator_
	# 	print clf.best_score_
	# 	print clf.best_params_
	# 	joblib.dump(clf, 'rf_ft%s.pkl'%counter)
	# 	rf_conf_matrix = metrics.confusion_matrix(Y_test, clf.predict(X_test))
	# 	print rf_conf_matrix
	# 	print clf.score(X_test, Y_test)



