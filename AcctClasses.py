#########
# Python Accountant Class Definitions
# Desc: Contains Class definitions used in PyAcc.py and AccountantMain.py
# Created By: Samuel Buzas & Elizabeth Sheetz
#########

class Account:

	def __init__(self, workbook_name = None, transactions = [], initial_balance = 0):
		self.workbook_name = workbook_name
		self.transactions = transactions
		self.initial_balance = initial_balance
		self.balance = initial_balance

	def balance_update(self, amount):
		self.balance += amount

	def get_transactions(self):
		#print list of transaction numbers
		print(t.entryNumber for t in self.transactions)

	def add_transaction(self, tnew):
		#add transaction to transaction list and update balance
		self.transactions += [tnew]
		self.balance_update(tnew.amount)

	def __create_and_add_transaction(self, Day = 12, Month =12, Year=12 , category = 'None' , amount = 0.0, checknum = 'None' , desc ='Ex. This was a purchase'):
		#create new transaction
		tnew = Transaction(Day, Month, Year, category, amount, checknum, desc)
		#store new transaction in Acct
		self.add_transaction(tnew)

def create_and_add_transaction():
	print ("Creating a new transaction.")
	print ("Please enter the following and press enter.")
	day = input("day: ")
	month = input("month: ")
	year = input("year: ")
	category = input("category: ")
	amount = input("amount: ")
	checknum = input("check no.: ")
	desc = input("description/for: ")
	#this might need to be part of the class.


def create_new_Account():
	#Use to create and populate a new account structure
	print("Creating a new account.")
	account_name = input("Enter name for account: ")
	myAcct = Account(account_name)
	print("Account Created. Balance is: " + myAcct.balance + ".")
	print("Add some transactions. You will need to invent new transactions.")



class Transaction:
	

	def __init__(self, Day = 12, Month =12, Year=12 , category = 'None' , amount = 0.0, checknum = 'None' , desc ='Ex. This was a purchase'):
		# Date format is Month/ Day / Year
		self.Day = Day
		self.Month = Month
		self.Year = Year
		#Category is used to lable puchases (i.e: Food, Entertainment, Gas, Travel,...etc)
		self.category = category
		# The Amount of the transaction
		self.amount = amount
		# The Check Number of the transaction, if needed
		self.checknum = checknum
		# Short Description of the purpose of the transaction, further defines the transaction with help of category
		self.desc = desc
		# excel isnt 0 based and row 1 is for titles
		self.entryNumber = 2
	
	# Create Entry
	def createTransaction(self, day= 12, month= 12, year= 12 , category = 'None' , amount = 0.0, checknum = 'None' , desc ='Ex.This was a purcahse'):
		sheet = wb.active
		sheet['A' + str(self.entryNumber)] = datetime.datetime(year, month, day)
		sheet['A' + str(self.entryNumber)].number_format
		wb.geuss_types= True
		sheet['B' + str(self.entryNumber)] = category
		sheet['C' + str(self.entryNumber)] = amount
		sheet['D' + str(self.entryNumber)] = checknum
		sheet['E' + str(self.entryNumber)] = desc

		wb.save('MyFirstBudget.xlsx')
		self.entryNumber += 1