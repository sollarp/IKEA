from requests_html import HTMLSession



class OffersSite():

    def open_url(self):
        url = "https://www.ikea.com/gb/en/offers/limited-time-offers/?filters=f-online-sellable%3Atrue&page=10"
        s = HTMLSession()
        req = s.get(url)
        self.req = req
        req.html.render(sleep=1)

    ## Find selected element from website
    def list_elements(self):
        self.open_url()
        n = "span.range-revamp-header-section__description-text"
        p = "span.range-revamp-price__integer"
        v = "div.range-revamp-compact-price-package__product-highlights"
        self.collect_elements(n, p, v)

    ## Asign elements to objects
    def collect_elements(self, n, p, v):
        get_req = self.req
        n = get_req.html.find(n)
        p = get_req.html.find(p)
        v = get_req.html.find(v)
        self.search_items(n, p, v)

    ## Passing elements in 3 containers using loop.
    def search_items(self, n, p, v):
        item_n = []
        item_p = []
        item_v = []
        for i in range(len(n)):
            name = n[i].text
            price =p[i].text
            valid =v[i].text
            item_p.append(price)
            item_n.append(name)
            item_v.append(valid)
        self.get_items(item_v, item_n, item_p)

    ## Merge 3 containers to able to insert in excelsheet
    def get_items(self, a, b, c):
        item_all = []
        for i in range(len(a)):
            item_all.append(a[i])
            item_all.append(b[i])
            item_all.append(c[i])
        self.pass_items = item_all
        
    ## Main program to call
    def data_container(self):
        self.list_elements()
        pass_over = self.pass_items
        return pass_over


######################################################################################
# This code using BeautifulSoup how ever the website has dynamic contents unable to
# collect all require data and form different container blockes. 
#######################################################################################

#from bs4 import BeautifulSoup
#import requests

#class OffersSite():
#
#    def open_url(self):
#        url = "https://www.ikea.com/gb/en/offers/limited-time-offers/?filters=f-online-sellable%3Atrue&page=10"
#        req = requests.get(url)
#        self.req = BeautifulSoup(req.text, "html.parser")
#    
#    def list_elements(self):
#        self.open_url()
#        n = "range-revamp-header-section__description-text"
#        p = "range-revamp-price__integer"
#        v = "range-revamp-product-highlight range-revamp-product-highlight__time-restricted-offer"
#        self.collect_elements(n, p, v)
#
#    def collect_elements(self, *args):
#        get_req = self.req
#        items = get_req.find_all("span", {"class": args})
#        self.search_items(item=items)
#
#    def search_items(self, item):
#        items_con=[]
#        for i in item:    
#            items_con.append(i.text)
#        self.get_items(items_con)
#
#    def get_items(self, items_con):
#        self.pass_over = items_con
#        item_name = []
#        valid_until = [] 
#        price = []
#        item_name = items_con[1::4] # All items names   
#        valid_until = items_con[0::4] # Price valid until
#        price = items_con[3::4] # Items price
#        k = 0
#        item_all = []
#        for i in range(len(item_name)):
#            a = valid_until[k]
#            b = item_name[k]
#            c = price[k]
#            k += 1
#            item_all.append(a)
#            item_all.append(b)
#            item_all.append(c)
#        self.pass_items = item_all
#        
#
#    def data_container(self):
#        self.list_elements()
#        pass_over = self.pass_items
#        return pass_over