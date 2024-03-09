from aiogram import Router, types, F
from aiogram.filters import StateFilter

from handlers.users.uz.start import uz_main_keyboard
from loader import db, bot
from states.user_states import UserSearchUz

user_search_router = Router()

services = ['Akusherlik', 'Algologiya', 'Allergologiya', 'Muqobil tibbiyot',
            'Tahlillar', 'Angiologiya', 'Andrologiya', 'Anezteziologiya va reanimatologiya']


@user_search_router.message(F.text == "salom")
async def get_photo_id(message: types.Message):
    await message.answer(
        text="GIF image",
        link_preview_options=types.LinkPreviewOptions(
            url="CgACAgIAAxkBAAIDMWXp_Nv-2TOo5t2IWMya5t4y0E2BAAL6DgAClctBSLqqKy7uhDekNAQ"
        )
    )


@user_search_router.callback_query(F.data == "back_main_menu")
async def back_main_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(
        text="Bosh sahifa", reply_markup=uz_main_keyboard
    )


# @user_search_router.inline_query(F.data == "klinika")
# async def search_clinics(inline_query: types.InlineQuery):
#     print(f"{user_search_router} klinika search")
#     query_ = inline_query.query
#     clinics = await db.select_all_clinics()
#     result_all = []
#     result_search = []
#     if len(query_) > 0:
#         sql_like = await db.select_clinic_like(text=query_)
#         for clinic in sql_like:
#             result_search.append(
#                 types.InlineQueryResultArticle(
#                     id=str(clinic['id']), title=clinic['name'],
#                     description=f"Manzil: {clinic['address']}\nIsh vaqti: {clinic['work_time']}",
#                     input_message_content=types.InputTextMessageContent(
#                         message_text=f"Hello, this is result {clinic['id']}", parse_mode="HTML"
#                     )
#                 )
#             )
#         await inline_query.answer(
#             results=result_search
#         )
#     else:
#         for clinic in clinics:
#             result_all.append(
#                 types.InlineQueryResultArticle(
#                     id=str(clinic['id']), title=clinic['name'],
#                     description=f"Manzil: {clinic['address']}\nIsh vaqti: {clinic['work_time']}",
#                     input_message_content=types.InputTextMessageContent(
#                         message_text=f"Hello, this is result {clinic['id']}", parse_mode="HTML"
#                     )
#                 )
#             )
#         await inline_query.answer(results=result_all, switch_pm_parameter="Parameter",
#                                   switch_pm_text="Pastdan tepaga suring", cache_time=1
#                                   )


# @user_search_router.callback_query(F.data == "shifoxona")
@user_search_router.inline_query(F.query == "hizmat")
async def search_services(inline_query: types.InlineQuery):
    print(inline_query)
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


@user_search_router.inline_query()
async def search_doctors(inline_query: types.InlineQuery):
    print("Salom 3")


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

# @user_search_router.inline_query(F.text == "hizmatlar")
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

# @user_search_router.message(F.text == "💉 Shifokor sohasi bo'yicha qidirish")
# async def search_doctor(message: types.Message):
#     pass
#
#
# @user_search_router.message(F.text == "🚶‍ Eng yaqin klinikalar ro'yxatini chiqarish")
# async def nearest_clinics(message: types.Message):
#     pass
#
#
# @user_search_router.message(F.text == "📍 Manzil bo'yicha qidirish")
# async def search_address(message: types.Message):
#     pass
