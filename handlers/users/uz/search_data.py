from LxmlSoup import LxmlSoup
import requests

html = requests.get('https://clinics.uz/uzb/catalog/medical-centers/estimed').text

soup = LxmlSoup(html)

# search_name = soup.find_all('span', itemprop='name')
# clinic_name = search_name[0].text()

# search_address = soup.find_all('span', class_='output_f')
# clinic_address = search_address[0].text()

# search_landmarks_one = soup.find_all('div', class_="roww")
# landmark = str()
# work_time = str()
#
# for n, datas in enumerate(search_landmarks_one):
#     search = soup.find_all('span', class_='data')
#     search_ = search[n].text()
#     if n == 1:
#         landmark = search_
#     if n == 2:
#         work_time = search_
#
# print(f"{landmark} \n{work_time}")


services = ['Akusherlik', 'Algologiya', 'Allergologiya', 'Muqobil tibbiyot',
            'Tahlillar', 'Angiologiya', 'Andrologiya', 'Anezteziologiya va reanimatologiya']
