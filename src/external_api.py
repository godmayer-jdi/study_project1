import os
import requests
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные окружения из .env

API_KEY = os.getenv("EXCHANGE_API_KEY")
API_URL = "https://api.apilayer.com/exchangerates_data/convert"

def convert_transaction_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Возвращает сумму транзакции в рублях.
    Если валюта RUB — возвращает сумму.
    Если валюта USD или EUR — конвертирует через внешний API.
    """
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    if currency in ("USD", "EUR"):
        params = {
            "from": currency,
            "to": "RUB",
            "amount": amount
        }
        headers = {
            "apikey": API_KEY
        }
        response = requests.get(API_URL, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        return float(data.get("result", 0.0))

    # Если валюта неизвестна — возвращаем 0.0
    return 0.0
