# -*- coding: utf-8 -*-
import sys

sys.path.append('../common')

from gen import go, GenerateIndex, Theme

# Все темы в порядке их следования в курсе
for fn in [
    Theme('Логика + Алгоритмы над целыми числами', 'Понедельник - 7'),
    ("logic1.html", 1, 1, 0, 2),
    ("logic2.html", 1, 0, 0, 2),
    ("../s1/integers.html", 3, 1, 0, 2),

    Theme('Функциональное программирование, LISP', 'Вторник - 6'),
    ("fp_lisp.html", 3, 3, 0, 1),

    Theme('Рекурсия и переборные алгоритмы', 'Среда - 6'),
    ("comb.html", 1, 1, 0, 1),
    ("backtracking.html", 1, 1, 0, 2),
    ("monte_carlo.html", 1, 1, 0, 2),

    Theme('Сортировки', "Четверг - 6"),
    ("../s1/sort.html", 3, 3, 0, 4),

    Theme('Алгоритмы на графах', "Пятница - 7"),
    ("graphs.html", 4, 3, 0, 2),

    Theme("Олимпиада", "Суббота - 4"),
    ("../s6/olymp.html", 0, 4, 0, 0),
]:
    go(fn)

GenerateIndex("Сессия 2 - лето: учебно-тематический план")