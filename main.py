from bot.core import TelegramBot
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    bot_token = os.getenv("TOKEN")
    bot = TelegramBot(bot_token)

    # Демонстрація: просто тестові виклики, те що потім можна використати для unit тестів
    # print(bot.handle_message("/help", 100, 1))
    # print(bot.handle_message("/dice", 100, 2))
    # print(bot.handle_message("/notebook add buy milk", 100, 2))
    # print(bot.handle_message("/notebook list", 100, 2))
    # print(bot.handle_message("/currency", 100, 1))
    # print(bot.handle_message("hello badword", 100, 2))  # буде заблоковано
    print(bot.handle_message("/weather", 123, 1111))

    bot.run()

if __name__ == "__main__":
    main()
