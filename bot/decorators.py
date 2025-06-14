import functools

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
        user_id = args[3]
        if user_id == 1:  # admin (умовно)
            return func(*args, **kwargs)
        return "Unauthorized"
    return wrapper
