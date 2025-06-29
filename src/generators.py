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

