from datetime import datetime, date

def week_print(dict):  #замена дней недели 
    result = ''
    days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    for key in dict:
        result += f'{days[int(key)-1]} : {dict[key]}\n'
    return result


def get_birthdays_per_week(users):    
    result ={}
    now = date.today().isocalendar()  # сегодня 
    for user in users:
        d = date.fromisoformat(users[user]).replace(year=now[0]).isocalendar()
        if d[1] == now[1] and d[2] < 6:  # проверка ДР на этой  рабочей неделе 
            if d[2] not in result:   
                result[d[2]] = user
            else:   
                s= result.get(d[2])
                result[d[2]] = f'{s}, {user}'
        if d[1] == now[1]-1 and d[2] >= 6:  # проверка ДР если попал на прошедшие выходные 
            if 1 not in result:   
                result[1] = user
            else:   
                s= result.get(1)
                result[1] = f'{s}, {user}'
    result = dict(sorted(result.items())) 
    return week_print(result)

users = {'Bill':'2015-06-03','Kill':'2015-06-14', 'Rill':'1999-06-09', 'Till':'2025-06-08'}
print (get_birthdays_per_week(users))