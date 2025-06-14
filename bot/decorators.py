import functools
from dotenv import load_dotenv
import os

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
        user_id = args[3]
        if user_id == admin_id:
            return func(*args, **kwargs)
        return "Unauthorized"
    return wrapper
