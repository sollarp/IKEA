import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import openpyxl
from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo


def search_in(input):
    dt = pd.read_excel('ESheet_second.xlsx')
    f = dt[dt['Item_name'].str.contains(input)][['Item_name', 'ValidUntil', 'Price']]
    lis = f.values.tolist() # convert dataobject to list
    return lis[0]
#input = 'Waste'
#search_in(input)
#print(search_in(input))