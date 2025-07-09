import pytest
from src.bank_operations import process_bank_search, process_bank_operations

sample_data = [
    {"description": "Перевод на карту", "status": "EXECUTED"},
    {"description": "Оплата услуг", "status": "CANCELED"},
    {"description": "Перевод организации", "status": "EXECUTED"},
    {"description": "Открытие вклада", "status": "PENDING"},
]

def test_process_bank_search_found():
    result = process_bank_search(sample_data, "перевод")
    assert len(result) == 2
    assert all("перевод" in item["description"].lower() for item in result)

def test_process_bank_search_not_found():
    result = process_bank_search(sample_data, "неизвестно")
    assert result == []

def test_process_bank_operations_counts():
    categories = ["перевод", "оплата", "вклад"]
    counts = process_bank_operations(sample_data, categories)
    assert counts["перевод"] == 2
    assert counts["оплата"] == 1
    assert counts["вклад"] == 1
