# Функция получает на вход текст вида: “1-й четверг ноября”, “3я среда мая” и
# т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.


import logging
import datetime
from datetime import date, datetime
from collections import namedtuple
import argparse

logging.basicConfig(filename="log.log", encoding= "utf-8", level = logging.INFO)
logger = logging.getLogger("log")

MONTH = {
    'января': 1,
    'февраля': 2,
    'марта': 3,
    'апреля': 4,
    'мая': 5,
    'июня': 6,
    'июля': 7,
    'августа': 8,
    'сентября': 9,
    'октября': 10,
    'ноября': 11,
    'декабря': 12
}
WEEKDAYS = {
    'понедельник': 0,
    'вторник': 1,
    'среда': 2,
    'четверг': 3,
    'пятница': 4,
    'суббота': 5,
    'воскресенье': 6
}

DATE = namedtuple("DATE", "day month year")

def getdate(text):
    num_week, week_day, month = text.split()
    num_week = int(num_week.split("-")[0])
    week_day = WEEKDAYS[week_day]
    count_week = 0
    for day in range(1, 31+1):
        d = date(year=datetime.now().year, month=MONTH[month], day=day)
        if d.weekday()==week_day:
            count_week+=1
            if count_week == num_week:
                logger.info(DATE(d.day, d.month, d.year))
                return d

print(getdate(input("Введите текст вида: '1-й четверг ноября' ")))

def pars_date():
    parser = argparse.ArgumentParser(prog="Работа с датой")
    parser.add_argument('-d', metavar='d', default='1-й')
    parser.add_argument('-w', metavar='w', default=datetime.now().weekday())
    parser.add_argument('-m', metavar='m', default=datetime.now().month)
    args = parser.parse_args()
    return getdate(f'{args.d} {args.w} {args.m}')


if __name__ == "__main__":
    print(pars_date())
