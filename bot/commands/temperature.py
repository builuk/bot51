from bot.base import BotCommand, CommandStrategy
from bot.helper.temperature_helper import TemperatureHelper

class TemperatureStrategy(CommandStrategy):
    def handle(self, text, chat_id, user_id):
        weather = TemperatureHelper()
        weather.run(q='Odesa', units='metric')
        temperature = weather.temperature()
        return temperature


class TemperatureCommand(BotCommand):
    info = "Check the current temperature"

    def __init__(self):
        self.strategy = TemperatureStrategy()

    def execute(self, text, chat_id, user_id):
        return self.strategy.handle(text, chat_id, user_id)
