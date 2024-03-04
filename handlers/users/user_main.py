from aiogram import Router, types, F

user_main_router = Router()


@user_main_router.message(F.text == "📱 Mutaxassis bilan bog'lanish")
async def communicate_to_specialist(message: types.Message):
    await message.answer(
        text="Mutaxassis turini tanlang"  # mutaxassislar ro'yxati dbdan olinib keyboard shaklida qaytariladi
    )
