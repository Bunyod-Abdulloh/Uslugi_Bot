from aiogram import Router

from filters.private_chat import ChatPrivateFilter


def setup_routers() -> Router:
    from .users.uz import start, communicate, main, search_main, search_clinics, search_data
    from .errors import error_handler

    router = Router()

    # Agar kerak bo'lsa, o'z filteringizni o'rnating
    start.router.message.filter(ChatPrivateFilter(chat_type=["private"]))

    router.include_routers(start.router, error_handler.router, communicate.router, main.router,
                           search_main.router)
    router.include_routers(search_clinics.router, search_data.router)

    return router
