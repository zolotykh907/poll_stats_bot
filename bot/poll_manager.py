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

        self.polls[poll_message.poll.id] = {
            "question": question,
            "options": options,
            "answers": {}
        }

        return poll_message
    

    def save_poll_answer(self, poll_answer):
        poll_id = poll_answer.poll_id
        user_id = poll_answer.user.id
        option_ids = poll_answer.option_ids

        # if poll_id not in self.polls:
        #     self.polls[poll_id] = {}

        self.polls[poll_id]['answers'][user_id] = {}
        self.polls[poll_id]['answers'][user_id]['option_ids'] = option_ids
        self.polls[poll_id]['answers'][user_id]['user'] = poll_answer.user.full_name
        
        print(self.polls)