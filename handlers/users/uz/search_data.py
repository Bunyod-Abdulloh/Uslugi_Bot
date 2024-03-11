from LxmlSoup import LxmlSoup
import requests
from aiogram import Router, F, types

from loader import db

router = Router()


@router.message(F.text == "add")
async def add_clinics_to_db(message: types.Message):
    html = requests.get(message.text).text

    soup = LxmlSoup(html)

    search_name = soup.find_all('span', itemprop='name')
    clinic_name = search_name[0].text()

    search_address = soup.find_all('span', class_='output_f')
    clinic_address = search_address[0].text()

    search_landmarks_one = soup.find_all('div', class_="roww")
    landmark = str()
    work_time = str()

    for n, datas in enumerate(search_landmarks_one):
        search = soup.find_all('span', class_='data')
        search_ = search[n].text()
        if n == 1:
            landmark = search_
        if n == 2:
            work_time = search_

    search_phone = soup.find_all('span', class_='data-phone')
    clinic_phone = search_phone[0].text()

    clinic_description = str()
    search_desription = soup.find_all('p', align='justify')
    for n in search_desription:
        clinic_description += n.text()

    doctors = []
    search_doctors_one = soup.find_all(tag='div', class_='clinicshifokor')
    search_doctors_two = search_doctors_one[0].find_all(tag='li')

    for doctor in search_doctors_two:
        doctors.append(doctor.text())

    services = []
    search_services_one = soup.find_all(tag='div', class_='clinicxizmatlar')
    search_service_two = search_services_one[0].find_all(tag='li')

    for service in search_service_two:
        services.append(service.text())

    await db.add_company(
        name=clinic_name, address=clinic_address, landmark=landmark,
        work_time=work_time, phone_one=clinic_phone, description=clinic_description
    )
    await db.add_ds_and_ss(name=clinic_name, )


services = ['Akusherlik', 'Algologiya', 'Allergologiya', 'Muqobil tibbiyot',
            'Tahlillar', 'Angiologiya', 'Andrologiya', 'Anezteziologiya va reanimatologiya']
