import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import openpyxl
from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo
from web_parsing import OffersSite

def collect_data():
    offerssite = OffersSite()
    data = offerssite.data_container() ## return data from web_parsing with targeted elements
    list = data
    cont = []  
    start = 0
    end = 3
    lenght = len(list)
    ##Loop takes 3 items out of the list and pass it into a container and append to excel columns.
    for i in range(int(lenght/3)):
        lis = list[start:end]
        end += 3
        start += 3
        cont.append(lis)
    ## Create 3 dataframes      
    df1 = pd.DataFrame(cont,columns=['ValidUntil', 'Item_name', 'Price'])
    ## Insert items from loop and create excel file or overwrite. 
    with pd.ExcelWriter("ESheet_second.xlsx", engine='openpyxl', mode='w') as writer: 
        df1.to_excel(writer, sheet_name='Sheet1')

collect_data()
# Data can be assigned directly to cells
#ws['A5'] = 42

#with pd.ExcelWriter(path, engine='openpyxl') as writer:
#    writer.book = openpyxl.load_workbook(path)
#    dr.to_excel(writer, sheet_name='Sheet1')
                                   
#
#df = pd.DataFrame(data={'d':[2], 'e':['co'], 'f':[1.5]})              
#
#with pd.ExcelWriter("ESheet_second.xlsx", engine='openpyxl', mode='r+') as writer: 
#    df.to_excel(writer)

#dr = pd.DataFrame(data=dt).T ## organize data
#dr_new = pd.DataFrame(data=dt_sec).T

#sub ='Test'
#start = 0
#dt["Indexes"]= dt["Item_name"].str.find(sub, start) 
#f = dt[dt['Desc'].str.contains("Waste")][['Desc']]
#lis = f.values.tolist() # convert dataobject to list

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