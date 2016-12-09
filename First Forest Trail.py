# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 14:28:29 2016

@author: satyajit
"""

import pandas as pd
import numpy as numpy
import csv as csv
from sklearn.ensemble import RandomForestRegressor
from sklearn.cross_validation import cross_val_score




train_df = pd.read_csv('train.csv', header = 0)
test_df = pd.read_csv('test.csv', header = 0)
actualGross_df = pd.read_csv('grossactuals.csv')

train_data = train_df.values
test_data = test_df.values


print 'Training...'
forest = RandomForestRegressor(n_estimators=200, max_features = 15, min_samples_leaf = 5, oob_score = True)

#forest = forest.fit(train_data[0::,1::],train_data[0::,0])


#ids = actualGross_df['id'].values
#gross = actualGross_df['gross'].values



#########CROSS VALIDATION
scores = cross_val_score(forest,train_data[0::,1::], train_data[0::,0], cv = 10, scoring = 'mean_absolute_error')
print scores.mean(),scores.std()*2



#########
#oob_prediction_for_train = forest.oob_score_
#print(oob_prediction_for_train, train_data)

#print 'Predicting...'
#output = forest.predict(test_data).astype(float)

#predictions_file = open("forestresults_200_10_8.csv", "wb")
#open_file_object = csv.writer(predictions_file)
#open_file_object.writerow(["Id","gross"])
#open_file_object.writerows(zip(ids, output))
#predictions_file.close()
#print 'Done.'
#
#accuracy = forest.score(test_data, gross)
#print accuracy