"""
Get a list of all airlines from the given data. 
Exclude all of the combination values like "All U.S. Carriers"
from the data that you return. You should return a list of codes for the
carriers.
"""
from bs4 import BeautifulSoup
html_page = "options.html"

def extract_carriers(page):
    data = []
    
    with open(page, "r") as html:
        soup = BeautifulSoup(html, "lxml")
        airlines = soup.find(id = "CarrierList")
        
        for airline in airlines.find_all("option"):
            if len(airline['value'] == 2:
                   data.append(airline['value'])
                   
    return data
                   
                   
extract_carriers(html_page)
        
      
