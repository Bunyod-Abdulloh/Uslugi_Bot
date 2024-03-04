from aiogram.fsm.state import StatesGroup, State


class UserCommunicate(StatesGroup):
    complaint = State()

