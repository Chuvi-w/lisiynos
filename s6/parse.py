# -*- coding: utf-8 -*-

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
print parsed_html.body.find('div', attrs={'class':'container'}).text

from os import listdir
from os import getcwd
from os.path import isfile, join, dirname, realpath
mypath = dirname(realpath(__file__))
# Filter *.html files
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath,f)) and f.endswith(".html")]
print onlyfiles

# Read from file
def go(filename):
  f = open(filename,"r")
  html = f.read()

  parsed_html = BeautifulSoup(html)
  # Find hours and theme
  print 'h1 = ', parsed_html.body.find('h1').text
  theory = int(parsed_html.body.find('span', attrs={'class':'theory'}).text)
  practic = int(parsed_html.body.find('span', attrs={'class':'practic'}).text)
  print 'theory = ', theory
  print 'practic = ', practic
  sum = theory + practic
  print 'sum =',sum

  # TODO: print HTML !!!
  # Выводить в index.html и генерировать описание

#print parsed_html.body.find('div', attrs={'class':'container'}).text

# TODO: Дописать сюда все темы
for fn in ["alg_number_theory.html"]:
  go(fn)


