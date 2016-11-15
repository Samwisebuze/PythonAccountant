#########
# Python Accounatn Header 
# Desc: Contains Any functions or shortcut snippets used to sumplify main
# Created By: Samuel Buzas & Elizabeth Sheetz
#########
from openpyxl import Workbook
from openpyxl.compat import range
from openpyxl.utils import get_column_letter

# Creat Workbook
def CreateWB(filename = "MyFirstWorkBook", title = "Worksheet 1"):
	wb = Workbook()
	dest_filename = filename + '.xlsx'
	wb.save(filename = dest_filename)


