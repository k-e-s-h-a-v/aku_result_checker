import time
import concurrent.futures
from helpers import value, response, check_result, save_to_xls

start = time.perf_counter()

API6thsem = "https://results.akuexam.net/ResultsBTechBPharm6thSemPub2021.aspx"
API7thsem = "https://results.akuexam.net/ResultsBTechBPharm7thSemPub2021.aspx"

sem = "VII"

head = ['Reg_No.','Name','SGPA','current CGPA']

reg_numlist=list(range(18104108001, 18104108061))

resultList = []

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(check_result, API7thsem, sem, reg_no) for reg_no in reg_numlist] 
    for futureObj in concurrent.futures.as_completed(results):
        result = futureObj.result()
        print(result)
        resultList.append(result)
        
save_to_xls(resultList)

finish = time.perf_counter()
print(f"finished in {finish-start} seconds")
