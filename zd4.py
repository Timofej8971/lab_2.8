#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Решите следующую задачу: напишите программу,
в которой определены следующие четыре
функции:
1. Функция get_input() не имеет параметров,
запрашивает ввод с клавиатуры и
возвращает в основную программу полученную строку.
2. Функция test_input() имеет один параметр.
В теле она проверяет, можно ли переданное
ей значение преобразовать к целому числу.
Если можно, возвращает логическое True.
Если нельзя – False.
3. Функция str_to_int() имеет один параметр.
В теле преобразовывает переданное
значение к целочисленному типу.
Возвращает полученное число.
4. Функция print_int() имеет один параметр.
Она выводит переданное значение на экран и
ничего не возвращает.
В основной ветке программы вызовите первую функцию.
То, что она вернула, передайте во
вторую функцию. Если вторая функция вернула True,
то те же данные (из первой функции)
передайте в третью функцию,
а возвращенное третьей функцией значение – в четвертую.
'''


def get_input():
    zapros = input("Введите строку: ")
    if test_input(zapros) is True:
        print_int(str_to_int(zapros))
    else:
        print("Строку нельзя конвертировать в целое число")


def test_input(stroka):
    try:
        int(stroka)
        return True
    except ValueError:
        return False


def str_to_int(stroka):
    otvet = int(stroka)
    return otvet


def print_int(chislo):
    print(chislo)


if __name__ == '__main__':
    get_input()
