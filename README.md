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

text

### Запуск flake8

Проверка соответствия кода стандарту PEP 8:
flake8 src/

text

### Запуск mypy

Проверка корректности аннотаций типов:
mypy src/

text

> Требование:  
> Количество ошибок по результатам проверки flake8 и mypy не должно превышать 4.

## Лицензия

Проект распространяется под лицензией MIT.