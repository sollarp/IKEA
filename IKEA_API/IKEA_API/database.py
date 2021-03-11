import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import openpyxl
from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo



def search_in(input):
    print(input.lower())
    d_frame = pd.read_excel('ESheet_second.xlsx')
    find = d_frame[d_frame['Item_name'].str.contains(input, 
                   case=False, regex=True)][['Item_name', 'ValidUntil', 'Price']]
    con_list = find.values.tolist() # convert dataobject to list
    return con_list[0]

