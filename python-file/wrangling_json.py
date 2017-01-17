"""
This exercise shows some important concepts that you should be aware aware of:
- using codecs module to write unicode files
- using authentication with web APIs
- using offset when accessing web APIs

Modify the article_overview() function to process the saved
file that represents the most popular articles (by view count) from the last
day, and return a tuple of variables containing the following data:
- labels: list of dictionaries, where the keys are the "section" values and
  values are the "title" values for each of the retrieved articles.
- urls: list of URLs for all 'media' entries with "format": "Standard Thumbnail"
"""
import json
import codecs
import requests

URL_MAIN = "http://api.nytimes.com/svc/"
URL_POPULAR = URL_MAIN + "mostpopular/v2/"
API_KEY = { "popular": "","article": ""}
            
            
