import csv
import requests
from bs4 import BeautifulSoup

url = "http://www.seoul.go.kr/coronaV/coronaStatus.do"

filename = "crawling_Seoul.csv"
f = open(filename, "w", encoding = "utf-8-sig", newline = "") #encoding = "utf8" -> 엑셀에서 한글깨지면 utf-8-sig
writer = csv.writer(f)

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

data_rows = soup.find("table", attrs={"class" : "tstyle-status pc pc-table"}).find("tbody").find_all("tr")
for row in data_rows:
    columns = row.find_all(["td", "th"])
    data = [column.get_text().strip() for column in columns]
    #print(data)
    writer.writerow(data)
