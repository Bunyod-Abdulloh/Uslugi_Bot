from aiogram import Router, types, F
from filters.chat_type_filter import ChatTypeFilter

user_main_router = Router()
user_main_router.message.filter(ChatTypeFilter(['private']))


@user_main_router.message(F.text == "📱 Mutaxassis bilan bog'lanish")
async def communicate_to_specialist(message: types.Message):
    await message.answer(
        text="Mutaxassis turini tanlang"  # mutaxassislar ro'yxati dbdan olinib keyboard shaklida qaytariladi
    )


@user_main_router.message(F.photo)
async def get_photo(message: types.Message):
    print(message.photo[-1].file_id)
