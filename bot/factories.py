from bot.commands.help_menu import HelpMenuCommand
from bot.commands.dice import DiceCommand
from bot.commands.notebook import NotebookCommand
from bot.commands.currency import CurrencyCommand
from bot.commands.iam import IAmCommand
from bot.commands.temperature import TemperatureCommand
from bot.commands.some import SomeCommand
from bot.commands import COMMAND_CLASSES



# Factory pattern: фабрика для створення команд за ключовим словом
class CommandFactory:
    commands_map = COMMAND_CLASSES.copy()
    commands_map["/help"] = HelpMenuCommand

    @staticmethod
    def create_command(command_name):
        CommandClass = CommandFactory.commands_map.get(command_name)
        if CommandClass:
            return CommandClass()
        return None
