import requests
from bot.base import BotCommand, CommandStrategy

class CurrencyStrategy(CommandStrategy):
    def fetch_rate(self, valcode='USD'):
        """Отримати курс valcode до гривні через API НБУ"""
        try:
            url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={valcode}&json"
            resp = requests.get(url, timeout=5)
            resp.raise_for_status()
            data = resp.json()
            if data and isinstance(data, list) and "rate" in data[0]:
                rate = data[0]["rate"]
                return rate
            return None
        except Exception as e:
            return None

    def handle(self, text, chat_id, user_id):
        # /currency USD  або просто /currency
        valcode = 'USD'
        if text.strip().upper().startswith('/CURRENCY'):
            parts = text.strip().split()
            if len(parts) > 1:
                valcode = parts[1].upper()
        rate = self.fetch_rate(valcode)
        if rate:
            return f"1 {valcode} = {rate:.2f} UAH (НБУ)"
        else:
            return f"Не вдалося отримати курс для {valcode}"

class CurrencyCommand(BotCommand):
    def __init__(self):
        self.strategy = CurrencyStrategy()

    def execute(self, text, chat_id, user_id):
        return self.strategy.handle(text, chat_id, user_id)
