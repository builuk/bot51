from bot.base import BotCommand, CommandStrategy

class DevStrategy(CommandStrategy):
    def handle(self, text, chat_id, user_id):
        # Корисне навантаження
        return f"Dev ID: {user_id}, chat: {chat_id}"

class DevCommand(BotCommand):
    def __init__(self):
        self.strategy = DevStrategy()

    def execute(self, text, chat_id, user_id):
        return self.strategy.handle(text, chat_id, user_id)
