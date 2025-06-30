import datetime
import functools
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования вызова функции.
    Если filename указан, логи пишутся в файл, иначе — в консоль.
    Логирует имя функции, аргументы, результат или ошибку.
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            time_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            func_name = func.__name__
            args_repr = ", ".join(repr(a) for a in args)
            kwargs_repr = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
            params = ", ".join(filter(None, [args_repr, kwargs_repr]))

            log_message_start = f"[{time_str}] Вызов функции '{func_name}' с аргументами: {params}"
            try:
                result = func(*args, **kwargs)
                log_message_end = f"[{time_str}] Функция '{func_name}' вернула: {result!r}"
                _write_log(log_message_start, filename)
                _write_log(log_message_end, filename)
                return result
            except Exception as e:
                log_message_error = (
                    f"[{time_str}] Ошибка в функции '{func_name}': {type(e).__name__} - {e}. " f"Аргументы: {params}"
                )
                _write_log(log_message_start, filename)
                _write_log(log_message_error, filename)
                raise  # проброс исключения дальше

        return wrapper

    return decorator


def _write_log(message: str, filename: Optional[str]) -> None:
    """
    Вспомогательная функция для записи лога.
    Если filename указан — пишет в файл, иначе — выводит в консоль.
    """
    if filename:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(message + "\n")
    else:
        print(message)
