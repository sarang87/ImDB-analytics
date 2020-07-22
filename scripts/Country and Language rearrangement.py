# -*- coding: utf-8 -*-
"""
Created on Thu Dec 08 18:46:30 2016

@author: satyajit
"""

import pandas as pd

movie = pd.read_csv('input_afterImputation_country.csv')





def set_country_column_bits ():
    column_headers_list =[]
    for idx, x in enumerate(movie['country']):
        column_to_insert = 'C' + str(x)
        column_headers_list.append(column_to_insert)
    print len(column_headers_list)

    
    for row in range(len(column_headers_list)):
        if (column_headers_list[row] is not None):        
            column_name = column_headers_list[row]
            movie.set_value(row,column_name, 1)
            
def set_language_column_bits ():
    column_headers_list =[]
    for idx, x in enumerate(movie['language']):
        column_to_insert = 'L' + str(x)
        column_headers_list.append(column_to_insert)
    print len(column_headers_list)

    
    for row in range(len(column_headers_list)):
        if (column_headers_list[row] is not None):        
            column_name = column_headers_list[row]
            movie.set_value(row,column_name, 1)

set_country_column_bits()
set_language_column_bits()

movie.to_csv('output_afterImputation_country.csv')
