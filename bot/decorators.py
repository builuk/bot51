import functools
from dotenv import load_dotenv
import os
from bot.roles.role_helper import check_command_access


# Decorator pattern: логування всіх команд
def log_command(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        text, chat_id, user_id = args[1:4]
        print(f"[LOG] Executing command for user {user_id} in chat {chat_id}: {text}")
        return func(*args, **kwargs)

    return wrapper


# Decorator pattern: перевірка авторизації (демо)
def require_auth(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        load_dotenv()
        admin_id = os.getenv("ADMIN_ID")
        command = args[1]
        user_id = args[3]
        if int(user_id) == int(admin_id):
            return func(*args, **kwargs)
        # Тут відбувається перевірка. Якщо команда не додана в список пускає далі
        access = check_command_access(command, int(user_id))
        if access is True:
            return func(*args, **kwargs)
        else:
            return access

    return wrapper
