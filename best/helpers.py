from requests_html import HTMLSession
from xlwt import Workbook 

# value = lambda res, id, index: res.find(f"#{id}", first=True,).text.split("\n")[index]
def value(res, id, index):
    try:
        return res.find(f"#{id}", first=True,).text.split("\n")[index]
    except: 
        return ''

response = (
    lambda payload, URL: HTMLSession()
    .get(
        "https://results.akuexam.net/ResultsBTechBPharm6thSemPub2021.aspx",
        params=payload,
    )
    .html
)

def check_result(reg_no):
    payload = {"Sem": "VI", "RegNo": reg_no}

    while 1:
        try:
            res = response(payload, "https://results.akuexam.net/ResultsBTechBPharm6thSemPub2021.aspx")
            break
        except:
            print("retrying for a number")

    name = value(res, "ctl00_ContentPlaceHolder1_DataList1_ctl00_StudentNameLabel", 0)
    sgpa = value(res, "ctl00_ContentPlaceHolder1_DataList5_ctl00_GROSSTHEORYTOTALLabel", 0)
    cgpa = value(res, "ctl00_ContentPlaceHolder1_GridView3", 17)

    output = [reg_no, name, sgpa, cgpa]
    return output


# writing to results.xls
def write(index, arr, sheet):
    for i, elem in enumerate(arr):
        sheet.write(2+index, 1+i, elem)
    print(arr)

def save_to_xls(arr):
    # Workbook is created 
    wb = Workbook() 

    # add_sheet is used to create sheet. 
    sheet1 = wb.add_sheet('6th Sem')

    head = ['Reg_No.','Name','SGPA','current CGPA']
    write(-1, head, sheet1)

    for i, elem in enumerate(arr):
        write(i, elem, sheet1)
        
    #Saving the workbook
    wb.save('result.xls')

    print('"result.xls" saved')