from xlwt import Workbook 
from important_functions import value, response, check_result

# Workbook is created 
wb = Workbook() 

# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('6th Sem')

# writing to results.xls
def write(index, arr):
    for i, elem in enumerate(arr):
        sheet1.write(2+index, 1+i, elem)
    print(arr)

head = ['Reg_No.','Name','SGPA','current CGPA']

write(-1, head)
    
'''This is list of Registration numbers
if yours is missing simply add it in the end by +[12345678910]
where '12345678910' is your reg no'''

reg_numlist=list(range(18103108001,18103108057))+[19104108905,19103108902]    

for i, reg_no in enumerate(reg_numlist):
    write(i, check_result(reg_no))
        
#Saving the workbook
wb.save('result.xls')

print('"result.xls" saved')

