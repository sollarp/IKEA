import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from web_sitesec import OffersSite


dt = pd.read_excel('ESheet.xls')
xl = pd.ExcelFile('ESheet.xls')
dr = pd.DataFrame(data=dt).T ## organize data 
dt.dropna(inplace = True)
sub ='Test'
start = 0
dt["Indexes"]= dt["Item_name"].str.find(sub, start) 
f = dt[dt['Desc'].str.contains("Waste")][['Desc']]
lis = f.values.tolist() # convert dataobject to list
print(lis[0][0])

#print(dt)
#print(dt['Item_name'])
#print(dr)
#print(dt)
#print(dt.head())
#print(dt.shape)
#print(dt.head(4))
#print(dt.tail)
