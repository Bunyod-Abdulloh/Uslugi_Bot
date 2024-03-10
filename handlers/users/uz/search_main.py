from aiogram import Router, types, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from handlers.users.uz.start import uz_main_keyboard
from keyboards.inline.user_inline_buttons import search_in_inline_mode
from loader import db, bot
from states.user_states import UserSearchUz

search_router = Router()

services = ['Akusherlik', 'Algologiya', 'Allergologiya', 'Muqobil tibbiyot',
            'Tahlillar', 'Angiologiya', 'Andrologiya', 'Anezteziologiya va reanimatologiya']

search_ibuttons = search_in_inline_mode(
    search="Qidirish", back_text="Ortga", back_callback="back_search_uz"
)


@search_router.message(F.text == "⬅️ Ortga")
async def back_main_menu(message: types.Message):
    await message.answer(
        text="Bosh sahifa", reply_markup=uz_main_keyboard
    )


@search_router.message(F.text == "🏥 Klinika bo'yicha qidirish")
async def uz_search_clinics(message: types.Message, state: FSMContext):
    await message.answer(
        text="🔎 <b>Qidirish</b> tugmasini bosib chiqarilgan ro'yxatdan kerakli klinikani tanlashingiz yoki matn "
             "kiritib kerakli natijani olishingiz mumkin.",
        reply_markup=search_ibuttons
    )
    await state.set_state(UserSearchUz.clinics)


@search_router.message(F.text == "💧 Hizmat turi bo'yicha qidirish")
async def uz_search_services(message: types.Message):
    pass


@search_router.message(F.text == "💉 Shifokor sohasi bo'yicha qidirish")
async def uz_search_doctors(message: types.Message):
    pass


@search_router.message(F.text == "🚶‍ Eng yaqin klinikalar")
async def uz_search_nearest_clinics(message: types.Message):
    pass


@search_router.message(F.text == "📍 Hudud bo'yicha qidirish")
async def uz_search_region(message: types.Message):
    pass


@search_router.inline_query(F.query == "hizmat")
async def search_services(inline_query: types.InlineQuery):
    print("hizmat search")
    result_all = []
    clinics = await db.select_all_clinics()
    for clinic in clinics:
        result_all.append(
            types.InlineQueryResultArticle(
                id=str(clinic['id']), title=clinic['name'],
                description=f"Manzil: {clinic['address']}\nIsh vaqti: {clinic['work_time']}",
                input_message_content=types.InputTextMessageContent(
                    message_text=f"Hello, this is result {clinic['id']}", parse_mode="HTML"
                )
            )
        )
    await inline_query.answer(results=result_all, switch_pm_parameter="Parameter",
                              switch_pm_text="Pastdan tepaga suring", cache_time=1
                              )


# @search_router.inline_query()
# async def search_doctors(inline_query: types.InlineQuery):
#     print("Salom 3")


        #     if '"' in query_:
    #         query_ = query_.replace('"', '')
    #     if query_ in clinic['name'].lower():
    #         result_all = [types.InlineQueryResultArticle(
    #             id=str(clinic['id']), title=clinic['name'],
    #             description=f"Manzil: {clinic['address']}\nIsh vaqti: {clinic['work_time']}",
    #             input_message_content=types.InputTextMessageContent(
    #                 message_text=f"Hello, this is result {clinic['id']}", parse_mode="HTML"
    #             )
    #         )]
    # await inline_query.answer(
    #     results=result, cache_time=1
    # )
    #     else:
    #
    #

# @search_router.inline_query(F.text == "hizmatlar")
# async def search_services(query: types.InlineQuery):
#     print("services qidirish")
#     result_services = []
#     c = 0
#     for clinic in services:
#         c += 1
#         result_services.append(
#             types.InlineQueryResultArticle(
#                 type="article",
#                 id=str(c),
#                 title=clinic,
#                 description=f"Manzil: {clinic}\nIsh vaqti: {clinic}",
#                 input_message_content=types.InputTextMessageContent(
#                     message_text=f"Hello, this is result {clinic}",
#                     parse_mode="HTML"
#                 )
#             )
#         )
#     await query.answer(results=result_services,
#                        switch_pm_parameter="Qidirish", switch_pm_text="Pastdan tepaga suring"
#                        )

# @search_router.message(F.text == "💉 Shifokor sohasi bo'yicha qidirish")
# async def search_doctor(message: types.Message):
#     pass
#
#
# @search_router.message(F.text == "🚶‍ Eng yaqin klinikalar ro'yxatini chiqarish")
# async def nearest_clinics(message: types.Message):
#     pass
#
#
# @search_router.message(F.text == "📍 Manzil bo'yicha qidirish")
# async def search_address(message: types.Message):
#     pass
