# Chain of Responsibility pattern: Ланцюг обробників
class Handler:
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, text, chat_id, user_id):
        if self._next_handler:
            return self._next_handler.handle(text, chat_id, user_id)
        return None

# Конкретний обробник — для прикладу: фільтрування мату
class CensorshipHandler(Handler):
    def handle(self, text, chat_id, user_id):
        if "badword" in text:
            return "Message blocked due to bad language!"
        return super().handle(text, chat_id, user_id)

# Ще один — логування
class LoggingHandler(Handler):
    def handle(self, text, chat_id, user_id):
        print(f"[Handler LOG] user={user_id}, chat={chat_id}, text={text}")
        return super().handle(text, chat_id, user_id)
