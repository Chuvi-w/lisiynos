# -*- coding: utf-8 -*-
import sys

sys.path.append('../common')

from BeautifulSoup import BeautifulSoup

import glob

tags = set()

for session_dir in ['s1', 's2', 's3', 's4', 's5', 's6']:
    dir_name = "../" + session_dir + "/*.html"
    print dir_name
    for filename in glob.glob(dir_name):
        if filename.endswith('index.html'):
            continue
        print filename
        f = open(filename, "r")
        html = f.read()
        f.close()

        parsed_html = BeautifulSoup(html)
        # Find hours and theme
        #print parsed_html.body.find('h1').text

        for item in parsed_html.body.findAll(True, {'class': 'theme'}):
            tags.add(item.text)
            print u"Тема: ", item.text


def x(t, teory, pract):
    pass

x('АЛГОРИТМЫ ТЕОРИИ ЧИСЕЛ', 8, 10)
x('Алгоритмы над целыми числами', 4, 4)
x('Длинная арифметика', 2, 3)
x('Криптография', 2, 3)
x('КОМБИНАТОРИКА И ТЕОРИЯ ВЕРОЯТНОСТЕЙ. МЕТОД МОНТЕ-КАРЛО', 14, 14)
x('Базовые идеи комбинаторики', 2, 2)
x('Рекурсия и рекуррентные соотношения', 4, 6)
x('Переборные алгоритмы', 4, 4)
x('Метод Монте-Карло', 4, 2)
x('ТЕОРИЯ ГРАФОВ', 14, 12)
x('Классические идеи теории графов', 4, 0)
x('Алгоритмы на графах', 4, 4)
x('Деревья в программировании', 2, 2)
x('Динамическое программирование', 4, 6)
x('ВЫЧИСЛИТЕЛЬНАЯ ГЕОМЕТРИЯ', 8, 8)
x('Основные геометрические понятия', 3, 0)
x('Отношения между геометрическими объектами', 3, 2)
x('Построение выпуклой оболочки', 2, 2)
x('Задачи с использованием геометрических понятий', 0, 4)
x('Логика', 4, 6)
x('Булева алгебра и построение логических схем', 2, 3)
x('Алгебра логики', 5, 6)
x('ЯЗЫКИ И ГРАММАТИКИ', 7, 3)
x('Компьютерное представление и обработка формул', 1, 2)
x('Конечные автоматы', 2, 1)
x('Машины Тьюринга и система Поста', 4, 0)