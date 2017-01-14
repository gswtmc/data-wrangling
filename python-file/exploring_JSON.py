import json
import requests


BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"

# query parameters are given to the requests.get function as a dictionary; this
# variable contains some starter parameters.
query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}


def query_site(url, params, uid="", fmt="json"):
    # This is the main function for making queries to the musicbrainz API.
    # A json document should be returned by the query.
    params["fmt"] = fmt
    r = requests.get(url + uid, params=params)
    print "requesting", r.url

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()
        


def query_by_name(url, params, name):
    # This adds an artist name to the query parameters before making
    # an API call to the function above.
    params["query"] = "artist:" + name
    return query_site(url, params)


def pretty_print(data, indent=4):
    # After we get our output, we can format it to be more readable
    # by using this function.
    if type(data) == dict:
        print json.dumps(data, indent=indent, sort_keys=True)
    else:
        print data
        
        
# How many bands name "FIRST AID KIT"?
def num_of_bands(name):
    results = query_by_name(ARTIST_URL, query_type["simple"], '\"' + name + '\"')
    print "\n The number of bands with the name " + name + " are: " + str(len(results["artists"]))
    
num_of_bands('FIRST AID KIT')
 

# What is the begin_area name for "Queen"?
def name_begin_area(name):
    results = query_by_name(ARTIST_URL, query_type["simple"], '\"' + name + '\"')
    artists = results["artists"]
    for i , entry in enumerate(artists):
        if entry["name"] == name:
            if entry.get('begin-area'):
                print "\n The begin-area name for " + name + " is: " + entry['begin-area']['name']
                
name_begin_area('Queen')


# What is Spanish Alias for "Beatles"?
def spanish_alias(name):
    results = query_by_name(ARTIST_URL, query_type["simple"], '\"' + name + '\"')
    artists = results["artists"]
    for i, entry in enumerate(artists):
        if entry['name'] == name:
            if entry.get('aliases'):
                for item in entry['aliases']:
                    if item.get('name'):
                        print item['name']
                        
spanish_alias('Beatles')


# What is disambiguation for "Nirvana"?
def disambiguation(name):
    results = query_by_name(ARTIST_URL, query_type["simple"], '\"' + name + '\"')
    artists = results["artists"]
    for i, entry in enumerate(artists):
        if entry['name'] == name:
            if entry.get('disambiguation'):
                print entry['disambiguation']
    
disambiguation('Nirvana')


# When was "One Direction" formed?
def formed_year(name):
    results = query_by_name(ARTIST_URL, query_type["simple"], '\"' + name + '\"')
    artists = results["artists"]
    for i,entry  in enumerate(artists):
        if entry['name'] == name:
            if entry.get('life-span'):
                print entry['life-span']
    
formed_year('One Direction')
