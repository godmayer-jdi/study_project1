import pandas as pd
from typing import List, Dict, Any


def read_transactions_from_csv(file_path: str) -> List[Dict[str, Any]]:
    """
    Считывает финансовые операции из CSV-файла.
    """
    df = pd.read_csv("../data/transactions.csv")
    transactions = df.to_dict(orient='records')
    return transactions


def read_transactions_from_excel(file_path: str) -> List[Dict[str, Any]]:
    """
    Считывает финансовые операции из Excel-файла.
    """
    df = pd.read_excel("../data/transactions_excel.xlsx")
    transactions = df.to_dict(orient='records')
    return transactions