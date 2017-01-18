"""
Create 'process_file()' to extract the flight data from that table as a list of
dictionaries, each dictionary containing relevant data from the file and table
row. This is an example of the data structure you should return:

data = [{"courier": "FL",
         "airport": "ATL",
         "year": 2012,
         "month": 12,
         "flights": {"domestic": 100,
                     "international": 100}
        },
         {"courier": "..."}
]

Note - year, month, and the flight data should be integers.
You should skip the rows that contain the TOTAL data for a year.
"""
from bs4 import BeautifulSoup
import os

datadir = "data"

def process_all(datadir):
    files = os.listdir(datadir)
    return files


def process_file(f):
    """
    This function extracts data from the file given as the function argument in
    a list of dictionaries. This is example of the data structure you should
    return:

    data = [{"courier": "FL",
             "airport": "ATL",
             "year": 2012,
             "month": 12,
             "flights": {"domestic": 100,
                         "international": 100}
            },
            {"courier": "..."}
    ]


    Note - year, month, and the flight data should be integers.
    You should skip the rows that contain the TOTAL data for a year.
    """
    data = []
    info = {}
    info["courier"], info["airport"] = f[:6].split("-")
    # Note: create a new dictionary for each entry in the output data list.
    # If you use the info dictionary defined here each element in the list 
    # will be a reference to the same info dictionary.
    with open("{}/{}".format(datadir, f), "r") as html:

        soup = BeautifulSoup(html,"lxml")
        # Find table
        table = soup.find("table",{"class":"dataTDRight"})
        for tr in table.find_all("tr",{"class":"dataTDRight"}):
            td = tr.find_all('td')
            year = td[0].string
            month = td[1].string
            dom = td[2].string.replace(',','')
            intl = td[3].string.replace(',','')
            
            if month == 'TOTAL':
                continue
            else:
                info = {
                    "courier": info["courier"],
                    "airport": info["airport"],
                    "year": int(year),
                    "month": int(month),
                    "flights": {"domestic": int(dom),
                    "international": int(intl)}
                    }
                data.append(info)
        
    return data
