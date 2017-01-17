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

def get_from_file(kind, period):
    filename = "popular-{0}-{1}.json".format(kind, period)
    with open(filename, "r") as f:
        return json.loads(f.read())


def article_overview(kind, period):
    data = get_from_file(kind, period)
    titles = []
    urls =[]
    
    for line in data:
        section = line['section']
        titles = line['title']
        urls = []
        
        for media in line['media']:
            for metadata in media['media-metadata']:
                if metadata['format'] == 'Standard Thumbnail':
                    urls.append(metadata['url'])

    return (titles, urls)

            
            
