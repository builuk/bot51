from bot.base import BotCommand, CommandStrategy

class CurrencyStrategy(CommandStrategy):
    def handle(self, text, chat_id, user_id):
        # Просто заглушка
        return "1 USD = 40 UAH (mocked data)"

class CurrencyCommand(BotCommand):
    def __init__(self):
        self.strategy = CurrencyStrategy()

    def execute(self, text, chat_id, user_id):
        return self.strategy.handle(text, chat_id, user_id)
