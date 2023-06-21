from datetime import datetime, date

def week_print(dict):  #замена дней недели 
    stroka = ''
    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    for key in dict:
        stroka += f'{days[int(key)-1]} : {dict[key]}\n'
    return stroka


def get_birthdays_per_week(users):    
    dirth_list ={}
    now = date.today().isocalendar()  # сегодня 
    for user in users:
        d = date.fromisoformat(users[user]).replace(year=now[0]).isocalendar()
        if d[1] == now[1] and d[2] < 6:  # проверка ДР на этой  рабочей неделе 
            if d[2] not in dirth_list:   
                dirth_list[d[2]] = user
            else:   
                s= dirth_list.get(d[2])
                dirth_list[d[2]] = f'{s}, {user}'
        if d[1] == now[1]-1 and d[2] >= 6:  # проверка ДР если попал на прошедшие выходные 
            if 1 not in dirth_list:   
                dirth_list[1] = user
            else:   
                s= dirth_list.get(1)
                dirth_list[1] = f'{s}, {user}'
    dirth_list = dict(sorted(dirth_list.items())) 
    return week_print(dirth_list)

users = {'Bill':'2015-06-17','Kill':'2015-06-21', 'Rill':'1999-06-25', 'Till':'2025-06-08'}
print (get_birthdays_per_week(users))