# -*- coding: utf-8 -*-
"""
Created on Thu Dec 08 18:46:30 2016

@author: satyajit
"""

movie = pandas.read_csv('pruned_movie_metadata.csv')


def set_genre_column_bits ():
    column_headers_list =[]
    for idx, x in enumerate(movie[Country]):
        column_to_insert = genre_dict.get(x)
        column_headers_list.append(column_to_insert)
    
    for row in range(len(column_headers_list)):
        if (column_headers_list[row] is not None):        
            column_name = column_headers_list[row]
            movie.set_value(row,column_name, 1)
