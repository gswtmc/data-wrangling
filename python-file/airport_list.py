"""
Complete the 'extract_airports()' function so that it returns a list of airport
codes, excluding any combinations like "All".

"""

from bs4 import BeautifulSoup
html_page = "options.html"


def extract_airports(page):
    data = []
    with open(page, "r") as html:
        soup = BeautifulSoup(html,'lxml'
        airports = soup.find(id = 'AirportList')
        for airport in airports.find_all(['option'])
    
    
    
    
