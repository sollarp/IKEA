import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


dt = pd.read_excel('ESheet.xls')
dr = pd.DataFrame(data=dt).T ## organize data 
dt.dropna(inplace = True)
sub ='Test'
start = 0
dt["Indexes"]= dt["Item_name"].str.find(sub, start) 
f = dt[dt['Desc'].str.contains("Waste")][['Desc']]
print(f.T)

#print(dt)
#print(dt['Item_name'])
#print(dr)
#print(dt)
#print(dt.head())
#print(dt.shape)
#print(dt.head(4))
#print(dt.tail)
