# -*- coding: utf-8 -*-
import os
from string import Template
from os import listdir
from os.path import isfile, join, dirname, realpath

from BeautifulSoup import BeautifulSoup


# Filter *.html files
thisDir = dirname(realpath(__file__))
allFiles = set(f for f in listdir(thisDir) if isfile(join(thisDir, f)) and f.endswith(".html"))
allFiles.remove('index_template.html')
allFiles.remove('index.html')
print allFiles


def ReadTemplate(template_fn):
    return open(template_fn, 'r').read()


def GenFile(template, params, fn, overwrite=False):
    """
    Генерация файла
    :param template: шаблон
    :param params: параметры (словарь значений)
    :param fn: имя файла
    :param overwrite: перезаписывать если файл уже существует
    """
    if not overwrite and os.path.isfile(fn):
        return
    print 'Gen "%s"' % fn
    f = open(fn, 'w')
    f.write(Template(template).safe_substitute(params))
    f.close()

# Шаблон одной строки при генерации таблицы
line_template = ReadTemplate("line_template.html")
body = ""


class Session:
    all_theory = 0
    all_practice = 0

    def theme(self, theory, practice):
        self.all_theory += theory
        self.all_practice += practice

    def all_time(self):
        return self.all_theory + self.all_practice

# Сумма по стоблцам
session = Session()
session_dist = Session()


# Read from file
def go(arg):
    global body, session, session_dist
    if isinstance(arg, basestring):
        filename = arg
    else:
        filename, theory, practic, theory_dist, practic_dist = arg

    f = open(filename, "r")
    html = f.read()

    parsed_html = BeautifulSoup(html)
    # Find hours and theme
    print parsed_html.body.find('h1').text
    if isinstance(arg, basestring):
        theory = int(parsed_html.body.find('span', attrs={'class': 'theory'}).text)
        practic = int(parsed_html.body.find('span', attrs={'class': 'practic'}).text)
        theory_dist = int(parsed_html.body.find('span', attrs={'class': 'theory_dist'}).text)
        practic_dist = int(parsed_html.body.find('span', attrs={'class': 'practic_dist'}).text)
        print 'theory = ', theory, theory_dist
        print 'practic = ', practic, practic_dist


    # Выводить в index.html и генерировать описание
    d = {
        'theory': theory, 'practic': practic,
        'theory_dist': theory_dist, 'practic_dist': practic_dist,
        'sum': theory + practic,
        'dist': theory_dist + practic_dist,
        'filename': filename,
        'theme': parsed_html.body.find('h1').text,
    }
    # print d
    session.theme(theory, practic)
    session_dist.theme(theory_dist, practic_dist)
    if d['theory'] == 0: d['theory'] = '&nbsp;';
    if d['theory_dist'] == 0: d['theory_dist'] = '&nbsp;';
    res = Template(line_template).safe_substitute(d)
    body += "\n" + res

#print parsed_html.body.find('div', attrs={'class':'container'}).text

# TODO: Дописать сюда все темы
for fn in [
    ("strings.html", 4, 4, 1, 1),
    ("segment_tree_modification.html", 2, 3, 1, 1),
    ("trees.html", 5, 1, 1, 1),
    ('..\\s3\\segments_tree.html', 3, 2, 1, 2),  # Структуры данных: дерево отрезков
    #("games.html", 2, 4, 1, 1),
    ("alg_number_theory.html", 4, 4, 2, 3), # Целочисленная арифметика, простые числа
    ("olymp.html", 0, 4, 0, 4), # Командная работа (решение олимпиад прошлых лет)
]:
    go(fn)

import color_console as cons


def Check(expected, actual, message):
    if actual != expected:
        default_colors = cons.get_text_attr()
        default_bg = default_colors & 0x0070
        cons.set_text_attr(cons.FOREGROUND_RED | default_bg | cons.FOREGROUND_INTENSITY)
        print 'ERROR:',
        cons.set_text_attr(default_colors)
        print message % (expected, actual)

# Генерируемый файл 
Check(18, session.all_theory, u'Теории на очной сессии должно быть %d часов, сейчас: %d')
Check(36, session.all_time(), u'Всего на очной сессии должно быть %d часов, сейчас: %d')
Check(18, session_dist.all_time(), u'Сумма по дистанционной сессии должна быть %d часов, сейчас: %d')

GenFile(ReadTemplate("index_template.html"),
        {
            'title': "Сессия 6 - осень: учебно-тематический план",
            'body': body.encode("utf-8"),
            'all_theory': session.all_theory,
            'all_practic': session.all_practice,
            'all_session': session.all_time(),
            'all_theory_dist': session_dist.all_theory,
            'all_practic_dist': session_dist.all_practice,
            'all_session_dist': session_dist.all_time(),

        },
        "index.html", True)

# Показываем неиспользованные файлы

