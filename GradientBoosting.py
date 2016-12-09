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

# read in the test and training data files
train_df = pd.read_csv("train_for_imdbScore.csv", header = 0)
test_df = pd.read_csv("test_for_imdbScore.csv", header = 0)

#separate the training dataframe into the first column and the rest of the columns for training on the gross values
X_train =  train_df.ix[:, 1:].as_matrix()
y_train =  train_df.ix[:, :1].as_matrix()

X_test =  test_df.ix[:, 1:].as_matrix()
y_test =  test_df.ix[:, :1].as_matrix()

print X_train.shape,y_train.shape
print type(X_train),type(y_train)

params = {'n_estimators': 500, 'max_depth': 4, 'min_samples_split': 2,
          'learning_rate': 0.01, 'loss': 'ls'}
clf = ensemble.GradientBoostingRegressor(**params)

clf.fit(X_train, y_train)
mse = mean_squared_error(y_test, clf.predict(X_test))
print("MSE: %.4f" % mse)
predicted = clf.predict(X_test)
np.savetxt("results_gb1.csv,",predicted)