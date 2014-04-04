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
		print idx, sum(Y_test ==  idx)
		print idx, sum(Y_train ==  idx)
	##--linear_regression
	# print Y_train
	classif_lr = OneVsRestClassifier(LogisticRegression(), n_jobs = -1)
	classif_lr.fit(X_train, Y_train)
	print classif_lr.predict(X_train)
	print 'logistics regression before tune'
	print classif_lr.score(X_test, Y_test)
	lr_conf_matrix = metrics.confusion_matrix(Y_test, classif_lr.predict(X_test))
	print lr_conf_matrix
	##--
	print '0 fine tune'
	classif_lr = OneVsRestClassifier(LogisticRegression(), n_jobs = -1)
	# classif_SVM_lr.fit(X_test, Y_test)
	parameters = {'estimator__penalty':['l1', 'l2'], 'estimator__C':np.logspace(-3., 3)}
	clf = grid_search.GridSearchCV(classif_lr, parameters, cv = 5)
	clf.fit(X_train, Y_train)
	print clf.best_estimator_
	print clf.best_score_
	print clf.best_params_
	lr_conf_matrix = metrics.confusion_matrix(Y_test, clf.predict(X_test))
	print lr_conf_matrix
	print clf.score(X_test, Y_test)
	joblib.dump(clf, 'lr_ft0.pkl')
	c_old = None
	counter = 0
	while c_old != clf.best_params_['estimator__C'] and counter < 10:
		c_old = clf.best_params_['estimator__C']
		clf = joblib.load('lr_ft%s.pkl'%counter)
		counter += 1
		print np.linspace(clf.best_params_['estimator__C']*.9, clf.best_params_['estimator__C']*1.1)
		parameters = {'estimator__penalty':[clf.best_params_['estimator__penalty']], \
			 'estimator__C':np.linspace(clf.best_params_['estimator__C']*.9, clf.best_params_['estimator__C']*1.1)}
		classif_lr = OneVsRestClassifier(LogisticRegression(), n_jobs = -1)
		clf = grid_search.GridSearchCV(classif_lr, parameters, cv = 5)
		clf.fit(X_train, Y_train)
		print clf.best_estimator_
		print clf.best_score_
		print clf.best_params_
		joblib.dump(clf, 'lr_ft%s.pkl'%counter)
		lr_conf_matrix = metrics.confusion_matrix(Y_test, clf.predict(X_test))
		print lr_conf_matrix
		print clf.score(X_test, Y_test)



