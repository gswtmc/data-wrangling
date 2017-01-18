"""
Use the csv module to extract data from the provided file.
The data comes from NREL (National Renewable Energy Laboratory) website. Each file
contains information from one meteorological station, in particular - about amount of
solar and wind energy for each hour of day.

Note that the first line of the datafile is neither data entry, nor header. It is a line
describing the data source. Extract the name of the station from it.
The data should be returned as a list of lists (not dictionaries).
"""


import csv
import os

DATAFILE = "745090.csv"

def parse_file(datafile):
    name = ""
    data = []
    with open(datafile, 'rb') as f:
        value = f.readline().split(',')
        csvfile = csv.reader(f)
        name = value[1].replace('"','')
        csvfile.next()
        for row in csvfile:
            data.append(row)
    return (name, data)
    
    
parse_file(DATAFILE)
        
        
        
