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


@user_search_router.inline_query()
async def search_inline_mode(inline_query: types.InlineQuery):
    # results = [
    #     types.InlineQueryResultCachedPhoto(
    #         id="005",
    #         photo_file_id="https://clinics.uz/uzb/components/com_mtree/img/listings/s/x2045.jpg",
    #         thumbnail_url="https://clinics.uz/uzb/components/com_mtree/img/listings/s/x2045.jpg",
    #         caption="<b>Mukammal Telegram bot</b> kursi."
    #     ),
    #     types.InlineQueryResultPhoto(
    #         id="006",
    #         photo_url="https://i1.wp.com/mohirdev.uz/wp-content/uploads/Anvar-aka-python.png",
    #         thumbnail_url="https://i1.wp.com/mohirdev.uz/wp-content/uploads/Anvar-aka-python.png",
    #         caption="<b>Python Dasturlash Asoslari</b> kursi."
    #     ),
    #     types.InlineQueryResultVideo(
    #         id="007",
    #         video_url="https://streamable.com/ryeff4",
    #         caption="Million dolarlik g'oya",
    #         description="Go'yalarning asl bahosi",
    #         title="Million 💲 g'oya ",
    #         thumbnail_url="https://i.imgur.com/bY2XasE.png",
    #         mime_type="video/mp4"
    #     )
    # ]
    # clinics = await db.select_all_clinics()
    # inline_result_clinics = []
    # for clinic in clinics:
    #     inline_result_clinics.append(types.InlineQueryResultCachedPhoto(
    #         id=str(clinic['id']),
    #         photo_file_id=clinic['image'],
    #         title="title title title title title title title title title title title ",
    #         description="description description description description description description description",
    #         caption="caption"
    #     )
    #     )
    await inline_query.answer(
        results=[
            types.InlineQueryResultPhoto(
                id="005",
                title="title of the Telegram bot",
                description="Anvar Narzullayev darslari",
                caption="<b>Mukammal Telegram bot</b> kursi. ga",
                photo_url="https://i1.wp.com/mohirdev.uz/wp-content/uploads/Telegram-bot.png",
                thumbnail_url="https://i1.wp.com/mohirdev.uz/wp-content/uploads/Telegram-bot.png",
                parse_mode="HTML"
            ),
            types.InlineQueryResultPhoto(
                id="006",
                title="Dasturlash asoslari",
                description="Anvar Narzullayev darslari",
                caption="<b>Python Dasturlash Asoslari</b> kursi.",
                parse_mode="HTML",
                photo_url="https://i1.wp.com/mohirdev.uz/wp-content/uploads/Anvar-aka-python.png",
                thumbnail_url="https://i1.wp.com/mohirdev.uz/wp-content/uploads/Anvar-aka-python.png"
            ),
            types.InlineQueryResultVideo(
                id="007",
                video_url="https://streamable.com/ryeff4",
                caption="Million dolarlik g'oya",
                description="Go'yalarning asl bahosi",
                title="Million 💲 g'oya ",
                thumbnail_url="https://i.imgur.com/bY2XasE.png",
                mime_type="video/mp4",  # video/mp4 yoki text/html
            ),
        ],
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
