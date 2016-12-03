################
# Python Accountant
# By: Samuel Buzas & Elizabeth Sheetz
# Version 0.1
#################

from PyAcc_Transactions import *
from PyAcc_Account import *
from openpyxl import Workbook

import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# def main():
# 	print("Welcome to Python Accountant!")
# 	print("Let's create a file.")
# 	new_filename = input("Enter a filename: ")
# 	new_worksheetname = input("Enter a worksheet name: ")
# 	PyAcc.create_workbook(new_filename, new_worksheetname)
# 	print("Open the file and see if it worked.")


# if __name__ == "__main__":
# 	main()


def main():
	wb = Workbook()
	account = Account()
	cls()

	while True:
		cls()
		print("\t\t Welcome to Python Accountant!\n")
		print("What Would you like to do today? \n")
		#Menu
		print("You are Curently Editing the " + account.account_Name + " Account in the " + account.workbook_name +" workbook.\n\n")
		print("\t\t Menu \n")
		print("\t 1 : \t Create a New Budget \n")
		print("\t 2 : \t Create a New Account (Must have an existing Workbook) \n")
		print("\t 3 : \t Select a Budget and an account to work with.\n")
		print("\t\t 3a : \t Enter a New Transaction \n")
		print("\t\t 3b : \t Edit an Existing Transaction (Must know Transaction number (Row Number)) \n")
		print("\t 5 : \t Exit Python Accountant  \n")

		option = input("Please Input an option: ")
		option = str(option)
		# Cases
		if option == '1':
			print("Let's Create a file.\n")
			filename = input("Enter a filename: ")
			worksheet = input("Enter a workseet name: ")
			create_workbook(filename,worksheet)

		if option == '2':
			print("Let's Create a new Account.\n")
			filename = input("Enter an existing filename  (No need to include the file extnesion): ")
			account_name =input("Enter a Account Name name: ")
			init_balance = input("Enter the initial balance: ")
			account = Account(account_name,filename)
			account.create_new_Account(init_balance)
			

		if option == '3':
			print("What workbook would you like to work with?\n")
			filename = input("Enter A Filename: ")
			wb = load_workbook(str(filename) +'.xlsx')

			print("Which Account would you like to work on?\n")
			print(wb.sheetnames)
			account_name = input("Please Enter an Account: ")
			transaction = Transaction(filename,account_name)
			account = Account(account_name,filename)

		if option == '3a':
			print("Lets add an new Transaction.\n")
			# year,month,day,categroy,amount,checknum,desc
			# Date
			print("What is the Date of the Transaction?\n")
			year = input("Enter the Year: ")
			month = input("Enter the Month: ")
			day = input("Enter the Day: ")

			print("How much was the transaction?\n Does it have a category?\n")
			amount = input("Enter the amount (Use negative for withdrawls and purchases): ")
			category = input("Enter the Category: ")

			checknum = input("If you used a check, please enter the check number here (Otherwise leave blank): ")
			print("Leave a small description of the transaction here:\n")
			description = input()

			transaction.createTransaction(int(year),int(month),int(day),category,float(amount),checknum,description)

		if option == '3b':
			pass
			

		if option == '5':
			print("Thank you for chosing Python Accountant for you budgeting needs!")
			import sys
			sys.exit(1)
		else:
			print("Please make a vaild selection from the Menu \n\n" )

if __name__ == "__main__":
	main()


