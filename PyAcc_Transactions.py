#########
# Python Accounatn Header 
# Desc: Contains Any functions or shortcut snippets used to sumplify main
# Created By: Samuel Buzas & Elizabeth Sheetz
#########
import datetime

from openpyxl import Workbook
from openpyxl.compat import range
from openpyxl.utils import get_column_letter
from openpyxl import load_workbook

#Constant
wb = Workbook()

# Create Workbook
def create_workbook(filename = "MyFirstBudget", sheet_name = "SimpleBudget"):
	dest_filename = filename + '.xlsx'
	wb.active.title = sheet_name
	wb.active['A1'] = 'Date'
	wb.active.column_dimensions['A'].width = 17
	wb.active['B1'] = 'Category'
	wb.active.column_dimensions['B'].width = 15
	wb.active['C1'] = 'Amount'
	wb.active.column_dimensions['C'].width = 10
	wb.active['D1'] = 'Check Number'
	wb.active.column_dimensions['D'].width = 17
	wb.active['E1'] = 'Description'
	wb.active.column_dimensions['E'].width = 50
	wb.geuss_types = True
	wb.save(filename = dest_filename)

# Create WorkSheet
def create_worksheet(sheet_name = "Trackin Sheet", filename = "MyFirstBudget"):
	dest_filename = filename + '.xlsx'
	wb = load_workbook(dest_filename)
	wb.create_sheet(sheet_name)
	wb.save(dest_filename)

# Create Blank Graph
def create_table(filename = "MyFirstBudget", sheet_name = "SimpleBudget"):
	dest_filename = filename + '.xlsx'
	wb.active.title = sheet_name
	wb.save(dest_filename)



class Transaction:


	def __init__(self, workbook = 'Default' ,account_name = 'Default'):
		self.workbook = workbook + '.xlsx'
		self.account_name = str(account_name)
		# excel isnt 0 based and row 1 is for titles
		self.entryNumber = 2
	
	# Create Entry
	def createTransaction(self, year = 1996 , month = 12,  day = 12, category = 'None' , amount = 0.0, checknum = 'None' , desc ='Ex.This was a purcahse'):
		# Load budget workbook to edit
		wb = load_workbook(self.workbook)
		# check that your not overwrting previous entries
		sheet = wb[self.account_name]
		#Alawyas start at entry 2, to prevetn massive gaps in the sheet
		self.entryNumber = 2
		while sheet['A'+ str(self.entryNumber)].value != None:
			self.entryNumber += 1

		sheet['A' + str(self.entryNumber)] = datetime.datetime(year, month, day)
		sheet['A' + str(self.entryNumber)].number_format
		wb.geuss_types= True
		sheet['B' + str(self.entryNumber)] = category
		sheet['C' + str(self.entryNumber)] = amount
		sheet['D' + str(self.entryNumber)] = checknum
		sheet['E' + str(self.entryNumber)] = desc

		wb.save(self.workbook)
		self.entryNumber += 1

	def checkEntries(self,filename,account_name):
		wb = load_workbook(filename)
		sheet = wb[account_name]
		self.entryNumber = 2
		while sheet['A'+ str(self.entryNumber)].value != None:
			self.entryNumber += 1
		return self.entryNumber



	# Edit Entries
	def updateTransaction_Date(self, entryNumber, year, month, day):
		wb = load_workbook(self.workbook)
		sheet = wb.self.account_name
		self.entryNumber = entryNumber
		# Update the description
		sheet['A' + str(self.entryNumber)] = datetime.datetime(year, month, day)
		sheet['A' + str(self.entryNumber)].number_format
		wb.geuss_types= True

		wb.save(self.workbook)

	def updateTransaction_Category(self, entryNumber, category):
		wb = load_workbook(self.workbook)
		sheet = wb.self.account_name
		self.entryNumber = entryNumber
		# Update the description
		sheet['B' + str(self.entryNumber)] = category

		wb.save(self.workbook)

	def updateTransaction_amount(self, entryNumber, amount):
		wb = load_workbook(self.workbook)
		sheet = wb.self.account_name
		self.entryNumber = entryNumber
		# Update the description
		sheet['C' + str(self.entryNumber)] = amount

		wb.save(self.workbook)

	def updateTransaction_checknum(self,entryNumber, checknum):
		wb = load_workbook(self.workbook)
		sheet = wb.self.account_name
		self.entryNumber = entryNumber
		# Update the description
		sheet['D' + str(self.entryNumber)] = checknum

		wb.save(self.workbook)

	def updateTransaction_desc(self, entryNumber, desc):
		wb = load_workbook(self.workbook)
		sheet = wb.self.account_name
		self.entryNumber = entryNumber
		# Update the description
		sheet['E' + str(self.entryNumber)] = desc

		wb.save(self.workbook)






