from aiogram import Router, types, F

from aiogram.fsm.context import FSMContext

from handlers.users.uz.start import uz_main_keyboard
from keyboards.inline.user_inline_buttons import search_in_inline_mode
from states.user_states import UserSearchUz

router = Router()

uz_search_ibuttons = search_in_inline_mode(
    search="Qidirish", back_text="Ortga", back_callback="back_search_uz"
)


async def search_text(message: types.Message, text: str, state: FSMContext, state_):
    await message.answer(
        text=f"🔎 <b>Qidirish</b> tugmasini bosib chiqarilgan ro'yxatdan kerakli {text} tanlashingiz yoki matn "
             f"kiritib kerakli natijani olishingiz mumkin.",
        reply_markup=uz_search_ibuttons
    )
    await state.set_state(state_)


@router.message(F.text == "⬅️ Ortga")
async def back_main_menu(message: types.Message):
    await message.answer(
        text="Bosh sahifa", reply_markup=uz_main_keyboard
    )


@router.message(F.text == "🏥 Klinika bo'yicha qidirish")
async def uz_search_clinics(message: types.Message, state: FSMContext):
    await search_text(
        message=message, text="klinikani", state=state, state_=UserSearchUz.clinics
    )


@router.message(F.text == "💧 Hizmat turi bo'yicha qidirish")
async def uz_search_services(message: types.Message, state: FSMContext):
    await search_text(
        message=message, text="hizmat turini", state=state, state_=UserSearchUz.services
    )


@router.message(F.text == "💉 Shifokor sohasi bo'yicha qidirish")
async def uz_search_doctors(message: types.Message, state: FSMContext):
    await search_text(
        message=message, text="shifokorni", state=state, state_=UserSearchUz.doctors
    )


@router.message(F.text == "🚶‍ Eng yaqin klinikalar")
async def uz_search_nearest_clinics(message: types.Message):
    pass


@router.message(F.text == "📍 Hudud bo'yicha qidirish")
async def uz_search_region(message: types.Message):
    pass
