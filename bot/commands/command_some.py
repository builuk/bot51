from bot.base import BotCommand, CommandStrategy

class SomeStrategy(CommandStrategy):
    def handle(self, text, chat_id, user_id):
        # Просто заглушка
        return "25 degree celsius"

class SomeCommand(BotCommand):
    def __init__(self):
        self.strategy = SomeStrategy()

    def execute(self, text, chat_id, user_id):
        return self.strategy.handle(text, chat_id, user_id)
