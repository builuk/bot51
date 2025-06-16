from bot.base import BotCommand, CommandStrategy

info = "Check temperature"

class TemperatureStrategy(CommandStrategy):
    def handle(self, text, chat_id, user_id):
        # Просто заглушка
        return "25 degree celsius"

class TemperatureCommand(BotCommand):
    def __init__(self):
        self.strategy = TemperatureStrategy()

    def execute(self, text, chat_id, user_id):
        return self.strategy.handle(text, chat_id, user_id)
