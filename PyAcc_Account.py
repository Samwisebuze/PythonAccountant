from PyAcc_Transactions import *
from openpyxl import Workbook

transaction = Transaction()
wb = Workbook()
# Use AcctClassses
# worksheets = accounts
# edit create worksheet to setup frrame work of blanace tracking

#########
# Python Accountant Class Definitions
# Desc: Contains Class definitions used in PyAcc.py and AccountantMain.py
# Created By: Samuel Buzas & Elizabeth Sheetz
#########


# Create WorkSheet
def create_worksheet(sheet_name = "Trackin Sheet", filename = "MyFirstBudget"):
	dest_filename = filename + '.xlsx'
	wb = load_workbook(dest_filename)
	wb.create_sheet(sheet_name)
	wb.save(dest_filename)


class Account:

	def __init__(self, account_Name, workbook_name = None, transactions = [], initial_balance = 0):
		self.workbook_name = workbook_name
		self.transactions = transactions
		self.initial_balance = initial_balance
		self.balance = initial_balance
		self.account_Name = account_Name

	def balance_update(self,account_Name, amount):
		wb.account_Name['G2'] = "=SUM(C2, C" + str(transaction.checkEntries(workbk)) +")"
		self.balance =  wb.account_Name['G2'].value

	# def get_transactions(self):
	# 	#print list of transaction numbers
	# 	print(t.entryNumber for t in self.transactions)

	# def add_transaction(self, tnew):
	# 	#add transaction to transaction list and update balance
	# 	self.transactions += [tnew]
	# 	self.balance_update(tnew.amount)

	def create_new_Account(self, account_Name = "Account0", initial_balance =0):
		#Use to create and populate a new account structure
		workbk = self.workbook +'.xlsx'
		wb.create_worksheet(account_Name)
		wb.active = wb.account_Name
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
		wb.active['G1'] = str(account_Name) + ' Balance'
		wb.active.column_dimensions['D'].width = 25
		wb.active['G2'] = "=SUM(C2, C" + str(transaction.checkEntries(workbk)) +")"
		wb.save(workbk)









