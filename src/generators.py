from typing import List, Dict, Iterator, Any

def filter_by_currency(transactions: List[Dict[str, Any]], currency_code: str) -> Iterator[Dict[str, Any]]:
    """
    Генератор, который поочередно возвращает транзакции с заданной валютой.
    """
    for transaction in transactions:
        # Проверяем, что валюта есть и совпадает с нужной
        if (
            "operationAmount" in transaction and
            "currency" in transaction["operationAmount"] and
            "code" in transaction["operationAmount"]["currency"] and
            transaction["operationAmount"]["currency"]["code"] == currency_code
        ):
            yield transaction
def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """Генератор, который поочередно возвращает описание каждой транзакции."""
    for transaction in transactions:
        yield transaction.get("description", "")
def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генератор номеров карт в формате XXXX XXXX XXXX XXXX.
    Генерирует номера от start до stop (не включая stop) """
    for num in range(start, stop):
        card_str = str(num).zfill(16)  # дополняем нулями слева до 16 символов
        formatted = f"{card_str[0:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:16]}"
        yield formatted