from bot.commands.command_currency import CurrencyCommand

def test_currency_command_execute():
    cmd = CurrencyCommand()
    result = cmd.execute("USD", 1, 2)
    assert isinstance(result, str)
