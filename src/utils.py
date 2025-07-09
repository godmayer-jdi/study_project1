import json
import logging
import os
from typing import Any, Dict, List

# Создаём логгер для модуля utils
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

# Абсолютный путь к папке study_project1
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # поднимаемся из src/ в study_project1

LOGS_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOGS_DIR, exist_ok=True)

log_path = os.path.join(LOGS_DIR, "utils.log")

file_handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

if not logger.hasHandlers():
    logger.addHandler(file_handler)

logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")


def load_transactions_from_json(path: str) -> List[Dict[str, Any]]:
    """
    Загружает список транзакций из JSON-файла.
    Если файл пустой, не найден или не содержит список — возвращает пустой список.
    """
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.debug(f"Успешно загружено {len(data)} транзакций из файла {path}")
                return data
            else:
                logger.error(f"Файл {path} не содержит список транзакций")
                return []
    except FileNotFoundError:
        logger.error(f"Файл {path} не найден")
        return []
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON из файла {path}: {e}")
        return []
