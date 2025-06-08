from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card

print("Маскировка карты:", get_mask_card_number("7000792289606361"))  # 7000 79** **** 6361
print("Маскировка счета:", get_mask_account("73654108430135874305"))  # **4305

print("Маскировка информации о картах и счетах:", mask_account_card("Maestro 1596837868705199"))
# Maestro 1596 83** **** 5199
print("Изменение формата даты:", get_date("2024-03-11T02:26:18.671407"))  # 11.03.2024
