#########
# Python Accounatn Header 
# Desc: Contains Any functions or shortcut snippets used to sumplify main
# Created By: Samuel Buzas & Elizabeth Sheetz
#########
from openpyxl import Workbook
from openpyxl.compat import range
from openpyxl.utils import get_column_letter

# Create Workbook
#Supply a WorkBook/Project name. and a filename for it to be saved as
wb = Workbook()
def createWB(filename = "MyFirstWorkBook"):
	dest_filename = filename + '.xlsx'
	wb.save(filename = dest_filename)

# Create WorkSheet

def createWS(sheet_name = "Worksheet", filename = "MyFirstWorkBook"):
	#do shome shite
	dest_filename = filename + '.xlsx'
	wb.save(filename = dest_filename)

	wb.create_sheet(sheet_name)
	wb.save(filename = dest_filename)