import re
from collections import Counter
from typing import Any, Dict, List


def process_bank_search(data: List[Dict[str, Any]], search: str) -> List[Dict[str, Any]]:
    """
    Возвращает список операций, у которых в описании встречается строка поиска (регулярное выражение).

    Args:
        data: список словарей с операциями.
        search: строка для поиска в поле 'description'.

    Returns:
        Список словарей с операциями, где описание содержит строку поиска.
    """
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    filtered = [item for item in data if "description" in item and pattern.search(item["description"])]
    return filtered

def process_bank_operations(data: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций по категориям (по полю 'description').

    Args:
        data: список словарей с операциями.
        categories: список категорий (строк) для подсчёта.

    Returns:
        Словарь {категория: количество операций}.
    """
    descriptions = [item.get("description", "") for item in data]
    counter: Counter[str] = Counter()
    for category in categories:
        count = sum(1 for desc in descriptions if category.lower() in desc.lower())
        counter[category] = count
    return dict(counter)
