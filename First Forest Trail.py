# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 14:28:29 2016

@author: satyajit
"""

import pandas as pandas
import numpy as numpy
from sklearn.ensemble import RandomForestClassifier


movie = pandas.read_csv('all_num_IMDB_before_imputation.csv')


from sklearn.preprocessing import Imputer
i = Imputer (strategy = 'median')
i.fit(movie)
imputed_sample = i.transform(movie)

numpy.savetxt('afterImputation.csv', imputed_sample, delimiter = ",")
