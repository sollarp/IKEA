from bs4 import BeautifulSoup
import requests


class OffersSite():

    def open_url(self):
        url = "https://www.ikea.com/gb/en/offers/limited-time-offers/?filters=f-online-sellable%3Atrue&page=10"
        req = requests.get(url)
        self.soup = BeautifulSoup(req.text, "html.parser")
    
    def list_elements(self):
        self.open_url()
        n = "range-revamp-header-section__description-text"
        p = "range-revamp-price__integer"
        v = "range-revamp-product-highlight range-revamp-product-highlight__time-restricted-offer"
        self.find_elements(n, p, v)

    def find_elements(self, *args):
        get_soup = self.soup
        items = get_soup.find_all("span", {"class": args})
        self.search_items(get_items=items)

    def search_items(self, get_items):
        items_all=[]

        for i in get_items:    

            items_all.append(i.text)
        #print(items_all)
        self.get_items(items_all)

    def get_items(self, item_all):
        item_name = []
        valid_until = [] 
        price = []

        item_name = item_all[1::4] # All items names
        valid_until = item_all[0::4] # Price valid until
        price = item_all[3::4] # Items price

run = OffersSite()
run.list_elements()

