from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from filters.chat_type_filter import ChatTypeFilter
from keyboards.default.user_default_buttons import uz_user_search_cbuttons
from keyboards.inline.user_inline_buttons import select_gender_communicate, user_search_ibuttons
from states.user_states import UserSearchUz

user_main_router = Router()
user_main_router.message.filter(ChatTypeFilter(['private']))

uz_select_gender_ibuttons = select_gender_communicate(
    man_text="Erkak shifokor", man_callback="complaintuz_Erkak",
    woman_text="Ayol shifokor", woman_callback="complaintuz_Ayol",
    all_text="Ahamiyati yo'q", all_callback="complaintuz_Ahamiyatsiz", back_text="Ortga", back_callback="back_mainuz"
)

uz_search_cbuttons = uz_user_search_cbuttons(
    clinics="Klinika bo'yicha qidirish", services="Hizmat turi bo'yicha qidirish",
    doctors="Shifokor sohasi bo'yicha qidirish", nearest_clinics="Eng yaqin klinikalar",
    region="Hudud bo'yicha qidirish", back_main_menu="Ortga"
)


@user_main_router.message(F.text == "📱 Shifokor bilan bog'lanish")
async def communicate_to_specialist(message: types.Message):
    await message.answer(
        text="Tugmalardan birini tanlang",
        reply_markup=uz_select_gender_ibuttons
    )


@user_main_router.message(F.text == "🔍 Qidirish")
async def search_(message: types.Message, state: FSMContext):
    await message.answer(
        text="Qidiruv turini tanlang",
        reply_markup=uz_search_cbuttons
    )
