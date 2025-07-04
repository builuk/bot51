from bot.base import BotCommand, CommandStrategy

class AgdevStrategy(CommandStrategy):
    def handle(self, text, chat_id, user_id):
        # Корисне навантаження
        return f"AGdev ID: {user_id}, chat: {chat_id}"

class AgdevCommand(BotCommand):
    def __init__(self):
        self.strategy = AgdevStrategy()

    def execute(self, text, chat_id, user_id):
        return self.strategy.handle(text, chat_id, user_id)
