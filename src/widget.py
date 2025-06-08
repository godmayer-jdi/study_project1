from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(info: str) -> str:
    """
    Принимает строку с типом и номером карты или счета.
    Возвращает строку с замаскированным номером.
    """
    parts = info.split()
    number = parts[-1]
    card_type = " ".join(parts[:-1])

    if card_type.lower().startswith("счет") or card_type.lower().startswith("счёт"):
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{card_type} {masked_number}"


def get_date(date_str: str) -> str:
    """
    Принимаем дату в формате "2024-03-11T02:26:18.671407",
    и возвращаем строку в формате "ДД.ММ.ГГГГ", например "11.03.2024".
    """
    date_part = date_str.split('T')[0]  # отделяем дату от времени
    year, month, day = date_part.split('-')
    return f"{day}.{month}.{year}"