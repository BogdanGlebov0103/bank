list_dict = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
   {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

def filter_by_state(list_dict, state='EXECUTED'):
    '''
    возвращает новый список, где значение совпадает со значением, указанным в параметре
    '''
    new_list_dict = [i for i in list_dict
                     for k, v in i.items()
                     if v == state]
    return new_list_dict


def sort_by_date(list_dict, decreasing = True):
    '''
    фильтрует по дате на убывание
    '''
    return sorted(list_dict, key=lambda d: d['date'], reverse=decreasing)


f_s = print(filter_by_state(list_dict, state='EXECUTED'))
s_d = print(sort_by_date(list_dict, decreasing = True))
