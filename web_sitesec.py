from bs4 import BeautifulSoup
import requests


class OffersSite():

    def open_url(self):
        url_call = "https://www.ikea.com/gb/en/offers/limited-time-offers/?filters=f-online-sellable%3Atrue&page=10"
        req = requests.get(url_call)
        soup = BeautifulSoup(req.text, "html.parser")
        self.find_elements(get_soup=soup)

    def find_elements(self, get_soup):
        n = "range-revamp-header-section__description-text"
        items = get_soup.find_all("span", {"class": n})
        self.search_items(get_items=items)

    # soup.find('input', {'name': 'auth_key'}).get('value')
    def search_items(self, get_items):
        items_all=[]

        for i in get_items:    

            items_all.append(i.text)

        print(items_all)

run = OffersSite()
run.open_url()

