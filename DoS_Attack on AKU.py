from requests_html import HTMLSession
from important_functions import value, response, check_result

import time
# import csv

start = time.perf_counter()

head = ["Reg_No.", "Name", "SGPA", "CGPA"]
print(head)

# csv_file = open('results.csv', "w")
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(head)
reg_numlist = [
    18103108025,
    18103108042,
    18103108006,
    18104108012,
    18103107013,
] 

for reg_no in reg_numlist:
    print(check_result(reg_no))
    # csv_writer.writerow([name, sgpa, cgpa])

# csv_file.close()
finish = time.perf_counter()

print(f"finished in {finish-start} seconds")