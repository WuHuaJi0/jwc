import xlrd
from xlrd.timemachine import REPR
import sys
import glob
book = xlrd.open_workbook("class.xlsx")
# print "The number of worksheets is", book.nsheets
# print "Worksheet name(s):", book.sheet_names()
# sh = book.sheet_by_index(0)
# print sh.name, sh.nrows, sh.ncols
# print "Cell D30 is", sh.cell_value(rowx=29, colx=3)
# for rx in range(sh.nrows):
#     print sh.row(rx)
# Refer to docs for more details.
# Feedback on API is welcomed.
#
#
# from xlrd import