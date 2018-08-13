#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 13:33:38 2018

@author: zhoulinn
"""

#### imports ####
import import_csv 
import os 




#### Main ####
if __name__ == '__main__':
    con = sqlite3.connect("atp_match_year.db", detect_types = sqlite3.PARSE_COLNAMES)  # making connection to sqlite
    cur = con.cursor()  # cursor    
    
    # conver all csv files from one foler to tables in sqlite, table names same as file names
#    folder_path = '~/Projects/tennis_analytics/data/raw/atp_matches'
    folder_path = '/Users/zhoulinn/Projects/tennis_analytics/data/raw/atp_matches/'
    for file in os.listdir(folder_path):
        if file.endswith(".csv"): 
            table = file[:-4]
            file_path = str(folder_path + file)
            import_csv.csv2sql(con, file_path, table) # load csv to sql table and show the first rows, run only once 
    
    # show all table names added to the database 
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cur.fetchall())
    
    con.commit() # save changes to the database!!
    
    con.close()  # close the connection