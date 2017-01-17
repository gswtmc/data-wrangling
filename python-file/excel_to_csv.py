'''
Find the time and value of max load for each of the regions
COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
and write the result out in a csv file, using pipe character | as the delimiter.
'''
import xlrd
import os
import csv

datafile = "2013_ERCOT_Hourly_Load_Data.xls"
outfile = "2013_Max_Loads.csv"

def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    data = {}
    
    for n in range(1, sheet.ncols - 1):
        cv = sheet.col_values(n, start_rowx = 1, end_rowx = None)
        
        station = sheet.cell_value(0,n)
        
        maxval = max(cv)
        maxpos = sheet.index(maxval) + 1
        xlmaxtime = sheet.cell_value(maxpos, 0)
        maxtime = xlrd.xldate_as_tuple(xlmaxtime, 0)
        
        data[station] = {'maxval': maxval, 'maxtime': maxtime}
    
    return data

def save_file(data, filename):
    with open(filename,'w') as f:
        w= csv.writer(f, delimiter ='|')
        w.writerow(['Station', 'Year', 'Month', 'Day', 'Hour', 'Max Load'])
        
        for s in data:
            year, month, day, hour, mins, sec = data[s]['maxtime']
            w.writerow([s, year, month, day, hour, data[s]['maxval']])
    

    
def test():
    data = parse_file(datafile)
    save_file(data, outfile)

    number_of_rows = 0
    stations = []

    ans = {'FAR_WEST': {'Max Load': '2281.2722140000024',
                        'Year': '2013',
                        'Month': '6',
                        'Day': '26',
                        'Hour': '17'}}
    correct_stations = ['COAST', 'EAST', 'FAR_WEST', 'NORTH',
                        'NORTH_C', 'SOUTHERN', 'SOUTH_C', 'WEST']
    fields = ['Year', 'Month', 'Day', 'Hour', 'Max Load']


if __name__ == "__main__":
    test()

