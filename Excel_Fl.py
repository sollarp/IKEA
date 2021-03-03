import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from web_sitesec import OffersSite
import openpyxl
from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo
from web_sitesec import OffersSite
#
offerssites = OffersSite()
data = offerssites.data_container()
#data1 = data[0]
#data2 = data[1]
#data3 = data[2]
list = data
  
# Using enumerate() 
var = []
s = 0
e = 4
g = len(list)
for var in range(int(g/4)):
    var = list[s:e]
    e += 4
    s += 4
   
    print(var)
   

#df = pd.DataFrame(data={'Itemname': [data1], 'Desc':[data2], 'Price':[data3], 'ValidUntil':[ ], 'Modified':[ ]})              
df1 = pd.DataFrame([data],
                   columns=['Itemname',	'Desc',	'Price', 'ValidUntil', 'Modified'])



with pd.ExcelWriter("ESheet_second.xlsx", engine='openpyxl', mode='w') as writer: 
    df1.to_excel(writer, sheet_name='Sheet1')


# Data can be assigned directly to cells
#ws['A5'] = 42


#
#
#path = 'ESheet_second.xlsx'
#dt = pd.read_excel('ESheet.xlsx')
#dr = pd.DataFrame(data=dt)
#
#with pd.ExcelWriter(path, engine='openpyxl') as writer:
#    writer.book = openpyxl.load_workbook(path)
#    dr.to_excel(writer, sheet_name='Sheet1')
                                   
#
#df = pd.DataFrame(data={'d':[2], 'e':['co'], 'f':[1.5]})              
#
#with pd.ExcelWriter("ESheet_second.xlsx", engine='openpyxl', mode='r+') as writer: 
#    df.to_excel(writer)
#
    

#
#dt = pd.read_excel('ESheet.xlsx')
#xl = pd.ExcelFile('ESheet.xlsx')

#dt_sec = pd.read_excel('ESheet_second.xlsx')




#dr = pd.DataFrame(data=dt).T ## organize data
#dr_new = pd.DataFrame(data=dt_sec).T

#dr_sec = pd.DataFrame(data=dt_sec).T

#dt.dropna(inplace = True)

#sub ='Test'
#start = 0
#dt["Indexes"]= dt["Item_name"].str.find(sub, start) 
#f = dt[dt['Desc'].str.contains("Waste")][['Desc']]
#lis = f.values.tolist() # convert dataobject to list



#print(lis[0][0]) # select one item from list

#print(dt)
#print(dt['Item_name'])
#print(dr)
#print(dt)
#print(dt.head())
#print(dt.shape)
#print(dt.head(4))
#print(dt.tail)



### This takes 2 excel sheets and merge together #############################
#    excel1 = 'ESheet.xlsx'                                                  #
#    excel2 = 'ESheet_sec.xlsx'                                              #
#
#    df1 = pd.read_excel(excel1)
#    df2 = pd.read_excel(excel2)
#
#    values1 = df1[['Itemname',	'Desc',	'Price', 'ValidUntil', 'Modified']]
#    values2 = df2[['Itemname',	'Desc',	'Price', 'ValidUntil', 'Modified']]
#
#    dataframes = [values1, values2]
#
#    join = pd.concat(dataframes)
#                                                                            #
#    join.to_excel("ESheet.xlsx")                                            #
##############################################################################