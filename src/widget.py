from datetime import datetime
from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(name_number_card):
    while name_number_card == '':
        name_number_card = input('Введите номер счета или карты')
    name_split = name_number_card.split()
    new_list = []
    for i in name_split:
        if i == "Счет":
            new_list.append(i)
        elif i.isdigit() and len(i) == 20:
            text_for_account = get_mask_account(i)
            new_list.append(text_for_account)
            break
        elif i.isalpha() and i != "Счет":
            new_list.append(i)
        elif i.isdigit() and len(i) == 16:
            text_for_number = get_mask_card_number(i)
            new_list.append(text_for_number)
            break
    return ' '.join(new_list)


def get_date(data):
    month_day = datetime.fromisoformat(data)
    return month_day.strftime('%d.%m.%Y')


if __name__ == '__main__':

    x = ['MasterCard 7158300734726758',
         'Счет 64686473678894779589',
         'Visa Classic 6831982476737658',
         '']
    data = "2024-03-11T02:26:18.671407"

    print(mask_account_card(x[3]))
    print(get_date(data))










