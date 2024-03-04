from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from states.user_states import UserCommunicate

user_communicate_router = Router()


@user_communicate_router.callback_query(F.data.contains("communicate_"))
async def communicate_one(call: types.CallbackQuery, state: FSMContext):
    specialist = call.data.split("_")[1]
    await state.update_data(
        get_specialist=specialist
    )
    await call.message.answer(
        text="Shikoyatingizni kiriting"
    )
    await state.set_state(UserCommunicate.complaint)


@user_communicate_router.message(UserCommunicate.complaint)
async def get_complaint(message: types.Message, state: FSMContext):
    pass


