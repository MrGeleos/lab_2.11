#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
"""
Используя замыкания функций, объявите внутреннюю функцию, которая на основе двух
параметров вычисляет площадь фигуры. Какой именно фигуры: треугольника или
прямоугольника, определяется параметром type внешней функции. Если type принимает
значение 0, то вычисляется площадь треугольника, а иначе – прямоугольника. По
умолчанию параметр type должен быть равен 0. Вычисленное значение должно
возвращаться внутренней функцией. Вызовите внутреннюю функцию замыкания и
отобразите на экране результат её работы.
"""


def f1(l, a, b):
    type = 0

    if l != 0:
        type = l
    else:
        print("Type не изменился")

    def f2(s):
        if type == 0:
            s = 1/2 * (a * b)
            return s
        else:
            s = a * b
            return s

    return f2


if __name__ == '__main__':
    a1 = int(input("Введите сторуну a: "))
    b1 = int(input("Введите сторону b: "))
    h = int(input("Если вы хотите изменить type, напишите любое число, кроме нуля: "))
    fs = f1(h, a1, b1)
    print(fs(h))
