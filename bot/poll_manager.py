class PollManager:
    def __init__(self, bot):
        self.bot = bot
        self.polls = {}

    async def create_poll(self, chat_id, question, options):
        poll_message = await self.bot.send_poll(
            chat_id=chat_id,
            question=question,
            options=options,
            is_anonymous=False
        )

        return poll_message