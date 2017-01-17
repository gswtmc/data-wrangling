# Extract data from xml on authors of an article
# and add it to a list, one item for an author.
# The tags for first name, surname and email should map directly
# to the dictionary keys, but you have to extract the attributes from the "insr" tag
# and add them to the list for the dictionary key "insr"
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
                "email": None,
                "insr": []
        }

        # YOUR CODE HERE
        data["fnm"] = author.find("./fnm").text
        data["snm"] = author.find("./snm").text
        data["email"] = author.find("./email").text
        
        for i in author.findall("./insr"):
            data["insr"].append(i.attrib["iid"])
        
        authors.append(data)

    return authors
    
root = get_root(article_file)
get_authors(root)
