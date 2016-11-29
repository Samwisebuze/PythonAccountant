################
# Python Accountant
# By: Samuel Buzas & Elizabeth Sheetz
# Version 0.1
#################

from PyAcc import *
from PyAcc import Transaction
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
	exit = False
	transaction = Transaction()
	cls()
	print("\t\t Welcome to Python Accountant!\n")
	print("What Would you like to do today? \n")

	while exit == False:

		#Menu
		print("\t\t Menu \n")
		print("\t 1 : \t Create a New Budget \n")
		print("\t 2 : \t Create a New Worksheet (Must have an existing Workbook) \n")
		print("\t 3 : \t Enter a New Transaction \n")
		print("\t 4 : \t Edit an Existing Transaction (Must know Transaction number) \n")
		print("\t 5 : \t Exit Python Accountant  \n")

		option = input("Please Input an option: ")

		# Cases
		if option == '1':
			print("Let's Create a file.\n")
			filename = input("Enter a filename: ")
			worksheet = input("Enter a workseet name: ")
			create_workbook(filename,worksheet)

		if option == '2':
			print("Let's Create a new Worksheet.\n")
			filename = input("Enter an existing filename  (No need to include the file extnesion): ")
			worksheet =input("Enter a worksheet name: ")
			create_worksheet(worksheet,filename)

		if option == '3':
			print("Let's add an new transaction.\n")

		if option == '5':
			print("Thank you for chosing Python Accountant for you budgeting needs!")
			import sys
			sys.exit(1)
		else:
			print("Please make a vaild selection from the Menu \n\n" )

if __name__ == "__main__":
	main()


