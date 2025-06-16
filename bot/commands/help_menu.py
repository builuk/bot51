import os
import importlib
import inspect
from bot.base import BotCommand, CommandStrategy

class HelpMenuStrategy(CommandStrategy):
    def handle(self, text, chat_id, user_id):
        # Генеруємо команди прямо тут
        commands_dir = os.path.dirname(__file__)
        command_names = []
        for file in os.listdir(commands_dir):
            if file.endswith(".py") and file not in ("__init__.py", "help_menu.py", "role.py"):
                command_names.append(f"/{file[:-3]}")
        command_names.append("/help")



        return f"This is help menu. Available commands:\n {'\n'.join(sorted(command_names))}"

class HelpMenuCommand(BotCommand):
    def __init__(self):
        self.strategy = HelpMenuStrategy()

    def execute(self, text, chat_id, user_id):
        return self.strategy.handle(text, chat_id, user_id)