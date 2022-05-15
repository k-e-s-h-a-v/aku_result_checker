from requests_html import HTMLSession
from helpers import value, response, check_result
import time
import concurrent.futures

start = time.perf_counter()

print(["Reg_No.", "Name", "SGPA", "CGPA"])

reg_numlist = [
    18103108025,
    18103108042,
    18103108006,
    18104108012,
    18103107013,
] 

with concurrent.futures.ThreadPoolExecutor() as executor:

    # Method 1: will show results as they are completed
    results = [executor.submit(check_result, reg_no) for reg_no in reg_numlist]  #submit() returns a future object
    for futureObj in concurrent.futures.as_completed(results):
        print(futureObj.result())

    # Method 2: returns all at once in sequence after everything is finished
    # results = executor.map(check_result, reg_numlist)
    # for result in results:
    #     print(result)
    

finish = time.perf_counter()

print(f"finished in {finish-start} seconds")
