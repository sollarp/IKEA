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
        self.get_items(items_all)

    def get_items(self, item_all):
        self.pass_over = item_all
        item_name = []
        valid_until = [] 
        price = []
        item_name = item_all[1::4] # All items names   
        valid_until = item_all[0::4] # Price valid until
        price = item_all[3::4] # Items price
        k = 0
        item_all_s = []
        for i in range(len(item_name)):
            a = valid_until[k]
            b = item_name[k]
            c = price[k]
            k += 1
            item_all_s.append(a)
            item_all_s.append(b)
            item_all_s.append(c)
        self.item_all_s = item_all_s
        

    def data_container(self):
        self.list_elements()
        pass_over = self.item_all_s
        #item_name = self.item_name
        #valid_until = self.valid_until
        #price = self.price
        #desc = ['1']
        #modi = ['8']
        return pass_over


#run = OffersSite()
#run.list_elements()

