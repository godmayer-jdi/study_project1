import pytest

from src.bank_operations import process_bank_operations, process_bank_search

sample_data = [
    {"description": "Перевод на карту", "status": "EXECUTED"},
    {"description": "Оплата услуг", "status": "CANCELED"},
    {"description": "Перевод организации", "status": "EXECUTED"},
    {"description": "Открытие вклада", "status": "PENDING"},
]


@pytest.mark.parametrize(
    "search_term, expected_count",
    [
        ("перевод", 2),
        ("неизвестно", 0),
    ],
)
def test_process_bank_search(search_term: str, expected_count: int) -> None:
    result = process_bank_search(sample_data, search_term)
    assert len(result) == expected_count
    if expected_count > 0:
        assert all(search_term in item["description"].lower() for item in result)


def test_process_bank_operations_counts() -> None:
    categories = ["перевод", "оплата", "вклад"]
    counts = process_bank_operations(sample_data, categories)
    assert counts["перевод"] == 2
    assert counts["оплата"] == 1
    assert counts["вклад"] == 1
