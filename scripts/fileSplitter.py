# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 18:27:35 2016
This script is used to split a data file into train and test data files. Please specify the parameters for how many records to split into in each of the files
@author: jo_sa
"""
import pandas as pd
import numpy as numpy
import csv as csv


fileName = raw_input("Please provide the name of the file to split into test and training data::")

file_df = pd.read_csv(fileName, header = None)
fileCountTrain = int(raw_input("Please provide the number of records for the training data file::"))
fileCountTest = int(raw_input("Please provide the number of records for the test data file::"))

train_df = pd.read_csv(fileName,nrows=fileCountTrain, header = 0)
test_df = pd.read_csv(fileName,skiprows=fileCountTrain, nrows=fileCountTest, header = 0)

train_df.to_csv('demo_train.csv')
test_df.to_csv('demo_test.csv')