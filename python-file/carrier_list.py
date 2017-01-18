"""
Get a list of all airlines from the given data. 
Exclude all of the combination values like "All U.S. Carriers"
from the data that you return. You should return a list of codes for the
carriers.
"""
from bs4 import BeautifulSoup
html_page = "options.html"
