# Проект study_project1

## Описание

Проект предназначен для обработки данных банковских операций клиента.  
Реализованы функции фильтрации операций по статусу и сортировки по дате.

## Установка

1. Клонируйте репозиторий:

git clone https://github.com/godmayer-jdi/study_project1.git

2. Перейдите в директорию проекта:

cd study_project1

3. Установите зависимости:

pip install -r requirements.txt

## Использование

Импортируйте функции из модуля `processing`:

from src.processing import filter_by_state, sort_by_date

Пример фильтрации:

data = [
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}
]

executed_ops = filter_by_state(data)
canceled_ops = filter_by_state(data, state='CANCELED')

Пример сортировки:

sorted_ops = sort_by_date(data) # по убыванию
sorted_ops_asc = sort_by_date(data, descending=False) # по возрастанию

## Проверка качества кода

Для поддержания качества кода используйте линтеры **flake8** и **mypy**.

### Установка линтеров

Если вы ещё не устанавливали линтеры, выполните:
pip install flake8 mypy

### Запуск flake8

Проверка соответствия кода стандарту PEP 8:
flake8 src/

### Запуск mypy

Проверка корректности аннотаций типов:
mypy src/

> Требование:  
> Количество ошибок по результатам проверки flake8 и mypy не должно превышать 4.

## Лицензия

Проект распространяется под лицензией MIT.
<<<<<<< HEAD
=======


## Тестирование

Для запуска тестов используйте:

pytest --cov=src --cov-report=html

Отчёт о покрытии тестами будет создан в папке `htmlcov`.


## Проверка качества кода

Для проверки стиля и типов используйте:

flake8 src/
mypy src/

Количество ошибок не должно превышать 4.
>>>>>>> origin/feature/homework_tests
 

## Модуль generators

Модуль содержит функции-генераторы для работы с транзакциями:

- filter_by_currency(transactions, currency_code) — возвращает транзакции с заданной валютой.
- transaction_descriptions(transactions) — возвращает описание каждой транзакции.
- card_number_generator(start, stop) — генерирует номера карт в формате XXXX XXXX XXXX XXXX.

### Пример использования

rom src.generators import filter_by_currency, transaction_descriptions, card_number_generator

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
print(next(usd_transactions))

descriptions = transaction_descriptions(transactions)
for _ in range(5):
print(next(descriptions))

for card in card_number_generator(1, 5):
print(card)

## Модуль decorators

В модуле реализован декоратор `log` для логирования выполнения функций.

### Особенности

- Логирует время вызова, имя функции, аргументы.
- Логирует результат выполнения или ошибку.
- Принимает необязательный параметр `filename` для записи логов в файл.
- Если `filename` не указан, логи выводятся в консоль.

## Работа с транзакциями и конвертацией валют

### Чтение транзакций из JSON
from src.utils import load_transactions_from_json

transactions = load_transactions_from_json("data/operations.json")

### Конвертация суммы транзакции в рубли

### Настройка окружения

## Работа с библиотекой pandas и чтение файлов CSV и XLSX

### Загружены библиотеки для работы с CSV и Excel файлами

### Реализована функция для считывания финансовых операций из CSV и Excel

### Функция выдает список словарей с транзакциями
