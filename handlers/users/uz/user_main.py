from aiogram import Router, types, F
from filters.chat_type_filter import ChatTypeFilter
from keyboards.default.user_default_buttons import user_search_cbuttons
from keyboards.inline.user_inline_buttons import select_gender_communicate

user_main_router = Router()
user_main_router.message.filter(ChatTypeFilter(['private']))

uz_select_gender_ibuttons = select_gender_communicate(
    man_text="Erkak shifokor", man_callback="complaintuz_Erkak",
    woman_text="Ayol shifokor", woman_callback="complaintuz_Ayol",
    all_text="Ahamiyati yo'q", all_callback="complaintuz_Ahamiyatsiz", back_text="Ortga", back_callback="back_mainuz"
)

uz_search_dbuttons = user_search_cbuttons(
    search_clinic="Klinika bo'yicha qidirish", search_doctor="Shifokor sohasi bo'yicha qidirish",
    search_address="Eng yaqin klinikalar ro'yxatini chiqarish", nearest_clinics="Manzil bo'yicha qidirish",
    back_main_menu="Bosh sahifaga qaytish"
)


@user_main_router.message(F.text == "📱 Shifokor bilan bog'lanish")
async def communicate_to_specialist(message: types.Message):
    await message.answer(
        text="Tugmalardan birini tanlang",
        reply_markup=uz_select_gender_ibuttons
    )


@user_main_router.message(F.text == "🔍 Qidirish")
async def search_(message: types.Message):
    await message.answer(
        text="Quyidagilardan birini tanlang",
        reply_markup=uz_search_dbuttons
    )
