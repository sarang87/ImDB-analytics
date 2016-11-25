# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 14:28:29 2016

@author: satyajit
"""

import pandas as pd
import numpy as numpy
import csv as csv
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import Imputer


movie = pd.read_csv('all_num_IMDB_before_imputation.csv')



#i = Imputer (strategy = 'median')
#i.fit(movie)
#imputed_sample = i.transform(movie)
#
#numpy.savetxt('afterImputation.csv', imputed_sample, delimiter = ",")


train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')
actualGross_df = pd.read_csv('grossactuals.csv')

train_data = train_df.values
test_data = test_df.values

print 'Training...'
forest = RandomForestClassifier(n_estimators=100)

#forest = forest.fit(train_data[0::,1::],train_data[0::,0])
ids = actualGross_df['id'].values
gross = actualGross_df['gross'].values
print len(gross)
print len(test_data)

#print 'Predicting...'
#output = forest.predict(test_data).astype(float)
#
#
#predictions_file = open("forestresults1.csv", "wb")
#open_file_object = csv.writer(predictions_file)
#open_file_object.writerow(["Id","gross"])
#open_file_object.writerows(zip(ids, output))
#predictions_file.close()
#print 'Done.'
#
#forest.score(test_data, gross)