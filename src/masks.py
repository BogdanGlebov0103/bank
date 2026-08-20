def get_mask_card_number(number: str) -> str:
    '''
    скрывает некоторые цифры номера карты
    '''
    return f"{number[0:4]} {number[4:6]}** **** {number[12:17]}"


def get_mask_account(number: str) -> str:
    '''
    маскирует номер счета
    '''
    return "**" + number[-4:]


if __name__ == '__main__':
    number = "1234567891234567"
    print(get_mask_card_number(number))
    print(get_mask_account(number))
