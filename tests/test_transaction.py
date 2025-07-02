import json
from typing import Any, Dict, List
from unittest.mock import MagicMock, patch

import pytest

from src.external_api import convert_transaction_to_rub
from src.utils import load_transactions_from_json


@pytest.fixture
def tmp_json_file(tmp_path: Any) -> str:
    # Создаём временный файл с транзакциями
    data: List[Dict[str, Any]] = [
        {"operationAmount": {"amount": "100.00", "currency": {"code": "RUB"}}},
        {"operationAmount": {"amount": "10.00", "currency": {"code": "USD"}}},
    ]
    file_path = tmp_path / "test.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)
    return str(file_path)


def test_load_transactions_from_json_ok(tmp_json_file: str) -> None:
    result: List[Dict[str, Any]] = load_transactions_from_json(tmp_json_file)
    assert isinstance(result, list)
    assert len(result) == 2


def test_load_transactions_from_json_empty(tmp_path: Any) -> None:
    file_path = tmp_path / "empty.json"
    file_path.write_text("", encoding="utf-8")
    result: List[Dict[str, Any]] = load_transactions_from_json(str(file_path))
    assert result == []


def test_load_transactions_from_json_not_found() -> None:
    result: List[Dict[str, Any]] = load_transactions_from_json("no_such_file.json")
    assert result == []


def test_load_transactions_from_json_not_list(tmp_path: Any) -> None:
    file_path = tmp_path / "obj.json"
    file_path.write_text('{"foo": "bar"}', encoding="utf-8")
    result: List[Dict[str, Any]] = load_transactions_from_json(str(file_path))
    assert result == []


@patch("src.external_api.requests.get")
def test_convert_transaction_to_rub_rub(mock_get: Any) -> None:
    transaction: Dict[str, Any] = {"operationAmount": {"amount": "123.45", "currency": {"code": "RUB"}}}
    result: float = convert_transaction_to_rub(transaction)
    assert result == 123.45
    mock_get.assert_not_called()


@patch("src.external_api.requests.get")
def test_convert_transaction_to_rub_usd(mock_get: Any) -> None:
    transaction: Dict[str, Any] = {"operationAmount": {"amount": "10.00", "currency": {"code": "USD"}}}
    mock_response = MagicMock()
    mock_response.json.return_value = {"result": 950.0}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result: float = convert_transaction_to_rub(transaction)
    assert result == 950.0
    mock_get.assert_called_once()


@patch("src.external_api.requests.get")
def test_convert_transaction_to_rub_unknown(mock_get: Any) -> None:
    transaction: Dict[str, Any] = {"operationAmount": {"amount": "10.00", "currency": {"code": "JPY"}}}
    result: float = convert_transaction_to_rub(transaction)
    assert result == 0.0
    mock_get.assert_not_called()
