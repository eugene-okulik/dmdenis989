import os
import datetime


def date_from_file(string):
    """
    Получаем строку, извлекаем нужные элементы по индексу,
    создаем новую строку,
    приводим ее к нужному формату с типом дата
    :param string: полученная из файла строка
    :return: отформатированная дата
    """
    parts = string.split()
    date = f'{parts[1]} {parts[2]}'
    final_date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
    return final_date


base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')

with open(eugene_file_path, encoding='UTF8') as data_file:
    lines = data_file.readlines()

line1, line2, line3 = [line.strip() for line in lines]

final_date1 = date_from_file(line1)
date1_after_week = final_date1 + datetime.timedelta(days=7)
print(date1_after_week)

final_date2 = date_from_file(line2)
date2_day = final_date2.strftime('%A')
print(date2_day)

final_date3 = date_from_file(line3)
past_date = datetime.datetime.now() - final_date3
print(past_date.days)
