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