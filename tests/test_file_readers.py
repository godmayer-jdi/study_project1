from unittest.mock import MagicMock, patch

import pytest

from src.file_readers import read_transactions_from_csv, read_transactions_from_excel


@pytest.fixture
def mock_csv_df() -> MagicMock:
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"id": 1, "amount": "100"}]
    return mock_df


@pytest.fixture
def mock_excel_df() -> MagicMock:
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"id": 2, "amount": "200"}]
    return mock_df


@patch("src.file_readers.pd.read_csv")
def test_read_transactions_from_csv(mock_read_csv: MagicMock) -> None:
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"id": 1, "amount": "100"}]
    mock_read_csv.return_value = mock_df

    result = read_transactions_from_csv("dummy.csv")
    mock_read_csv.assert_called_once_with("dummy.csv")
    assert result == [{"id": 1, "amount": "100"}]


@patch("src.file_readers.pd.read_excel")
def test_read_transactions_from_excel(mock_read_excel: MagicMock) -> None:
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"id": 2, "amount": "200"}]
    mock_read_excel.return_value = mock_df

    result = read_transactions_from_excel("dummy.xlsx")
    mock_read_excel.assert_called_once_with("dummy.xlsx")
    assert result == [{"id": 2, "amount": "200"}]
