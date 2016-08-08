from openpyxl import load_workbook
import logging
count = '1'
wb = load_workbook(filename='C:/1/units.xlsx')
sheet_ranges = wb['Sheet1']
def printexcel():
    global count
    while (sheet_ranges['A'+str(count)+''].value != None):
       count=str(count)
       unitid=sheet_ranges['A'+count+''].value
       print unitid
       count = int(count) + 1

# printexcel()
logging.basicConfig(level=logging.DEBUG)
logging.warning('Watch out!')
logging.info('I told you so')
logging.error("sadsad errorrrrrrr")


