#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Решите следующую задачу: напишите функцию,
которая считывает с клавиатуры числа и
перемножает их до тех пор, пока не будет введен 0.
Функция должна возвращать
полученное произведение.
Вызовите функцию и выведите на экран результат ее работы.
'''


def peremnog():
    i = 1
    while True:
        zapros = int(input("Введите число: "))
        if zapros == 0:
            print("Перемножение прекращено")
            break
        else:
            i *= zapros
            print(i)


if __name__ == '__main__':
    peremnog()