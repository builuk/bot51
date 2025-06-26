from bot.commands.command_some import SomeCommand

def test_some_command_returns_static_text():
    command = SomeCommand()
    result = command.execute('/some', chat_id=123, user_id=456)
    assert result == "25 degree celsius"