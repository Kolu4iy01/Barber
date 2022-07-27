from datetime import datetime, timedelta
from itertools import takewhile, count

date_start = input(
    'Дата с которой начинается расписание: ')
date_end = input(
    'Дата на которой заканчивается расписание: ')
days_work = int(input(
    'Сколько дней подряд парикмахер работает: '))
days_skip = int(input(
    'Сколько дней после этого отдыхает: '))

# форматирование строчной даты в datetime
date_start_iso = datetime.strptime(date_start, "%Y-%m-%d")
date_end_iso = datetime.strptime(date_end, "%Y-%m-%d")
# интервал между датами
interval = days_work + days_skip
# период составления расписания форматированный в int
end = int(((date_end_iso - date_start_iso).__str__())[:2])
#
date_new_work = []
for y in takewhile(lambda y: y < end, count(0, interval)):
    if days_work > 0:    #range(0, end, interval):
        delta = ((date_start_iso + timedelta(days=y)).__str__())[:10]
    else:
        break
    date_new_work.append(delta)
print(date_new_work)

# a = input()
# def data_45(a):
#     result = ''
#     for char in a:
#         if char == ']' or char =='[':
#             result = result + ''
#         #elif char == '-':
#          #   result = result + '.'
#         else:
#             result = result + char
#     return result
#
# [data_start, date_end, x, y] = data_45(a).split(',')
