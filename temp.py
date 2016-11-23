# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv as csv
import numpy as np
import pandas as pandas


#print movie
movie = pandas.read_csv('../../csv/pruned_movie_metadata.csv')

# calculate the unique genres across all colums and store them ina dictionary
pd1 = movie.g1.unique()
pd2 = movie.g2.unique()
all_genres = (set(pd1).union(set(pd2)))
cleanedGenreList = [x for x in all_genres if str(x) != 'nan']
genre_dict= {cleanedGenreList[x]:'n'+str(x+1) for x in range(len(cleanedGenreList))}
print genre_dict           

# select the columns in the dataframe movie to change the value from 0 to 1. For example if the genre in g1 is action then lookup the column name in the dictionary and change the value in the dataframe to 1
def set_genre_column_bits (str):
    column_headers_list =[]
    for idx, x in enumerate(movie[str]):
        column_to_insert = genre_dict.get(x)
        column_headers_list.append(column_to_insert)
    
    for row in range(len(column_headers_list)):
        if (column_headers_list[row] is not None):        
            column_name = column_headers_list[row]
            movie.set_value(row,column_name, 1)
    print "success"


set_genre_column_bits(str = 'g1')
set_genre_column_bits(str = 'g2')
set_genre_column_bits(str = 'g3')
set_genre_column_bits(str = 'g4')
set_genre_column_bits(str = 'g5')
set_genre_column_bits(str = 'g6')
set_genre_column_bits(str = 'g7')
set_genre_column_bits(str = 'g8')


print movie ['n18']







 

pd3 = (movie.language.unique())
cleanedLanguageList = [x for x in pd3 if str(x) != 'nan']
language_dict= {cleanedLanguageList[x]:x+1 for x in range(len(cleanedLanguageList))}
#print language_dict

pd4 = (movie.country.unique())
cleanedCountryList = [x for x in pd4 if str(x) != 'nan']
country_dict= {cleanedCountryList[x]:x+1 for x in range(len(cleanedCountryList))}


# for each value in tthe column country
# find the corresponding value in the dictionary
country_value =[]
for idx, x in enumerate(movie.country):
    country_value.insert(idx,country_dict.get(x))
   
# replace the country with the corresponding value
for idx, x in enumerate(country_value):
    movie.set_value(idx,'country', country_value[idx])

language_value =[]
for idx, x in enumerate(movie.language):
    language_value.insert(idx,language_dict.get(x))
   
# replace the country with the corresponding value
for idx, x in enumerate(language_value):
    movie.set_value(idx,'language', language_value[idx])
    

    





    
