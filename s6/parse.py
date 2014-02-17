# -*- coding: utf-8 -*-
import os
from string import Template

from BeautifulSoup import BeautifulSoup

html = """<html>
<head>Heading</head>
<body attr1='val1'>
    <div class='container'>
        <div id='class'>Something here</div>
        <div>Something else</div>
    </div>
    <div class='xx'>
        NOT SHOW :)
    </div>
</body>
</html>"""
#the HTML code you've written above
parsed_html = BeautifulSoup(html)
print parsed_html.body.find('div', attrs={'class': 'container'}).text

from os import listdir
from os.path import isfile, join, dirname, realpath

# Filter *.html files
thisDir = dirname(realpath(__file__))
onlyFiles = [f for f in listdir(thisDir) if isfile(join(thisDir, f)) and f.endswith(".html")]
#print onlyFiles


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
def go(filename):
    global body, session, session_dist
    f = open(filename, "r")
    html = f.read()

    parsed_html = BeautifulSoup(html)
    # Find hours and theme
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
    print d
    session.theme(theory, practic)
    session_dist.theme(theory_dist, practic_dist)
    res = Template(line_template).safe_substitute(d)
    body += "\n" + res

#print parsed_html.body.find('div', attrs={'class':'container'}).text

# TODO: Дописать сюда все темы
for fn in [
    "alg_number_theory.html", "strings.html"
]:
    go(fn)

# Генерируемый файл 
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
        "index_gen.html", True)

