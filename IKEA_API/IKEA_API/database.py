import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import openpyxl
from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo


def search_in(input):
    dt = pd.read_excel('ESheet_second.xlsx')
    #dt["Indexes"]= dt["Item_name"].str.find(sub, start) 
    f = dt[dt['Item_name'].str.contains(input)][['Item_name']]
    lis = f.values.tolist() # convert dataobject to list
    back = lis[0][0]
    return back
input = 'Waste'
#search_in(input)
print(search_in(input))