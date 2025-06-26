from bot.base import BotCommand, CommandStrategy
import random

class DiceStrategy(CommandStrategy):
    def handle(self, text, chat_id, user_id):
        return f"🎲 You rolled: {random.randint(1, 6)}"

class DiceCommand(BotCommand):
    def __init__(self):
        self.strategy = DiceStrategy()

    def execute(self, text, chat_id, user_id):
        return self.strategy.handle(text, chat_id, user_id)
