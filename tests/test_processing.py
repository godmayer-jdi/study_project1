import pytest
from src.processing import filter_by_state, sort_by_date

# Фикстура с тестовыми данными
@pytest.fixture
def sample_data():
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-05-01T10:00:00'},
        {'id': 2, 'state': 'CANCELED', 'date': '2023-04-01T10:00:00'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-06-01T10:00:00'},
        {'id': 4, 'state': 'PENDING', 'date': '2023-03-01T10:00:00'},
        {'id': 5, 'state': 'EXECUTED', 'date': '2023-05-01T09:00:00'},
    ]


