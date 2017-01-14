"""
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples
"""


import xlrd
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"

def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    cv = sheet.col_values(1, start_rowx = 1, end_rowx = None)
    
    maxval = max(cv)
    minval = min(cv)
    
    maxpos = cv.index(maxval) + 1
    minpos = cv.index(minval) + 1
    
    xlmaxtime = sheet.cell_value(maxpos, 0)
    xlmintime = sheet.cell_value(minpos, 0)
    maxtime = xlrd.xldate_as_tuple(xlmaxtime, 0)
    mintime = xlrd.xldate_as_tuple(xlmintime, 0)
    
   
    data = {
            'maxtime': maxtime,
            'maxvalue': maxval,
            'mintime': mintime,
            'minvalue': minval,
            'avgcoast': sum(cv)/float(len(cv))
    }
    return data
    
data = parse_file(datafile)
import pprint
pprint.pprint(data)
