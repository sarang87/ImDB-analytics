# -*- coding: utf-8 -*-
"""
Created on Thu Dec 08 17:08:33 2016

@author: jo_sa
"""


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import ensemble
from sklearn import datasets
from sklearn.utils import shuffle
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

# read in the test and training data files
data_df = pd.read_csv("output_afterImputation_country_deleted_budget_etc.csv", header = 0)


# create X and y for test and train split
X = data_df.ix[:, 1:].as_matrix()
y = data_df.ix[:, :1].as_matrix()


#separate the training dataframe into the first column and the rest of the columns for training on the gross values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

parameters = {'n_estimators':[1000,1500, 2000,2500,3000], 'max_depth':[2, 4,6,8],'min_samples_split': [2,4],'learning_rate': [0.01]}
#
#params = {'n_estimators': 2000, 'max_depth': 6, 'min_samples_split': 2,
#          'learning_rate': 0.01, 'loss': 'ls'}
         
clf = ensemble.GradientBoostingRegressor()
clf2 = GridSearchCV(clf, parameters, scoring='mean_squared_error') 
clf2.fit(X_train, y_train)
results = clf2.cv_results_
#np.savetxt('grid_results.csv',results)


#mse = mean_squared_error(y_test, clf.predict(X_test))
#print("MSE: %.4f" % mse)
#predicted = clf.predict(X_test)


#feature_importance = clf.feature_importances_
##print feature_importance.max()
##feature_importance = 100.0 * (feature_importance / feature_importance.max())
#sorted_idx = np.argsort(feature_importance)
#print feature_importance



