from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from loader import db, dp
from states.user_states import UserSearchUz

router = Router()
uz_back_search_router = Router()


@uz_back_search_router.callback_query(F.data == "back_search_uz")
async def back_search_uz(callback_query: types.CallbackQuery, state: FSMContext):
    await state.clear()
    print(callback_query.data)


@router.inline_query(UserSearchUz.clinics)
async def uz_clinics_one(inline_query: types.InlineQuery):
    query_ = inline_query.query
    clinics = await db.select_all_clinics()
    result_all = []
    result_search = []
    if len(query_) > 0:
        sql_like = await db.select_clinic_like(text=query_)
        for clinic in sql_like:
            result_search.append(
                types.InlineQueryResultArticle(
                    id=str(clinic['id']), title=clinic['name'],
                    description=f"Manzil: {clinic['address']}\nIsh vaqti: {clinic['work_time']}",
                    input_message_content=types.InputTextMessageContent(
                        message_text=f"Hello, this is result {clinic['id']}", parse_mode="HTML"
                    )
                )
            )
        await inline_query.answer(
            results=result_search
        )
    else:
        for clinic in clinics:
            result_all.append(
                types.InlineQueryResultArticle(
                    id=str(clinic['id']), title=clinic['name'],
                    description=f"Manzil: {clinic['address']}\nIsh vaqti: {clinic['work_time']}",
                    input_message_content=types.InputTextMessageContent(
                        message_text=f"Hello, this is result {clinic['id']}", parse_mode="HTML"
                    )
                )
            )
        await inline_query.answer(results=result_all, switch_pm_parameter="Parameter",
                                  switch_pm_text="Pastdan tepaga suring", cache_time=1
                                  )
