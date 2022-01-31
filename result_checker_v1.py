import urllib.request
import time
from xlwt import Workbook 

# Workbook is created 
wb = Workbook() 
  
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('5th Sem')

ini=['Reg_No.','Name','SGPA']
for m in range(3):
    sheet1.write(1, 1+m, ini[m])
    
#18103107013 = Dharnidhar
reg_numlist=list(range(18103107001,18103107070))    

count=0
for reg_no in reg_numlist:
    while 1:
        try:
            text=str(urllib.request.urlopen("https://results.akuexam.net/ResultsBTechBPharm5thSemPub2020.aspx?Sem=V&RegNo={0}".format(reg_no),timeout=15).read())
            break
        except:
            print("retrying...for",reg_no)
    def student_name(text):
        prefix='''<span id="ctl00_ContentPlaceHolder1_DataList1_ctl00_StudentNameLabel" style="font-weight: 700">'''
        n=text.find(prefix)+len(prefix)
        suffix=text.find('''</span>''',n)
        name=''
        for j in range(suffix-n):
            name+=text[n+j]
        return name

    def student_sgpa(text):
        prefix='''<span id="ctl00_ContentPlaceHolder1_DataList5_ctl00_GROSSTHEORYTOTALLabel" style="font-weight: 700">'''
        s=text.find(prefix)+len(prefix)
        suffix=text.find('''</span>''',s)
        sgpa=''
        for i in range(suffix-s):
            sgpa+=text[s+i]
        return (sgpa)
    
    output = [reg_no,student_name(text),student_sgpa(text)]
    count+=1
    # writing to results.xls
    for l in range(3):
        sheet1.write(2+count, 1+l, output[l])

    print(output)

#Saving the workbook
wb.save('result_MIT.xls')

print('''\n "result.xls" saved to folder \n C:\\Users\keshav\AppData\Local\ \n Programs\Python\Python39\\aku_result_checker''')

time.sleep(10)
