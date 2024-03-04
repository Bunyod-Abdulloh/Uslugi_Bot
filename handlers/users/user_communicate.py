from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from loader import db
from states.user_states import UserCommunicate

user_communicate_router = Router()


@user_communicate_router.callback_query(F.data.contains("communicate_"))
async def communicate_one(call: types.CallbackQuery, state: FSMContext):
    specialist = call.data.split("_")[1]
    await state.update_data(
        get_doctor=specialist
    )
    await db.add_complaint_user(
        telegram_id=call.from_user.id, get_doctor=specialist
    )
    await call.message.edit_text(
        text="Shikoyatingizni kiriting"
    )
    await state.set_state(UserCommunicate.complaint)


@user_communicate_router.message(UserCommunicate.complaint)
async def get_complaint(message: types.Message, state: FSMContext):
    pass


