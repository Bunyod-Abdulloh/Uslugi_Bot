from aiogram import Router, F, types

from handlers.users.uz.start import uz_main_keyboard

user_search_router = Router()


#  🏥 Klinika bo'yicha qidirish

@user_search_router.message(F.text == "🏡 Bosh sahifaga qaytish")
async def back_main_menu(message: types.Message):
    await message.answer(
        text="Bosh sahifa", reply_markup=uz_main_keyboard
    )


@user_search_router.inline_query(F.query == "anor")
async def search_inline_mode(inline_query: types.InlineQuery):
    results = [
        types.InlineQueryResultArticle(
            id='1',
            title='Result 1',
            input_message_content=types.InputTextMessageContent(message_text='Hello, this is result 1')
        ),
        types.InlineQueryResultArticle(
            id='2',
            title='Result 2',
            input_message_content=types.InputTextMessageContent(message_text='Hello, this is result 2')
        )
    ]
    await inline_query.answer(results)


@user_search_router.message(F.text == "💉 Shifokor sohasi bo'yicha qidirish")
async def search_doctor(message: types.Message):
    pass


@user_search_router.message(F.text == "🚶‍ Eng yaqin klinikalar ro'yxatini chiqarish")
async def nearest_clinics(message: types.Message):
    pass


@user_search_router.message(F.text == "📍 Manzil bo'yicha qidirish")
async def search_address(message: types.Message):
    pass
