from bs4 import BeautifulSoup

html_page = "page_source.html"

def options(soup,id):
    option_values = []
    carrier_list= soup.find(id=id)
    for option in carrier_list.find_all('option'):
        option_values.append(option['value'])
    return option_values

def print_list(label,codes):
    print "\n%s:" %label
    for c in codes:
        print c


def main():
    soup = BeautifulSoup(open(html_page))
    
    codes = options(soup, 'CarrierList')
    print_list("Carrier", codes)
    
    codes = options(soup, 'AirportList')
    print_list("Airport", codes)

main()
