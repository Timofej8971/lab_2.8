#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Решить индивидуальное задание лабораторной работы 2.6,
оформив каждую команду в виде
отдельной функции.
'''


import sys


def main():
    stations = []

    while True:
        command = input(">>> ").lower()
        if command == "exit":
            break
        elif command == "add":
            add(stations)
        elif command == "select":
            select(stations)
        elif command == "show":
            show(stations)
        elif command == "help":
            help()


def add(info):
    punkt = input("Пункт назначения: ")
    nomer = input("Номер поезда: ")
    time = input("Время отправления: ")

    station = {
        'punkt': punkt,
        'nomer': nomer,
        'time': time,
    }

    info.append(station)

    if len(info) > 1:
        info.sort(key=lambda item: item.get('time', ''))


def select(info):
    punkt = input("Введите пункт прибытия для поиска: ")

    if not punkt:
        print("Вы ничего не ввели")

    else:
        for station in info:
            if station.get('punkt', '') == punkt:
                print(
                    "Город прибытия: ", station.get('punkt', ''),
                    " Номер поезда: ", station.get('nomer', ''),
                    " Время отправления: ", station.get('time', '')
                )
                break
            else:
                print(f"Такого города нет: {punkt}", file=sys.stderr)


def show(info):
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 15
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
            "№",
            "Город прибытия",
            "Номер поезда",
            "Время отправления"
        )
    )
    print(line)

    for idx, station in enumerate(info, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                idx,
                station.get('punkt', ''),
                station.get('nomer', ''),
                station.get('time', '')
            )
        )

    print(line)


def help():
    print("Список команд:\n")
    print("add - для добовления маршрутов")
    print("select - для поиска маршпута")
    print("show - для демонстрации всех машрутов")


if __name__ == '__main__':
    main()
