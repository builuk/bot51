from bot.base import BotCommand, CommandStrategy

class IAmStrategy(CommandStrategy):
    def handle(self, text, chat_id, user_id):
        # Корисне навантаження
        return f"Your ID: {user_id}, chat: {chat_id}"

class IAmCommand(BotCommand):
    def __init__(self):
        self.strategy = IAmStrategy()

    def execute(self, text, chat_id, user_id):
        return self.strategy.handle(text, chat_id, user_id)
