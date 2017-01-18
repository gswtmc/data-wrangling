# Process the HTML using BeautifulSoup, extract the hidden
# form field values for "__EVENTVALIDATION" and "__VIEWSTATE" and set the appropriate
# values in the data dictionary.

from bs4 import BeautifulSoup
import requests
import json

html_page = "page_source.html"

def extract_data(page):
    data = {"eventvalidation": "",
            "viewstate": ""}
    with open(page, "r") as html:
        
        soup = BeautifulSoup(html, "lxml")
        
        ev = soup.find(id = "__EVENTVALIDATION")
        data["eventvalidation"] = ev["value"]
        
        vs = soup.find(id="__VIEWSTATE")
        data["viewstate"] = vs["value"]


    return data

extract_data(html_page)
