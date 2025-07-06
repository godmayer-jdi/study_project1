from typing import Any, Dict, List, cast

import pandas as pd


def read_transactions_from_csv(file_path: str = "../data/transactions.csv") -> List[Dict[str, Any]]:
    """
    Считывает финансовые операции из CSV-файла.
    """
    df = pd.read_csv(file_path)
    transactions_any = df.to_dict(orient="records")
    transactions = cast(List[Dict[str, Any]], transactions_any)
    return transactions


def read_transactions_from_excel(file_path: str = "../data/transactions_excel.xlsx") -> List[Dict[str, Any]]:
    """
    Считывает финансовые операции из Excel-файла.
    """
    df = pd.read_excel(file_path)
    transactions_any = df.to_dict(orient="records")
    transactions = cast(List[Dict[str, Any]], transactions_any)
    return transactions
