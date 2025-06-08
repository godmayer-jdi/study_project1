def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты. Пример: 7000792289606361 → 7000 79** **** 6361"""
    card_number = card_number.replace(" ", "")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета. Пример: 73654108430135874305 → **4305"""
    return "**" + account_number[-4:]
