################
# Python Accountant
# By: Samuel Buzas & Elizabeth Sheetz
# Version 0.1
#################

import PyAcc

def main():
	print("Welcome to Python Accountant!")
	print("Let's create a file.")
	new_filename = input("Enter a filename: ")
	new_worksheetname = input("Enter a worksheet name: ")
	PyAcc.create_workbook(new_filename, new_worksheetname)
	print("Open the file and see if it worked.")


if __name__ == "__main__":
	main()