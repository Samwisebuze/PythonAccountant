#########
# Python Accounatn Header 
# Desc: Contains Any functions or shortcut snippets used to sumplify main
# Created By: Samuel Buzas & Elizabeth Sheetz
#########
import datetime
from openpyxl import Workbook
from openpyxl.compat import range
from openpyxl.utils import get_column_letter

#Constant
wb = Workbook()

# Create Workbook
def create_workbook(filename = "MyFirstBudget", sheet_name = "SimpleBudget"):
	dest_filename = filename + '.xlsx'
	wb.active.title = sheet_name
	wb.active['A1'] = 'Date'
	wb.active.column_dimensions['A'].width = 10
	wb.active['B1'] = 'Category'
	wb.active.column_dimensions['B'].width = 10
	wb.active['C1'] = 'Amount'
	wb.active['D1'] = 'Check Number'
	wb.active['E1'] = 'Description'
	wb.active.column_dimensions['E'].width = 30
	wb.geuss_types = True
	wb.save(filename = dest_filename)

# Create WorkSheet
def create_worksheet(sheet_name = "Trackin Sheet", filename = "MyFirstBudget"):
	dest_filename = filename + '.xlsx'
	wb.create_sheet(sheet_name)
	wb.save(filename = dest_filename)

# Create Blank Graph
def create_table(filename = "MyFirstBudget", sheet_name = "SimpleBudget"):
	dest_filename = filename + '.xlsx'
	wb.active.title = sheet_name
	wb.save(filename = dest_filename)



# Edit Entry


