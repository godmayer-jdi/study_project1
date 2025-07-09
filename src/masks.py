import logging
import os

# Создаём логгер для модуля masks
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

# Абсолютный путь к папке study_project1
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # поднимаемся из src/ в study_project1

LOGS_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOGS_DIR, exist_ok=True)

log_path = os.path.join(LOGS_DIR, "masks.log")

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


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты. Пример: 7000792289606361 → 7000 79** **** 6361"""
    try:
        card_number_clean = card_number.replace(" ", "")
        masked = f"{card_number_clean[:4]} {card_number_clean[4:6]}** **** {card_number_clean[-4:]}"
        logger.debug(f"Маскированный номер карты: {masked}")
        return masked
    except Exception as e:
        logger.error(f"Ошибка маскирования номера карты '{card_number}': {e}")
        raise


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета. Пример: 73654108430135874305 → **4305"""
    try:
        masked = "**" + account_number[-4:]
        logger.debug(f"Маскированный номер счета: {masked}")
        return masked
    except Exception as e:
        logger.error(f"Ошибка маскирования номера счета '{account_number}': {e}")
        raise
