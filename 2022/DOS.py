from requests_html import HTMLSession
import webbrowser

status_code = 0 
text = ""
URL = "http://results.akuexam.net/ResultsBTechBPharm7thSemPub2021.aspx?Sem=VII&RegNo=1810410012"
# URL = 'https://requests.readthedocs.io/projects/requests-html/en/latest/'
# URL = 'https://www.google.com/'

while status_code != 200:
    r = HTMLSession().get(URL)
    print(r)
    status_code = r.status_code
    print("status:", status_code, "retrying...")
    # print(dir(r))
else:
    text = r.text
    # print(text)
    print("found it")
    with open("seven_sem.html", "w", encoding="utf-8") as f:
        f.write(text)
    webbrowser.open("seven_sem.html")
