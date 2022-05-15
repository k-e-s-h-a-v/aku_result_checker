import time
import concurrent.futures
from helpers import value, response, check_result, save_to_xls

start = time.perf_counter()

head = ['Reg_No.','Name','SGPA','current CGPA']

reg_numlist=list(range(18103108001,18103108057))+[19104108905,19103108902]    

resultList = []

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(check_result, reg_no) for reg_no in reg_numlist] 
    for futureObj in concurrent.futures.as_completed(results):
        result = futureObj.result()
        print(result)
        resultList.append(result)
        
save_to_xls(resultList)

finish = time.perf_counter()
print(f"finished in {finish-start} seconds")