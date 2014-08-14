# -*- utf-8 -*-
# Полиномиальное хеширование строк

from math import *


def is_prime(a):
    """ Простое ли число a? """
    return all(a % i for i in range(2, int(sqrt(a) + 0.1) + 1))

# Генерируем все простые числа < 100
primes = [x for x in range(2, 100) if is_prime(x)]
print(*primes)

# Простые числа больше миллиарда
primes = [x for x in range(10 ** 9, 10 ** 9 + 1000) if is_prime(x)]
print(*primes)

# Пусть есть некоторая строка s
s = 'abacaba'

P = 10 * 9 + 7
b = 29

# Считаем заранее все степени
base = [0] * len(s)
base[0] = 1
for i in range(1, len(s)):
    base[i] = (base[i - 1] * b) % P

# Прямое вычисление хеша
def hash_slow(s):
