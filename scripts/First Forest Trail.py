# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 14:28:29 2016

@author: satyajit
"""

import pandas as pd
import numpy as numpy
import csv as csv
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import Imputer


movie = pd.read_csv('afterImputation.csv', header = 0)




#i = Imputer (strategy = 'median')
#i.fit(movie)
#imputed_sample = i.transform(movie)
#
#numpy.savetxt('afterImputation.csv', imputed_sample, delimiter = ",")


train_df = movie[:3400]
test_df = movie[3400:]

#actualGross_df = pd.read_csv('grossactuals.csv')
#
train_data = train_df.values
test_data = test_df.values

print 'Training...'
forest = RandomForestRegressor(n_estimators=100)

forest = forest.fit(train_data[0::,1::],train_data[0::,0])

print 'Predicting...'
output = forest.predict(test_data).astype(float)
print output
#predictions_file = open("forestresults1.csv", "wb")
#open_file_object = csv.writer(predictions_file)
#open_file_object.writerow(["Id","gross"])
#open_file_object.writerows(zip(ids, output))
#predictions_file.close()
#print 'Done.'
#
#forest.score(test_data, gross)