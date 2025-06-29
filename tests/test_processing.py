import pytest
from typing import List, Dict, Any
from src.processing import filter_by_state, sort_by_date


# Фикстура с тестовыми данными
@pytest.fixture
def sample_data() -> List[Dict[str, Any]]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-05-01T10:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2023-04-01T10:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-06-01T10:00:00"},
        {"id": 4, "state": "PENDING", "date": "2023-03-01T10:00:00"},
        {"id": 5, "state": "EXECUTED", "date": "2023-05-01T09:00:00"},
    ]


# Тесты для filter_by_state
@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", [1, 3, 5]),
        ("CANCELED", [2]),
        ("PENDING", [4]),
        ("NON_EXISTENT", []),
    ],
)
def test_filter_by_state(sample_data: List[Dict[str, Any]], state: str, expected_ids: List[int]) -> None:
    filtered = filter_by_state(sample_data, state)
    filtered_ids = [item["id"] for item in filtered]
    assert filtered_ids == expected_ids


# Тест для функции sort_by_date. Проверка сортировки по дате
def test_sort_by_date_descending(sample_data: List[Dict[str, Any]]) -> None:
    sorted_list = sort_by_date(sample_data, descending=True)
    dates = [item["date"] for item in sorted_list]
    assert dates == sorted(dates, reverse=True)


def test_sort_by_date_ascending(sample_data: List[Dict[str, Any]]) -> None:
    sorted_list = sort_by_date(sample_data, descending=False)
    dates = [item["date"] for item in sorted_list]
    assert dates == sorted(dates)


# Тест на нестандартные данные
def test_filter_by_state_empty_list() -> None:
    assert filter_by_state([], "EXECUTED") == []


def test_sort_by_date_empty_list() -> None:
    assert sort_by_date([], descending=True) == []


def test_sort_by_date_missing_date_key() -> None:
    data: List[Dict[str, Any]] = [{"id": 1}, {"id": 2, "date": "2023-01-01T00:00:00"}]
    sorted_list = sort_by_date(data)
    # Проверяем, что элементы без 'date' не вызывают ошибку и сортируются корректно
    assert sorted_list[-1]["id"] == 1  # Элемент без даты должен быть в конце при сортировке по убыванию
