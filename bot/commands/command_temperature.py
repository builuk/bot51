from bot.base import BotCommand, CommandStrategy
from bot.helper.temperature_helper import TemperatureHelper


class TemperatureStrategy(CommandStrategy):
    def handle(self, text, chat_id, user_id):
        # Видаляємо команду `/temperature` і пробіли
        if text.startswith('/temperature'):
            text = text[len('/temperature'):].strip()

        # Значення за замовчуванням
        city = 'Odesa'
        units = 'metric'

        if text:
            parts = text.split()
            if len(parts) >= 1:
                city = parts[0]
            if len(parts) >= 2:
                units = parts[1]

        weather = TemperatureHelper(units=units)
        weather.fetch_weather(city)
        return f"{city}: {weather.get_temperature()}"


class TemperatureCommand(BotCommand):
    info = "Check the current temperature in a city (usage: <city> <units>)"

    def __init__(self):
        self.strategy = TemperatureStrategy()

    def execute(self, text, chat_id, user_id):
        return self.strategy.handle(text, chat_id, user_id)