from bot.base import BotCommand, CommandStrategy

class ShutdownStrategy(CommandStrategy):
    def handle(self, text, chat_id, user_id):
        # Можна тут повертати спец. маркер
        return "__SHUTDOWN__"

class ShutdownCommand(BotCommand):
    def __init__(self):
        self.strategy = ShutdownStrategy()

    def execute(self, text, chat_id, user_id):
        return self.strategy.handle(text, chat_id, user_id)
