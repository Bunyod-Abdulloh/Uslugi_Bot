import requests
from LxmlSoup import LxmlSoup

clinics = ['https://clinics.uz/uzb/catalog/medical-centers/big-pharm'
           'https://clinics.uz/uzb/catalog/medical-centers/darmon-servis',
           'a']

html_two = requests.get("https://clinics.uz/uzb/catalog/medical-centers").text
soup_two = LxmlSoup(html_two)

search_name = soup_two.find_all('div', id='subcats')

for n in search_name:
    for i in n.select('a'):
        print(i.text())
