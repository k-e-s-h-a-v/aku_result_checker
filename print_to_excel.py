# Writing to an excel  
# sheet using Python 
import aku_result_checker.result_checker as result
from xlwt import Workbook 
  
# Workbook is created 
wb = Workbook() 
  
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 
  
sheet1.write(1, 0, 'ISBT DEHRADUN') 
 
  
wb.save('xlwt example.xls') 
