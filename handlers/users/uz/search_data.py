import asyncio

from LxmlSoup import LxmlSoup
import requests
from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from loader import db
from states.user_states import UserSearchUz

router = Router()


@router.message(F.text == "add")
async def add_clinics_state(message: types.Message, state: FSMContext):
    await message.answer(
        text="Link yuboring"
    )
    await state.set_state(UserSearchUz.add_data)


@router.message(UserSearchUz.add_data)
async def add_clinics_data(message: types.Message, state: FSMContext):
    # html_one = requests.get(message.text).text
    #
    # soup_one = LxmlSoup(html_one)
    # main_links = []
    # search_all_clinics = soup_one.find_all(tag="sup", class_="featured")
    # for n in search_all_clinics:
    #     href = n.previous_sibling().get('href')
    #     main_links.append(f"https://clinics.uz{href}")
    #     await asyncio.sleep(2)
    # await message.answer(text="Jarayon main_links da!")

    # for i, link in enumerate(main_links):
    html_two = requests.get(message.text).text
    soup_two = LxmlSoup(html_two)

    search_name = soup_two.find_all('span', itemprop='name')
    clinic_name = search_name[0].text()

    search_address = soup_two.find_all('span', class_='output_f')
    clinic_address = search_address[0].text()

    search_landmarks_one = soup_two.find_all('div', class_="roww")
    landmark = str()
    work_time = str()

    for n, datas in enumerate(search_landmarks_one):
        search = soup_two.find_all('span', class_='data')
        search_ = search[n].text()
        if n == 1:
            landmark = search_
        if n == 2:
            work_time = search_
        await asyncio.sleep(2)
    await message.answer(text="Jarayon search_landmarksda da!")

    search_phone = soup_two.find_all('span', class_='data-phone')
    clinic_phone = search_phone[0].text()

    clinic_description = str()
    search_desription = soup_two.find_all('p', align='justify')
    for n in search_desription:
        clinic_description += n.text()
        await asyncio.sleep(2)
    await message.answer(text="Jarayon clinic_description da!")

    id_ = await db.add_ds_and_ss(name=clinic_name)

    search_services_one = soup_two.find_all(tag='div', class_='clinicxizmatlar')
    search_service_two = search_services_one[0].find_all(tag='li')

    for service in search_service_two:
        await db.update_ds_service_by_id(service=service.text(), id_=id_["id"])
        await asyncio.sleep(2)
    await message.answer(text="Jarayon services da!")

    search_doctors_one = soup_two.find_all(tag='div', class_='clinicshifokor')
    search_doctors_two = search_doctors_one[0].find_all(tag='li')

    for doctor in search_doctors_two:
        await db.update_ds_doctor_by_id(doctor=doctor.text(), id_=id_["id"])
        await asyncio.sleep(2)
    await message.answer(text="Jarayon doctors da!")

    await db.add_company(
        name=clinic_name, address=clinic_address, landmark=landmark,
        work_time=work_time, phone_one=clinic_phone, description=clinic_description
    )
    await message.answer(text="Ma'lumotlar omborga joylandi!")
    await asyncio.sleep(3)


services = ['Akusherlik', 'Algologiya', 'Allergologiya', 'Muqobil tibbiyot',
            'Tahlillar', 'Angiologiya', 'Andrologiya', 'Anezteziologiya va reanimatologiya']
