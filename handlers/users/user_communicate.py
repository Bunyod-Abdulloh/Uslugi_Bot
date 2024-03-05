from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from keyboards.inline.user_inline_buttons import user_select_doctors_ibutton, user_send_complaint, \
    select_gender_communicate
from loader import db
from states.user_states import UserCommunicate

user_communicate_router = Router()


@user_communicate_router.callback_query(F.data.contains("communicate_"))
async def communicate_gender_doctor(call: types.CallbackQuery, state: FSMContext):
    gender_doctor = call.data.split("_")[1]

    add_complaint = await db.add_complaint(
        telegram_id=call.from_user.id, gender_doctor=gender_doctor
    )
    await state.update_data(
        complaint_id=add_complaint[0]
    )
    await call.message.edit_text(
        text="Shifokor turini tanlang", reply_markup=user_select_doctors_ibutton()
    )


@user_communicate_router.callback_query(F.data.contains("communicatedoctors_"))
async def communicate_type_doctor(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()

    id_ = data["complaint_id"]
    type_doctor = call.data.split("_")[1]

    await db.update_doctor_complaint(
        type_doctor=type_doctor, id_=id_
    )
    await call.message.edit_text(
        text="Shikoyatingizni kiriting"
    )
    await state.set_state(UserCommunicate.complaint)


@user_communicate_router.message(UserCommunicate.complaint)
async def get_complaint(message: types.Message, state: FSMContext):
    data = await state.get_data()
    id_ = data["complaint_id"]
    await db.update_user_complaint(
        complaint=message.text, id_=id_
    )
    await message.answer(
        text="Shikoyatingiz qabul qilindi! Tasdiqlaysizmi?",
        reply_markup=user_send_complaint()
    )


@user_communicate_router.callback_query(F.data == "re_enter_communicate")
async def communicate_re_enter(call: types.CallbackQuery, state: FSMContext):
    data = await state.update_data()
    id_ = data["complaint_id"]
    await db.delete_complaint_by_id(
        id_=id_
    )
    await state.clear()
    datas = await state.get_data()
    print(datas)
    await call.message.edit_text(
        text="Tugmalardan birini tanlang",
        reply_markup=select_gender_communicate()
    )


@user_communicate_router.callback_query(F.data == "check_communicate")
async def check_communicate(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    id_ = data["complaint_id"]

    user = await db.select_complaint_by_id(
        id_=id_
    )
    # user_ = await db.select_user(
    #     telegram_id=call.from_user.id
    # )
    # text = (f"Bemordan yangi habar qabul qilindi!\n\nSana: {user['checked_date']}"
    #         f"\nBemor ismi: {user_['fullname']}"
    #         f"\nTelefon raqami: {user_['phone_one']}"
    #         f"\nSo'ralgan shifokor: {user['gender_doctor']} | {user['type_doctor']}"
    #         f"\nHabar matni: {user['complaint']}")
    # print(text)
    await call.message.edit_text(
        text="Habaringiz qabul qilindi va shifokorlar guruhiga yuborildi! Onlaynda bo'lgan shifokorlar tez orada "
             "javob yuborishadi!"
    )


@user_communicate_router.callback_query(F.data == "back_communicate")
async def back_communicate(call: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.edit_text(
        text="Tugmalardan birini tanlang",
        reply_markup=select_gender_communicate()
    )
