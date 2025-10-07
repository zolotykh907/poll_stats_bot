from aiogram import BaseMiddleware

from bot.poll_manager import PollManager


class PollManagerMiddleware(BaseMiddleware):
    def __init__(self, poll_manager: PollManager):
        super().__init__()
        self.poll_manager = poll_manager

    async def __call__(
        self, handler, event, data):
        data["poll_manager"] = self.poll_manager
        return await handler(event, data)
