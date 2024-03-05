from aiogram import Router, types, F
from filters.chat_type_filter import ChatTypeFilter
from keyboards.inline.user_inline_buttons import select_gender_communicate

user_main_router = Router()
user_main_router.message.filter(ChatTypeFilter(['private']))


@user_main_router.message(F.text == "📱 Shifokor bilan bog'lanish")
async def communicate_to_specialist(message: types.Message):
    await message.answer(
        text="Tugmalardan birini tanlang",
        reply_markup=select_gender_communicate(
            man_text="Erkak shifokor", man_callback="complaintuz_Erkak",
            woman_text="Ayol shifokor", woman_callback="complaintuz_Ayol",
            all_text="Ahamiyati yo'q", all_callback="complaintuz_Ahamiyatsiz",
            back_text="Ortga", back_callback="back_complaintuz"
        )
    )
