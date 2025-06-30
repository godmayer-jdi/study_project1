from typing import Any, Dict, List


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Функция выбирает из списка только те операции, у которых 'state' равен нужному значению.

    Параметр data: список словарей с операциями
    Параметр state: состояние для фильтрации, по умолчанию 'EXECUTED'
    return: новый список с отфильтрованными операциями
    """
    result = []
    for item in data:
        if "state" in item and item["state"] == state:
            result.append(item)
    return result


def sort_by_date(data: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """
    Функция сортирует список операций по дате.

    Параметр data: список словарей с операциями
    Параметр descending: если True — сортировка от новых к старым, иначе наоборот
    return: новый отсортированный список
    """
    return sorted(data, key=lambda x: x.get("date", ""), reverse=descending)
