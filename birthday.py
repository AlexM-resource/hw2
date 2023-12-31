from datetime import datetime, date

def week_print(dict):  #замена дней недели 
    stroka = ''
    days={1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
    for key in dict:
        stroka += f'{days[key]} : {dict[key][0]}\n'
    return stroka


def get_birthdays_per_week(users):    
    dirth_list ={}
    now = date.today().isocalendar()  # сегодня 
    for user in users:
        d = date.fromisoformat(list(user.values())[0]).replace(year=now[0]).isocalendar()
        if d[1] == now[1] and d[2] < 6:  # проверка ДР на этой  рабочей неделе 
            if d[2] not in dirth_list:   
                dirth_list[d[2]] = list(user.keys())
            else:   
                s= dirth_list.get(d[2])
                dirth_list[d[2]] = f'{s}, {list(user.keys())}'
        if d[1] == now[1]-1 and d[2] >= 6:  # проверка ДР если попал на прошедшие выходные 
            if 1 not in dirth_list:   
                dirth_list[1] = list(user.keys())
            else:   
                s= dirth_list.get(1)
                dirth_list[1] = f'{s}, {list(user.keys())}'
    dirth_list = dict(sorted(dirth_list.items())) 
    return week_print(dirth_list)

users = [{'Bill':'2015-06-18'},{'Kill':'2015-06-14'}, {'Rill':'1999-06-28'}, {'Till':'2025-06-24'}]
print (get_birthdays_per_week(users))