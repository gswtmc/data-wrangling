# Extract data from xml on authors of an article
# and add it to a list, one item for an author.
# The tags for first name, surname and email should map directly
# to the dictionary keys
import xml.etree.ElementTree as ET

article_file = "exampleResearchArticle.xml"


def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()


def get_authors(root):
    authors = []
    for author in root.findall('./fm/bibl/aug/au'):
        data = {
                "fnm": None,
                "snm": None,
                "email": None
        }
        
        data['fnm'] = author.find('./fnm').text
        data['snm'] = author.find('./fnm').text
        data['email'] = author.find('./fnm').text

        authors.append(data)

    return authors

root = get_toor(article_file)
get_authors(root)
