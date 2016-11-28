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
	wb.active['B4'] = 'Date'
	wb.active['C4'] = 'Category'
	wb.active['D4'] = 'Amount'
	wb.active['E4'] = 'Check Number'
	wb.active['F4'] = 'Description'
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



class Transaction:

	entryNumber = 0

	def __init__(self, date = [12,12,1212] , category = 'None' , amount = 0.0, checknum = 'None' , desc ='Ex. This was a purcahse'):
		# Date formati is Month/ Day / Year
		self.date = date
		#Category is used to lable puchases (i.e: Food, Entertainment, Gas, Travel,...etc)
		self.category = category
		# The Amount of the transaction
		self.amount = amount
		# The Check Number of the transaction, if needed
		self.checknum = checknum
		# Short Description of the purpose of the transaction, further defines the transaction with help of category
		self.desc = desc
	
	# Create Entry
	def createTransaction(self, date = [12,12,1212] , category = 'None' , amount = 0.0, checknum = 'None' , desc ='Ex.This was a purcahse'):
		pass

# Edit Entry


