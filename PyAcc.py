#########
# Python Accounatn Header 
# Desc: Contains Any functions or shortcut snippets used to sumplify main
# Created By: Samuel Buzas & Elizabeth Sheetz
#########
from openpyxl import Workbook
from openpyxl.compat import range
from openpyxl.utils import get_column_letter

#Constant
wb = Workbook()

# Create Workbook
def create_workbook(filename = "MyFirstBudget", sheet_name = "SimpleBudget"):
	dest_filename = filename + '.xlsx'
	wb.active.title = sheet_name
	wb.save(filename = dest_filename)

# Create WorkSheet
def create_worksheet(sheet_name = "Trackin Sheet", filename = "MyFirstBudget"):
	dest_filename = filename + '.xlsx'
	wb.create_sheet(sheet_name)
	wb.save(filename = dest_filename)

# Create Graph
