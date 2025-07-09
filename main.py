from typing import List, Dict, Any

from src.bank_operations import process_bank_search, process_bank_operations
from src.file_readers import read_transactions_from_csv, read_transactions_from_excel
from src.utils import load_transactions_from_json


def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    while True:
        choice = input("Пользователь: ").strip()
        if choice == "1":
            print("Программа: Для обработки выбран JSON-файл.")
            data = load_transactions_from_json("../data/transactions.json")
            break
        elif choice == "2":
            print("Программа: Для обработки выбран CSV-файл.")
            data = read_transactions_from_csv("../data/transactions.csv")
            break
        elif choice == "3":
            print("Программа: Для обработки выбран XLSX-файл.")
            data = read_transactions_from_excel("../data/transactions_excel.xlsx")
            break
        else:
            print("Программа: Неверный выбор. Пожалуйста, введите 1, 2 или 3.")

    valid_statuses = {"EXECUTED", "CANCELED", "PENDING"}

    while True:
        status = input(
            "Программа: Введите статус, по которому необходимо выполнить фильтрацию.\n"
            f"Доступные для фильтровки статусы: {', '.join(valid_statuses)}\nПользователь: "
        ).strip().upper()
        if status in valid_statuses:
            print(f'Программа: Операции отфильтрованы по статусу "{status}"')
            break
        else:
            print(f'Программа: Статус операции "{status}" недоступен.')

    # Фильтрация по статусу (регистр учитывается как в статусах)
    filtered_data = [op for op in data if op.get("status", "").upper() == status]

    if not filtered_data:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    # Сортировка по дате
    sort_answer = input("Программа: Отсортировать операции по дате? Да/Нет\nПользователь: ").strip().lower()
    if sort_answer == "да":
        order = input("Программа: Отсортировать по возрастанию или по убыванию?\nПользователь: ").strip().lower()
        reverse = order == "по убыванию"
        def parse_date(op: Dict[str, Any]) -> Any:
            from datetime import datetime
            try:
                return datetime.strptime(op.get("date", ""), "%d.%m.%Y")
            except Exception:
                return datetime.min  # если дата отсутствует или некорректна

        filtered_data.sort(key=parse_date, reverse=reverse)

    # Фильтрация по валюте (только рубли)
    rub_filter = input("Программа: Выводить только рублевые транзакции? Да/Нет\nПользователь: ").strip().lower()
    if rub_filter == "да":
        filtered_data = [op for op in filtered_data if op.get("operationAmount", {}).get("currency", {}).get("name", "").lower() == "руб."]

    # Фильтрация по слову в описании
    desc_filter = input("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: ").strip().lower()
    if desc_filter == "да":
        search_word = input("Программа: Введите слово для поиска в описании:\nПользователь: ").strip()
        filtered_data = process_bank_search(filtered_data, search_word)

    # Вывод результата
    if not filtered_data:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print("Программа: Распечатываю итоговый список транзакций...\n")
    print(f"Всего банковских операций в выборке: {len(filtered_data)}\n")

    for op in filtered_data:
        date = op.get("date", "")
        description = op.get("description", "")
        print(f"{date} {description}")
        # Пример вывода счёта и суммы, если есть
        from_account = op.get("from", "")
        to_account = op.get("to", "")
        if from_account and to_account:
            print(f"{from_account} -> {to_account}")
        amount_info = op.get("operationAmount", {})
        amount = amount_info.get("amount", "")
        currency = amount_info.get("currency", {}).get("name", "")
        if amount and currency:
            print(f"Сумма: {amount} {currency}")
        print()

if __name__ == "__main__":
    main()
