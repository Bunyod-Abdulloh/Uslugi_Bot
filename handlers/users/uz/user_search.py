from aiogram import Router, F, types

from handlers.users.uz.start import uz_main_keyboard
from loader import db

user_search_router = Router()


#  🏥 Klinika bo'yicha qidirish


@user_search_router.message(F.text == "salom")
async def get_photo_id(message: types.Message):
    # file_id = message.photo[-1].file_id
    # name = message.caption
    # await db.add_company(
    #     name=name, image=file_id
    # )
    clinics = await db.select_all_clinics()
    print(clinics)
    await message.answer(
        text="Bazaga qo'shildi!"
    )


@user_search_router.message(F.text == "🏡 Bosh sahifaga qaytish")
async def back_main_menu(message: types.Message):
    await message.answer(
        text="Bosh sahifa", reply_markup=uz_main_keyboard
    )


@user_search_router.inline_query(F.text == "search_clinic")
async def search_inline_mode(inline_query: types.InlineQuery):
    clinics = await db.select_all_clinics()
    inline_result_clinics = []
    for clinic in clinics:
        inline_result_clinics.append(
            types.InlineQueryResultArticle(
                id=str(clinic['id']),
                title=clinic['name'],
                description=f"Manzil: {clinic['address']}",
                input_message_content=types.InputTextMessageContent(
                    message_text=f"Hello, this is result {clinic['id']}"
                )
            )
        )
    await inline_query.answer(results=inline_result_clinics,
                              switch_pm_parameter="Qidirish",
                              switch_pm_text="Pastdan tepaga suring"
                              )


@user_search_router.message(F.text == "💉 Shifokor sohasi bo'yicha qidirish")
async def search_doctor(message: types.Message):
    pass


@user_search_router.message(F.text == "🚶‍ Eng yaqin klinikalar ro'yxatini chiqarish")
async def nearest_clinics(message: types.Message):
    pass


@user_search_router.message(F.text == "📍 Manzil bo'yicha qidirish")
async def search_address(message: types.Message):
    pass
