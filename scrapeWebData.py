import requests
import csv

payload = {"username": "<USERNAME>", "password": "<PASSWORD>" }
login_url = "<LOGIN_URL>"

#Perform Login
session_requests = requests.session()
result = session_requests.post(login_url, data = payload)

from bs4 import BeautifulSoup
resp = BeautifulSoup(result.content,"html.parser")

stuff = resp.find_all("tr")
ls = []

for row in stuff:
    var = row.find_all("td")
    tmp = []
    for r in var:
        tmp.append(r.text)
    ls.append(tmp)

with open("output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(ls)
    
