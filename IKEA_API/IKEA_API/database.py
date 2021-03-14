import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import openpyxl
from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo

## Search in excelsheet for requested Item_name come from Api request. 
def search_in(input):
    print(input.lower())
    d_frame = pd.read_excel('/home/peter/PycharmProjects/IKEA/IKEA_API/ESheet_second.xlsx')
    find = d_frame[d_frame['Item_name'].str.contains(input, 
                   case=False, regex=True)][['Item_name', 'ValidUntil', 'Price']] ## Case sensivity disabled.
    con_list = find.values.tolist() # convert dataobject to list
    return con_list[0]

