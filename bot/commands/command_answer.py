from bot.base import BotCommand, CommandStrategy
import os
from dotenv import load_dotenv

class AnswerStrategy(CommandStrategy):
    def handle(self, text, chat_id, user_id):
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")

        if text.startswith('/answer'):
            text = text[:8]

        from openai import OpenAI

        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Ти короткий і чіткий помічник."},
                {"role": "user", "content": f"{text}"},
            ],
            max_tokens=100,
            temperature=0.5,
        )

        return response.choices[0].message.content

class AnswerCommand(BotCommand):
    def __init__(self):
        self.strategy = AnswerStrategy()

    def execute(self, text, chat_id, user_id):
        return self.strategy.handle(text, chat_id, user_id)
