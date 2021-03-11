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
        self.search_items(item=items)

    def search_items(self, item):
        items_con=[]
        for i in item:    
            items_con.append(i.text)
        self.get_items(items_con)

    def get_items(self, items_con):
        self.pass_over = items_con
        item_name = []
        valid_until = [] 
        price = []
        item_name = items_con[1::4] # All items names   
        valid_until = items_con[0::4] # Price valid until
        price = items_con[3::4] # Items price
        k = 0
        item_all = []
        for i in range(len(item_name)):
            a = valid_until[k]
            b = item_name[k]
            c = price[k]
            k += 1
            item_all.append(a)
            item_all.append(b)
            item_all.append(c)
        self.pass_items = item_all
        

    def data_container(self):
        self.list_elements()
        pass_over = self.pass_items
        return pass_over

run = OffersSite()
run.list_elements()
print(run.data_container())