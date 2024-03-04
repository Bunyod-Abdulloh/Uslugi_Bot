from aiogram import Router, types, F
from filters.chat_type_filter import ChatTypeFilter
from keyboards.inline import user_select_doctors_ibutton

user_main_router = Router()
user_main_router.message.filter(ChatTypeFilter(['private']))


@user_main_router.message(F.text == "📱 Mutaxassis bilan bog'lanish")
async def communicate_to_specialist(message: types.Message):
    await message.answer(
        text="Mutaxassis turini tanlang",
        reply_markup=user_select_doctors_ibutton().as_markup()
    )


@user_main_router.message(F.photo)
async def get_photo(message: types.Message):
    print(message.photo[-1].file_id)
