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
# Find hours and theme

f = open("","r")
data = f.read()


