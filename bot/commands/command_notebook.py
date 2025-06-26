from bot.base import BotCommand, CommandStrategy

class NotebookStrategy(CommandStrategy):
    notes = {}

    def handle(self, text, chat_id, user_id):
        text = text[10:] # костиль, щоб прибрати '/notebook ' з тексту
        if user_id not in self.notes:
            self.notes[user_id] = []
        if text.startswith("add "):
            note = text[4:]
            self.notes[user_id].append(note)
            return f"Note added: {note}"
        if text == "list":
            return "\n".join(self.notes[user_id]) if self.notes[user_id] else "No notes."
        return "Unknown notebook command."

class NotebookCommand(BotCommand):
    def __init__(self):
        self.strategy = NotebookStrategy()

    def execute(self, text, chat_id, user_id):
        return self.strategy.handle(text, chat_id, user_id)
