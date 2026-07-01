# 7000 7922 89606361     # входной аргумент
# 7000 79** **** 6361  # выход функции
number = "1234567891234567"


def get_mask_card_number(number: str) -> str:
    return f"{number[0:4]} {number[4:6]}** **** {number[12:17]}"


def get_mask_account(number: str) -> str:
    return "**" + number[-4:]

if __name__ == '__main__':
    print(get_mask_card_number(number))
    print(get_mask_account(number))
