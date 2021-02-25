import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


dt = pd.read_excel('ESheet.xls')
dr = pd.DataFrame(data=dt).T ## organize data 
#print(dt)
#print(dt['Item_name'])
print(dr)
print(dt.head())
#print(dt.shape)
#print(dt.head(4))
#print(dt.tail)
