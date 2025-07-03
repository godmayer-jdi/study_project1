# Описание структуры транзакции через TypedDict (опционально, для более строгой типизации)
from typing import Any, Dict, List, Optional, TypedDict

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


class Currency(TypedDict):
    name: str
    code: str


class OperationAmount(TypedDict):
    amount: str
    currency: Currency


class Transaction(TypedDict, total=False):
    id: int
    state: str
    date: str
    operationAmount: OperationAmount
    description: Optional[str]
    from_: Optional[
        str
    ]  # 'from' — зарезервированное слово, поэтому можно использовать from_ и в коде обращаться через dict['from']
    to: Optional[str]


@pytest.fixture
def transactions() -> list[dict[str, str | dict[str, str | dict[str, str]] | int]]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


@pytest.mark.parametrize(
    "currency_code, expected_ids",
    [
        ("USD", [939719570, 142264268, 895315941]),
        ("RUB", [873106923, 594226727]),
        ("EUR", []),
    ],
)
def test_filter_by_currency(transactions: List[Dict[str, Any]], currency_code: str, expected_ids: List[int]) -> None:
    result = list(filter_by_currency(transactions, currency_code))
    result_ids = [item["id"] for item in result]
    assert result_ids == expected_ids


def test_filter_by_currency_empty() -> None:
    assert list(filter_by_currency([], "USD")) == []


def test_filter_by_currency_no_currency_key() -> None:
    txs: List[Dict[str, Any]] = [{"id": 1, "description": "test"}]
    assert list(filter_by_currency(txs, "USD")) == []


def test_transaction_descriptions(transactions: List[Dict[str, Any]]) -> None:
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    result = list(transaction_descriptions(transactions))
    assert result == expected


def test_transaction_descriptions_empty() -> None:
    assert list(transaction_descriptions([])) == []


def test_transaction_descriptions_no_description() -> None:
    txs: List[Dict[str, Any]] = [{"id": 1}, {"id": 2, "description": "abc"}]
    result = list(transaction_descriptions(txs))
    assert result == ["", "abc"]


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 5, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003", "0000 0000 0000 0004"]),
        (9999, 10001, ["0000 0000 0000 9999", "0000 0000 0001 0000"]),
        (0, 1, ["0000 0000 0000 0000"]),
    ],
)
def test_card_number_generator(start: int, stop: int, expected: List[str]) -> None:
    result = list(card_number_generator(start, stop))
    assert result == expected


def test_card_number_generator_empty() -> None:
    assert list(card_number_generator(5, 5)) == []
