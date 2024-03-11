from aiogram.fsm.state import StatesGroup, State


class UserCommunicateUz(StatesGroup):
    complaint = State()


class UserSearchUz(StatesGroup):
    clinics = State()
    services = State()
    doctors = State()
    address = State()
    nearest_clinics = State()

