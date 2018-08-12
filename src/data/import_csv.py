#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 16:55:44 2018

@author: zhoulinn
"""

"""
import and visualize csv datasets with sqlite3
"""

#### imports ####
import sqlite3
import pandas as pd


#### functions ####
def csv2sql (con, path, table_name, show_table = False, rows = 5):
    """
    reads csv file, convert to sql table and show first rows by option
    - path: complete file path for csv file 
    - con: sql connection 
    - table_name: name of new sql table to store the csv file
    - show_table: print first rows of the table
    - row: number of rows to print if show_table
    """
    
    df_raw_data = pd.read_csv(path) # empty values replaced with nan
    print('...read file to dataframe')
    df_raw_data.to_sql(table_name, con, if_exists='replace', index=False)
    print('...added to sql table')
    
    if show_table:   # if print first rows of the table
        sql_command = str('SELECT * FROM ' + table_name +  ' LIMIT ' + str(rows))
        df_sql_output = pd.read_sql_query(sql_command, con)
        print(df_sql_output)    
    
    
    
#### Main ####     
if __name__ == '__main__':
    
    # query options
    count_tour_match = True     # count matches played at each tourney
    cuont_surface_tour = False  # count tourney by surface
    
    con = sqlite3.connect("TennisData.db", detect_types=sqlite3.PARSE_COLNAMES)  # making connection to sqlite
    cur = con.cursor()  # cursor    
    
    file_path = '~/Projects/tennis_analytics/data/raw/atp_matches_2017.csv'
    table = 'atp_2017'
    
    csv2sql(con, file_path, table) # load csv to sql table and show the first rows, run only once 
    
    
    if count_tour_match:   # count matches played at each tourney
        
        sql_command = """ 
        SELECT tourney_name, 
               count(*) AS matches_per_tourney
        FROM atp_2017
        GROUP BY tourney_name
        ORDER BY matches_per_tourney DESC
        """
        tour_match_count = pd.read_sql_query(sql_command, con) 
        print('Matches played at each tourney: \n',tour_match_count)
    
    
    if cuont_surface_tour:   # count tourney by surface
        
        sql_command = """   
        SELECT a.surface, 
               count(tourney_name) AS tourney_count
        FROM(
            SELECT tourney_name, 
                   surface, 
                   count(*) AS matches_tourney
            FROM atp_2017
            GROUP BY tourney_name
            ORDER BY matches_tourney DESC
        ) a
        GROUP BY surface
        """
        surface_tour_count = pd.read_sql_query(sql_command, con) 
        print('Tourney per surface: \n',surface_tour_count)
    
    
    con.commit() # save changes to the database!!
    
    con.close()  # close the connection