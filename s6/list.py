# -*- coding: utf-8 -*-
import os
from string import Template
import re

def subdirs(d='.'): # Подкаталоги каталога problems
  return [name for name in os.listdir(d) if os.path.isdir(os.path.join(d, name))]

def ReadTemplate(template_fn):
  return open("templates/"+template_fn, 'r').read()

# Запись файла: t - шаблон, d - словарь значений, fn - имя файла
def GenFile(t, d, fn,overwrite=False):
  if not overwrite and os.path.isfile(fn):
    return
  print 'Gen "%s"' % fn
  f = open(fn, 'w')
  f.write(Template(t).safe_substitute(d))
  f.close()

task_cfg = ReadTemplate("task.cfg")
problem = ReadTemplate("problem.tex")

contest_id = os.path.split(os.path.dirname(__file__))[-1]
contest_name = open("name.txt").read().decode("utf-8") # Название контеста
print contest_id,'-',contest_name

# Пробегаем все задачи
l = []

for TaskID in subdirs('problems'):
  if TaskID == '.idea': continue
  # Генерация task.cfg 
  d = { 'TaskID' : TaskID }
  GenFile(task_cfg, d, "problems/%s/task.cfg" % TaskID, True)
  # Если нет заготовки .tex файла, создаём её
  tex_file = "statements/problems/%s.tex" % TaskID
  GenFile(problem,d,tex_file)
  # Читаем заголовок tex файла
  tex_cont = open(tex_file, 'r').read()
  x = re.findall(r'\\begin{problem}\s*{([\w\s\d]+)}' , tex_cont, re.U)
  if x:
    first = x[0]
    prob_name = first.decode('utf-8')
  else:
    prob_name = 'parse'

  # Определяем размер решения
  size = 1
  difficulty_file = '%s/size' % TaskID;
  if os.path.isfile(difficulty_file):
    size = int(open(difficulty_file).read())
  d = {'id':TaskID,'size':size,'name':prob_name}
  l.append(d)


str = ""
problems = "problems = [\n"
Letter = ord('A')
for task in sorted(l, key=lambda k: k['size']):
  str += '\prob{%s} %% %d\n' % (task['id'],task['size'])
  problems += '\tproblAD (%s, "%s", %s)\n' % (chr(Letter), task['name'],task['id'])
  Letter += 1
problems += "];"
print problems


# Генерируем tex файл условий задач
st = ReadTemplate("statements.tex")
st = st.replace('%problem_list%',str)
st = st.replace('%contest_name%',unicode(contest_name).encode("utf-8"))
f = open(os.path.join('statements', contest_id+'.tex'), 'w')
f.write(st)
f.close()

# Генерируем конфигурационный файл
st = ReadTemplate("contest.cfg")
st = st.replace('%problem_list%',unicode(problems).encode('cp866'))
st = st.replace('%contest_name%',unicode(contest_name).encode('cp866'))
f = open(contest_id+'.cfg', 'w')
f.write(st)
f.close()