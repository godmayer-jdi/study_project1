import os
import pytest
from src.decorators import log


def test_log_console_success(capsys):
    @log()
    def add(a, b):
        return a + b

    result = add(2, 3)
    captured = capsys.readouterr()
    assert result == 5
    assert "Вызов функции 'add' с аргументами: 2, 3" in captured.out
    assert "Функция 'add' вернула: 5" in captured.out


def test_log_console_exception(capsys):
    @log()
    def div(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        div(1, 0)

    captured = capsys.readouterr()
    assert "Вызов функции 'div' с аргументами: 1, 0" in captured.out
    assert "Ошибка в функции 'div': ZeroDivisionError" in captured.out


def test_log_file_success(tmp_path):
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def mul(a, b):
        return a * b

    result = mul(4, 5)
    assert result == 20

    content = log_file.read_text(encoding="utf-8")
    assert "Вызов функции 'mul' с аргументами: 4, 5" in content
    assert "Функция 'mul' вернула: 20" in content


def test_log_file_exception(tmp_path):
    log_file = tmp_path / "error.log"

    @log(filename=str(log_file))
    def sub(a, b):
        return a - b

    # Искусственно вызываем исключение
    @log(filename=str(log_file))
    def raise_error():
        raise ValueError("Ошибка!")

    with pytest.raises(ValueError):
        raise_error()

    content = log_file.read_text(encoding="utf-8")
    assert "Вызов функции 'raise_error' с аргументами:" in content
    assert "Ошибка в функции 'raise_error': ValueError - Ошибка!" in content