# stepik.org/lesson/2414/step/5?unit=931
# проверка на сон Ани
"""
A = int(input())
B = int(input())
H = int(input())
if H < A : print("Недосып")
if H > B : print("Пересып")
if A <= H <= B : print("Это нормально")
"""

# проверка на високосность
from typing import List

"""
while True:
    H = int(input())
    if 1900<=H<=3000:
        if H%4==0 and H%400==0: print("Мой Високосный") #думал так надо, моя ошибка
        elif H%4==0 and H%100!=0 or H%400==0: print("Их Високосный")
        else: print("Обычный")
    else: break
"""



# https://stepik.org/lesson/5047/step/1?unit=1086
# площадь 3угольника по формуле Герона
"""
a = int(input())
b = int(input())
c = int(input())
p = (a+b+c)/2
S = float(p*(p-a)*(p-b)*(p-c))**0.5
print(S)
"""

"""
# проверка числа на вхождение в интервал
n = int(input())
if -15<n<=12 or 14<n<17 or 19<=n : print("True")
else: print("False")
"""

#простой калькулятор
"""
n1 = float(input())
n2 = float(input())
c = input()
if n2==0 and (c=="/" or c=="mod" or c=="div"):
    print("Деление на 0!")
elif c=="+": print(n1+n2)
elif c=="-": print(n1-n2)
elif c=="/": print(n1/n2)
elif c=="*": print(n1*n2)
elif c=="mod": print(n1%n2)
elif c=="pow": print(n1**n2)
elif c=="div": print(n1//n2)
"""

# площади жилья страны Малевии
"""
T = input() #тип фигуры
if T=="треугольник":
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    S = float(p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(S)
elif T=="прямоугольник":
    a = int(input())
    b = int(input())
    print(float(a*b))
elif T=="круг":
    r = int(input())
    print(float(3.14*(r**2)))
"""


# задача 1.12 https://stepik.org/lesson/5047/step/5?unit=1086
# Напишите программу, которая получает на вход три целых числа, по одному числу
# в строке, и выводит на консоль в три строки сначала максимальное, потом минимальное,
# после чего оставшееся число. На ввод могут подаваться и повторяющиеся числа.
# Sample Input 1: 8 2 14
# Sample Output 1: 14 2 8
# Sample Input 2: 23 23 21
# Sample Output 2: 23 21 23
"""
a = int(input())
b = int(input())
c = int(input())
#проверка на максимум:
if a>=b and a>=c :
    print(a)
    mx=a
elif a>=b and a<=c :
    print(c)
    mx=c
elif a<=b and b<=c :
    print(c)
    mx=c
elif a<=b and b>=c :
    print(b)
    mx=b
#проверка на минимум:
if a<=b and a<=c :
    print(a)
    mn=a
elif a<=b and a>=c :
    print(c)
    mn=c
elif a>=b and b>=c :
    print(c)
    mn=c
elif a>=b and b<=c :
    print(b)
    mn=b
# вывод оставшегося числа
print(a+b+c-mx-mn)
"""

# задача "Робот и программисты" 1.12 https://stepik.org/lesson/5047/step/5?unit=1086
# Напишите программу, считывающую с пользовательского ввода целое число n (неотрицательное),
# выводящее это число в консоль вместе с правильным образом изменённым словом
# "программист", для того, чтобы робот мог нормально общаться с людьми, например:
# 1 программист, 2 программиста, 5 программистов. В комнате может быть очень много
# программистов. Проверьте, что ваша программа правильно обработает все случаи,
# как минимум до 1000 человек.
""" Мой код:
a=int(input())
if a==1 or (a-1)%10==0 and a%100!=11: print(str(a)+" программист")
elif 5<=a<=20 or 5<=a%10<=20 or 5<=a%100<=20 or a%10==0 or (a-11)%100==0: print(str(a)+" программистов")
elif 2<=a<=4 or 2<=a%10<=4: print(str(a)+" программиста")

Не мой код:
n=int(input())
print(n,'программист'+('ов' if n%10==0 or 4<n%10<10 or 10<n%100<15 else 'а' if 1<n%10<5 else ''))
"""



# задача "Счастливый билет" 1.12 https://stepik.org/lesson/5047/step/5?unit=1086
"""
a = int(input())
print(a%1000000//100000, a%100000//10000, a%10000//1000, a%1000//100, a%100//10, a%10)
if a%10 + a%100//10 + a%1000//100 == a%10000//1000 + a%100000//10000 + a%1000000//100000: 
    print("Счастливый")
else: 
    print("Обычный")
"""

"""m=0
i = 0
while i <= 10:
    m=m+1
    i = i + 1
    if i > 7:
        i = i + 2
print(i, m)
0* **
1*
2* **
3* ***
4* ** ***
"""
# Задача 2.1 https://stepik.org/lesson/3364/step/11?unit=947
# Циклы While
""" подсчет звездочек
i = 0
while i < 5:
    print('*')
    if i % 2 == 0:
        print('**')
    if i > 2:
        print('***')
    i = i + 1
"""
"""
# подсчет введенных целых чисел, пока не введут 0
s=0
a = int(input())
s=s+a
while a!=0:
    a = int(input())
    s=s+a
print(s)
"""


################################################################
# В команде биологов "a" человек, а в команде информатиков — "b" человек.
# Нужно заранее разрезать пирог таким образом, чтобы можно было раздать
# кусочки пирога любой команде, выигравшей соревнование, при этом каждому
# участнику этой команды должно достаться одинаковое число кусочков пирога.
# Нужно найти минимальное подходящее число. Напишите программу, которая
# помогает найти это число. Программа должна считывать размеры команд
# (два положительных целых числа a и b, каждое вводится на отдельной строке)
# и выводить наименьшее число d, которое делится на оба этих числа без остатка.
#ПИРОГ!!! Решил (03-06-2020)!!!
# Sample Input 1: 1 2
# Sample Output 1: 2
# Sample Input 2: 7 5
# Sample Output 2: 35
# Sample Input 3: 15 15
# Sample Output 3: 15
"""
a = int(input())
b = int(input())
if a == b: 
    print(a)
if a>b:
    a,b = b,a
    c = b
c = b
if a < b:
    for i in range(1,a*b):
        if b%a == 0:
            break
        else:
            b = b + c
    print(b)
"""

#https://stepik.org/lesson/3366/step/1?unit=949
# урок 2.2 операторы break, continue
"""
i = 0
s = 0
while i < 10:
    i = i + 1   #1,3,5,7,9 
    s = s + i   #1,4,9,16,25
    if s > 15:
        continue
    i = i + 1   #2,4,6,8,10
print(i) #выводится 10
"""

"""
a=int(input())
while a<=100:
    if a>=10: print(a)
    a = int(input())
"""

# урок 2.3 Циклы for
# Напишите программу,на вход которой даются четыре числа a,b,c и d, каждое
# в своей строке. Программа должна вывести фрагмент таблицы умножения для
# всех чисел отрезка [a;b] на все числа отрезка [c;d].
# Числа a,b,c и d являются натуральными и не превосходят 10, a≤b, c≤d.
"""
a=int(input())
b=int(input())
c=int(input())
d=int(input())
print('    ', end=' ')          # печать 4 пробелов для красоты
for k in range(c, d + 1):       # печать первой строки (от c до d)
    print('%4d' %k, end=' ')
print()                         # перевод строки

for i in range(a,b+1):          # собственно печать таблицы, тут просто
    print('%4d' %i, end=' ')   # плюс 1, потому что range не берет b и d
    for k in range(c,d+1):
        print('%4d' % (i*k), end=' ')
    print()
"""

# Напишите программу, которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль среднее арифметическое всех чисел
# из отрезка [a;b], которые делятся на 3. На вход программе подаются
# интервалы, внутри которых всегда есть хотя бы одно число, которое делится на 3.
"""
a=int(input())
b=int(input())
k=s=0
for i in range(a,b+1):
    if i%3==0:
        k=k+1
        s=s+i
print(s/k)
"""



# https://stepik.org/lesson/3367/step/3?unit=950
# 2.4 Строки и символы
# Напишите программу, которая вычисляет процентное содержание символов G (гуанин)
# и C (цитозин) в введенной строке (программа не должна зависеть от регистра
# вводимых символов). Например, в строке "acggtgttat" процентное содержание символов
# G и C равно (4/10)*100=40.0, где 4-это количество G и C, а 10 - длина строки.
# Sample Input:
# acggtgttat
# Sample Output:
# 40.0
"""
s=input().upper()
print(100*(s.count('C')+s.count('G'))/len(s))
"""

"""
s = 'abcdefghijk'
print(s[:6])
print(s[3:])
print(s[::-1])
print(s[3:6])
print(s[-3:])
print(s[:-6])
print(s[-1:-10:-2])
"""

# РЕШИЛ (03-06-2020)!!!
# s='aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы oдинаковых символов
# исходной строки заменяются на этот символ и количество его повторений в этой
# позиции строки. Напишите программу, которая считывает строку, кодирует её
# предложенным алгоритмом и выводит закодированную последовательность на
# стандартный вывод. Кодирование должно учитывать регистр символов.
# Sample Input 1:
# aaaabbcaa
# Sample Output 1:
# a4b2c1a2
# Sample Input 2:
# abc
# Sample Output 2:
# a1b1c1
'''
a = input()
b = []                      # создаем второй пустой список, куда будем скидывать совпадения
k = 1                       # счетчик совпадений
l = len(a)
for i in range(l):          # перебираем буквы в введенном списке
    if i != l-1:            # нужна проверка на 'out of range', иначе ошибка
        if a[i] != a[i+1]:
            b.append(a[i])  # во 2й список добавляем текущий, тк след.уже другой элемент
            b.append(k)     # добавляем также и их количество
            k = 1           # сбрасываем счетчик
        else:
            k = k + 1       # тк элементы одинаковые, то включаем счетчик
    else:
        b.append(a[i])      # если элемент последний, то его и добавляем просто
        b.append(k)
print(*b, sep='')           # печать в одну строку через *, сепаратор чтобы без пробела
'''



# Напишите программу, на вход которой подается одна строка с целыми числами.
# Программа должна вывести сумму этих чисел. Используйте метод split строки.
'''
a=[int(i) for i in input().split()]
s=0
for i in range (len(a)):
    s=s+a[i]
print(s)
'''
# или можно просто так:
'''
a=[int(i) for i in input().split()]
print(sum(a))
'''

# Напишите программу, на вход которой подаётся список чисел одной строкой.
# Программа должна для каждого элемента этого списка вывести сумму двух его соседей.
# Для элементов списка, являющихся крайними, одним из соседей считается элемент, находящий
# на противоположном конце этого списка. Например, если на вход подаётся список "1 3 5 6 10",
# то на выход ожидается список "13 6 9 15 7" (без кавычек).
# Если на вход пришло только одно число, надо вывести его же.
# Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.
'''
a=[int(i) for i in input().split()]
c=[]                            # создаем НОВЫЙ список, он пустой
c.extend(a)                     # наполняем его "старым" списком
if len(a)==1:                   # если всего один элемент,
    print(*a)                   # то его и печатаем
else:
    for i in range(len(a)):     # перебираем список
        if i!=len(a)-1:         # чтобы не выйти за пределы индексов списка
            c[i]=a[i-1]+a[i+1]  # в НОВЫЙ список складываем элементы старого
        else: c[i]=a[i-1]+a[0]  # если элемент последний, прибавляем 1й(нулевой в Питоне)
    print(*c)                   # печатаем весь новый список в одну строку
'''


# Напишите программу, которая принимает на вход список чисел в одной строке
# и выводит на экран в одну строку значения, которые повторяются в нём более
# одного раза. Для решения задачи может пригодиться метод sort списка.
# Выводимые числа не должны повторяться, порядок их вывода может быть
# произвольным.
# Sample Input 1:
# 4 8 0 3 4 2 0 3
# Sample Output 1:
# 0 3 4
'''
a = [int(i) for i in input().split()]    # 4 8 0 3 4 2 0 3
a.sort()                                    # 0 0 2 3 3 4 4 8
l = len(a)                                  # 8 
k = m = 0
for i in range(l):
    if m>l-1:
        break
    k = a.count(a[m])
    if k > 1: 
        print(a[m])
        m = m+k
    else:
        m = m+1
'''

# https://stepik.org/lesson/3369/step/8?unit=952
# 2.6 Задачи по материалам недели
# Напишите программу, которая считывает с консоли числа (по одному в строке)
# до тех пор, пока сумма введённых чисел не будет равна 0 и сразу после этого
# выводит сумму квадратов всех считанных чисел.
# Гарантируется, что в какой-то момент сумма введённых чисел окажется равной 0,
# после этого считывание продолжать не нужно.
# В примере мы считываем числа 1, -3, 5, -6, -10, 13; в этот момент замечаем,
# что сумма этих чисел равна нулю и выводим сумму их квадратов, не обращая
# внимания на то, что остались ещё не прочитанные значения.
'''Sample Input:
1
-3
5
-6
-10
13
4
-8
Sample Output:
340
'''
'''
s = 1
k = 1
a2 = 0
ss2 = 0
while s != 0:
    s = s - k
    a = int(input())
    s = s + a
    print('сумма=', s)              # не выводить, просто проверка
    a2 = a**2
    ss2 = ss2 + a2
    print('квадрат числа=', a2)     # не выводить, просто проверка
    print('сумма квадратов=', ss2)  # не выводить, просто проверка
    k = 0
print(ss2)
'''


# Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
# (число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное
# целое число n — столько элементов последовательности должна отобразить программа.
# На выходе ожидается последовательность чисел, записанных через пробел в одну строку.
# Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.
'''Sample Input:
7
Sample Output:
1 2 2 3 3 3 4
'''
'''
a = [1]                     # создаем не пустой список, а пока с первым элементом "1"
n = int(input())            # вводим сколько надо вывести в итоге элементов
for i in range(2, n+1):     # цикл добавления элементов в КОНЕЦ списка, начиная с 2
    l=0                     # надо ввести в программу счетчик, заодно и обнулить 
    while l != i:           # надо добавлять столько раз, какое i в данный момент
        a.append(i)         # например i=2, добавляем "2" два раза
        l=l+1               # считаем сколько раз уже добавили
print(*a[:n])               # цикл прошел, выводим в строчку "*" с начала до позиции :n
'''
# еще одно решение, не мое, самое короткий код кажется)
''' n = int(input())
s = []
for i in range (1, n + 1):
        s += [i] * i
        print(s[i-1], end=' ')
'''

# Напишите программу, которая считывает список чисел lst из первой строки и число x
# из второй строки, которая выводит все позиции, на которых встречается число x
# в переданном списке lst. Позиции нумеруются с нуля, если число x не встречается
# в списке, вывести строку "Отсутствует" (без кавычек, с большой буквы).
# Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
''' Sample Input 1:
5 8 2 7 8 8 2 4
8
Sample Output 1:
1 4 5
'''
# МОЙ код:
'''
l = [int(i) for i in input().split()]
x = int(input())
m = -1                          # -1 для проверки первого (нулевого) элемент списка
k = l.count(x)
if k != 0:
    for i in range(k):
        m = l.index(x, m + 1)   # запоминаем позицию, в след.раз стартуем с позиции m+1
        print(m, end=' ')       # выводим в строку, через пробел
else:
    print("Отсутствует")
'''
#'''
# НЕ мой код:
'''lst = list(map(int, input().split()))
x = int(input())
if x not in lst:
    print('Отсутствует')
else:
    for i in range(len(lst)):
        if lst[i] == x:
            print(i, end=' ')
'''

# НЕ РЕШИЛ!!!
# Напишите программу, на вход которой подаётся прямоугольная матрица в виде
# последовательности строк,заканчивающихся строкой, содержащей только
# строку "end" (без кавычек). Программа должна вывести матрицу того же размера,
# у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы
# на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов
# соседний элемент находится с противоположной стороны матрицы. В случае одной
# строки/столбца элемент сам себе является соседом по соответствующему направлению.
# Sample Input 1:
# 9 5 3
# 0 7 -1
# -5 2 9
# end
# Sample Output 1:
# 3 21 22
# 10 6 19
# 20 16 -1

'''n, m, = (int(i) for i in input().split())       # чтение размеров поля
a = [[0 for j in range(m)] for i in range(n)]   # заполнение поля нулями
'''
'''n = [1]
i = 0
while str(n[i]) != 'end':

    n = [i for i in input().split()]
    s = int(n[i]) + 1
    print(s)

print("выход")
'''

# НЕ РЕШИЛ!!!
# Дополнительная
# Выведите таблицу размером n×n, заполненную числами от 1 до n2 по спирали,
# выходящей из левого верхнего угла и закрученной по часовой стрелке,
# как показано в примере (здесь n=5):
# Sample Input:
# 5
# Sample Output:
# 1 2 3 4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9
'''
n = int(input())                        # вводим размер квадрата (5)
a = [i for i in range(1, n*n+1)]        # наполняем список элементами от 1 до 25
'''
'''
print(*a[0:n])                          # печать 1й строки (1...5)
первый вариант
a2 = [(4*n-5)+i for i in range(1,n)]    # вторая строка без последнего элемента (16...19)
print(*a2[0:n], n+1)                    # печать 2й строки, включая последний элемент
a3 = [(8*n-17)+i for i in range(1,n-2)]
print(4*n-5, *a3[0:n], 5*n-5, n+2       # печать 3й строки, включая последний элемент
'''
'''второй вариант
for i in range(1,2): print(*a[0:n])      # печать 1й строки (1...5)
for i in range(2,n):
    for j in range(1,n+1):
        print(4*n-3,'\t', end='')
    print()
'''

# 3.1 Функции https://stepik.org/lesson/3372/step/9?unit=955
# Напишите функцию f(x), которая возвращает значение следующей функции,
# определённой на всей числовой прямой:
# f(x)=​ 1−(x+2)**2,​при x≤−2
# f(x) = -x/2​, при −2<x≤2 и
# f(x) = (x−2)**2+1,при 2<x​
'''
x = float(input())
def f(x):
    if x <= -2:
        f = 1 -(x + 2)**2
    elif x > 2:
        f = (x-2)**2 + 1
    else:
        f = -x/2
    return(f)
print(f(x))
'''

# Напишите функцию modify_list(l), которая принимает на вход список целых чисел,
# удаляет из него все нечётные значения, а чётные нацело делит на два.
# Функция не должна ничего возвращать, требуется только изменение переданного
# списка, например:
# l = [1, 2, 3, 4, 5, 6]
# print(modify_list(l))  # None
# print(l)               # [1, 2, 3]
# modify_list(l)
# print(l)               # [1]
# l = [10, 5, 8, 3]
# modify_list(l)
# print(l)               # [5, 4]
# Функция не должна осуществлять ввод/вывод информации.
'''
def modify_list(l):
    b = []              # нужен второй список
    for i in l:         # пробегаем по элементам списка l
        if i % 2 == 0:  # число четное, делим без остатка на 2
            i = i // 2  # если делить просто /, то будут числа 1.0 и т.д.
            b.append(i) # наполняем новый список
    l.clear()           # очищаем старый список
    l.extend(b)         # наполняем его новым списком
'''
# НЕ МОЕ
# def modify_list(l):
#    l[:] = [i//2 for i in l if i % 2 == 0]


# https://stepik.org/lesson/3373/step/5?unit=956
# 3.2 Словари
# Задача №1
# Напишите функцию update_dictionary(d, key, value), которая принимает на вход
# словарь d и два числа: key и value. Если ключ key есть в словаре d, то добавьте
# значение value в список, который хранится по этому ключу. Если ключа key нет
# в словаре, то нужно добавить значение в список по ключу 2∗key. Если и ключа
# 2∗key нет, то нужно добавить ключ 2∗key в словарь и сопоставить ему список из
# переданного элемента [value]. Требуется реализовать только эту функцию, кода
# вне неё не должно быть. Функция не должна вызывать внутри себя функции input
# и print. Пример работы функции:
#
# d = {}
# print(update_dictionary(d, 1, -1))  # None
# print(d)                            # {2: [-1]}
# update_dictionary(d, 2, -2)
# print(d)                            # {2: [-1, -2]}
# update_dictionary(d, 1, -3)
# print(d)                            # {2: [-1, -2, -3]}
'''
def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)                # ключ есть -> добавляем значение для текущего ключа key
    else:
        if 2*key in d:
            d[2*key].append(value)          # ключ есть -> добавляем значение для текущего ключа 2*key 
        else:
            d[2*key] = [value]              # ключа нет -> создаем(!) значение, а не добавляем! (второй принт, после None)
d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-1, -2, -3]}
'''


# 3.2 Словари
# Задача №2
# Программа сможет подсчитать слова, разделённые пробелом и вывести получившуюся
# статистику. Программа должна считывать одну строку со стандартного ввода и
# выводить для каждого уникального слова в этой строке число его повторений(без
# учёта регистра) в формате "слово количество"(см.пример вывода). Порядок вывода
# слов может быть произвольным, каждое уникальное слово должно выводиться только
# один раз.

# Sample Input 1:
# a aa abC aa ac abc bcd a
# Sample Output 1:
# ac 1
# a 2
# abc 2
# bcd 1
# aa 2

# Sample Input 2:
# a A a
# Sample Output 2:
# a 3
'''
s = input().lower().split()
s.sort()    # это лишнее скорее всего, и без сортировки вроде работает) 
for x in s:
    if s.count(x) == 1:
        print(x, s.count(x))    # печатаем элемент и его количество
    else:
        print(x, s.count(x))
        for k in range(1, s.count(x)):  # если их несколько, то приходится  
            s.remove(x)                 # удалять лишние несколько раз
# НЕ МОЙ КОД, в 2 строки через множество SET()!
# s = input().lower().split()
# [print(x, s.count(x)) for x in set(s)]
'''

# НЕ РЕШИЛ
# Задача №3
# Напишите программу, которая считывает строку с числом n, которое задаёт количество
# чисел, которые нужно считать. Далее считывает n строк с числами x[i]​, по одному
# числу в каждой строке. Итого будет (n+1) строк. При считывании числа x[i]​ программа
# должна на отдельной строке вывести значение f(x[i]). Функция f(x) уже реализована и
# доступна для вызова. Функция вычисляется достаточно долго и зависит только от
# переданного аргумента x. Для того, чтобы уложиться в ограничение по времени, нужно
# избежать повторного вычисления значений.
# Sample Input:
# 5     ввод n-кол-во чисел
# 5     ввод 1 числа
# 12    ввод 2 числа
# 9     ввод 3 числа
# 20    ввод 4 числа
# 12    ввод 5 числа
# Sample Output:
# 11    вывод функции ф(5)
# 41    вывод функции ф(12)
# 47    вывод функции ф(9)
# 61    вывод функции ф(20)
# 41    вывод функции ф(12)
''' 
def f(x):
    return x


n = int(input())  # кол-во чисел
key = [0] * n
d = {}
x = 0
for i in range(0, n):
    key[i] = int(input())
    d[i] = key[i]
    if d[i] in d.values():
        print(f(x))
print(d.values())
'''

# https://stepik.org/lesson/3363/step/2?unit=1135
# 3.4 Файловый ввод/вывод
# Задача 1
# Напишите программу, которая считывает из файла строку, соответствующую тексту,
# сжатому с помощью кодирования повторов, и производит обратную операцию, получая
# исходный текст. Запишите полученный текст в файл и прикрепите его, как ответ
# на это задание. В исходном тексте не встречаются цифры, так что код однозначно
# интерпретируем. Это первое задание типа Dataset Quiz. В таких заданиях после
# нажатия "Start Quiz" у вас появляется ссылка "download your dataset". Используйте
# эту ссылку для того, чтобы загрузить файл со входными данными к себе на компьютер.
# Запустите вашу программу, используя этот файл в качестве входных данных. Выходной
# файл, который при этом у вас получится, надо отправить в качестве ответа на эту задачу.
# Sample Input:
# a3b4c2e10b1
# Sample Output:
# aaabbbbcceeeeeeeeeeb

# import os
# a = os.path.join('.', '/Python', 'dataset_3363_2.txt')
# with open (a) as txt:
#     s = txt.readline().strip()
# СКАЧАЛ ФАЙЛ, ОТКРЫЛ БЛОКНОТОМ, ТАМ СТРОКА, ВСТАВИЛ ЕЕ СЮДА КАК s=input() см.ниже, ДАЛЕЕ
# СКОПИРОВАЛ И ВСТАВИЛ ПОЛУЧЕННУЮ СТРОКУ В ОКНО НА СТЕПИКО, ПОЛУЧИЛ 2 БАЛЛА:))
# ПРИМЕР: <<a101>>
'''
b = c = ''      # обнуление строк
k = 1           # счетчик для списков
m = 0           # переменная, сколько надо печатать символов в итоге, например a101, m=101
s = input()                      # для проверки, сам ввожу, ПО ИДЕЕ НАДО УБРАТЬ
v1 = ['']*(len(s))  # создаем список букв (a)
v2 = ['']*(len(s))  # создаем список цифр (101)
for i in range(len(s)):
    if s[i] in '1234567890':    # если символ-число, то начинаем складывать '1+0+1'
        b = b + s[i]            # работаем со строками!
        c = s[i]                # работаем со строками!
        m = int(b)              # переводим строку '101' в число 101
    else:
        v2[k-1] = m             # запоминаем полученное число 101
        v1[k] = s[i]            # запоминаем букву
        k += 1
        m = 0
        b = ''
    v2[k-1] = m
for i in range(1, k):
    print(v1[i]*v2[i], end='')

#with open (a, 'w') as out:     ЭТА ШТУКА ЧТО-ТО НЕ РАБОТАЕТ(((
#    out.write(s)
#    print(s)
'''

# 3.4 Файловый ввод/вывод
# Задача 2
# Напишите программу, которая считывает текст из файла (в файле может быть
# больше одной строки) и выводит самое частое слово в этом тексте и через
# пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести
# лексикографически первое (можно использовать оператор < для строк).
# В качестве ответа укажите вывод программы, а не саму программу. Слова,
# написанные в разных регистрах, считаются одинаковыми.
# Sample Input:
# abc a bCd bC AbC BC BCD bcd ABC
# Sample Output:
# abc 3
'''
import os
a = os.path.join('.', '/Python', 'txt.txt') # файл скачиваем и кидаем в папку С:/Python с именем txt.txt
with open (a) as txt:
    s = txt.read().lower().strip().split()               # отступы! забываю постоянно тут их
    # s = txt.readlines().strip()       # пишут в комментах что можно и так, не проверял
#s = input().lower().split()     # все в нижн.регистре с разделителем-пробелом (если не читать из файла)
# -------------------------------------------------------
str = {}                        # будем делать через словарь, создаем
m = 0                           # счетчик числа слов
for x in set(s):                # перебираем слова в множестве
    m = s.count(x)              # выводит сразу сколько слов таких
    str[m] = x                  # заносим в словарь, где ключ - текущее m, а значение - текущее слово Х
max_key = max(str.keys())       # находим максимальное число среди ключей созданного словаря str
print(str[max_key], max_key)    # выводим значение по макс.ключу и число(сам ключ)
# --------------------------------------------------------------
print(len(s))                   # решил еще строчку добавить - сколько всего слов в тексте
#with open (a, 'w') as out:     # ЭТА ШТУКА ЧТО-ТО НЕ РАБОТАЕТ(
#    out.write(str[max_key] + ' ' + str(max_key))
'''

'''
#НЕ МОЙ КОД, НО ОН ПРАКТИЧЕСКИ САМЫЙ БЫСТРЫЙ, ПОТОМУ ЧТО НЕТ COUNT!)
import os
a = os.path.join('.', '/Python', 'Библия.txt') # файл скачиваем и кидаем в папку С:/Python с именем txt.txt
s, d, m, w = str(), dict(), 0, str()
with open(a) as f:
    s = f.read().lower().strip().split()
s.sort()
for word in s:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
for word in d:
    if d[word] > m:
        m = d[word]
        w = word
print(m, w)
print(len(s))
'''

# 3.4 Файловый ввод/вывод
# Задача 3
# Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой
# строке записана следующая информация: Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
# Поля внутри строки разделены точкой с запятой, оценки — целые числа. Напишите программу, которая считывает
# файл с подобной структурой и для каждого абитуриента выводит его среднюю оценку по этим трём предметам на
# отдельной строке, соответствующей этому абитуриенту. Также в конце файла, на отдельной строке, через пробел
# запишите средние баллы по математике, физике и русскому языку по всем абитуриентам.
# В качестве ответа на задание прикрепите полученный файл со средними оценками.
# Sample Input:
# Петров;85;92;78
# Сидоров;100;88;94
# Иванов;58;72;85
# Sample Output:
# 85.0
# 94.0
# 71.666666667
# 81.0 84.0 85.666666667
'''
import os
a = os.path.join('.', '/Python', 'students.txt') # файл скачиваем и кидаем в папку С:/Python с именем txt.txt
l1 = l2 = l3 = k = 0
with open (a) as txt:
    for line in txt:
        line = line.strip().split(';')
        print ((int(line[1]) + int(line[2]) + int(line[3]))/3)
        l1 += int(line[1])
        l2 += int(line[2])
        l3 += int(line[3])
        k = k + 1
print(l1/k, l2/k, l3/k)
'''
# Набрал после этой задачи 80 баллов и получил Сертификат!))



# КУРС №2 "Python: основы и применение"
# https://stepik.org/lesson/24458/step/9?unit=6765
# 1.2 Модель данных: объекты
# Реализуйте программу, которая будет вычислять количество различных объектов в списке.
# Два объекта a и b считаются различными, если a is b равно False. Вашей программе
# доступна переменная с названием objects, которая ссылается на список, содержащий
# не более 100 объектов. Выведите количество различных объектов в этом списке.
'''
ans = 0
# objects = [1, 2, 1, 5, True, False, True, 'false', [], [1,2], [1,2]] #строка для внутреннего тестирования
s = []
for obj in objects: # доступная переменная objects
    if obj not in s:
        s.append(obj)
        ans += 1
print(ans)
'''
# НЕ МОЕ РЕШЕНИЕ, в одну строку Карл!: print(len(set(map(id, objects))))

# https://stepik.org/lesson/24459/step/9?unit=6764
# 1.3 Функции и стек вызовов
# Напишите реализацию функции closest_mod_5, принимающую в качестве единственного
# аргумента целое число x и возвращающую самое маленькое целое число y, такое что:
#     y больше или равно x
#     y делится нацело на 5
'''
def closest_mod_5(x):
    if x % 5 != 0:
        x = ((x // 5) + 1) * 5
    return (x)
'''

''' Не мой код, проверка на скорость: какая функция быстрее,с позиционными агрументами или списком
import time

def one(a, b, c):
    return a + b + c

def two(*args):
    return args[0] + args[1] + args[2]

count = 9000000
_startTime = time.time()
for num in range(count):
    one(1, 2, 3)
print("Positional test:", time.time() - _startTime)

_startTime = time.time()
for num in range(count):
    two(1, 2, 3)
print("Positional args as list test:", time.time() - _startTime)
'''





# =====================================================================================================
# ИГРА ТЕТРИС, надо установить PyQt5!
'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, random
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor


class Tetris(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.tboard = Board(self)
        self.setCentralWidget(self.tboard)

        self.statusbar = self.statusBar()
        self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)

        self.tboard.start()

        self.resize(180, 380)
        self.center()
        self.setWindowTitle('Tetris')
        self.show()


    def center(self):

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2,
            (screen.height()-size.height())/2)


class Board(QFrame):

    msg2Statusbar = pyqtSignal(str)

    BoardWidth = 10
    BoardHeight = 22
    Speed = 300

    def __init__(self, parent):
        super().__init__(parent)

        self.initBoard()


    def initBoard(self):

        self.timer = QBasicTimer()
        self.isWaitingAfterLine = False

        self.curX = 0
        self.curY = 0
        self.numLinesRemoved = 0
        self.board = []

        self.setFocusPolicy(Qt.StrongFocus)
        self.isStarted = False
        self.isPaused = False
        self.clearBoard()


    def shapeAt(self, x, y):
        return self.board[(y * Board.BoardWidth) + x]


    def setShapeAt(self, x, y, shape):
        self.board[(y * Board.BoardWidth) + x] = shape


    def squareWidth(self):
        return self.contentsRect().width() // Board.BoardWidth


    def squareHeight(self):
        return self.contentsRect().height() // Board.BoardHeight


    def start(self):

        if self.isPaused:
            return

        self.isStarted = True
        self.isWaitingAfterLine = False
        self.numLinesRemoved = 0
        self.clearBoard()

        self.msg2Statusbar.emit(str(self.numLinesRemoved))

        self.newPiece()
        self.timer.start(Board.Speed, self)


    def pause(self):

        if not self.isStarted:
            return

        self.isPaused = not self.isPaused

        if self.isPaused:
            self.timer.stop()
            self.msg2Statusbar.emit("paused")

        else:
            self.timer.start(Board.Speed, self)
            self.msg2Statusbar.emit(str(self.numLinesRemoved))

        self.update()


    def paintEvent(self, event):

        painter = QPainter(self)
        rect = self.contentsRect()

        boardTop = rect.bottom() - Board.BoardHeight * self.squareHeight()

        for i in range(Board.BoardHeight):
            for j in range(Board.BoardWidth):
                shape = self.shapeAt(j, Board.BoardHeight - i - 1)

                if shape != Tetrominoe.NoShape:
                    self.drawSquare(painter,
                        rect.left() + j * self.squareWidth(),
                        boardTop + i * self.squareHeight(), shape)

        if self.curPiece.shape() != Tetrominoe.NoShape:

            for i in range(4):

                x = self.curX + self.curPiece.x(i)
                y = self.curY - self.curPiece.y(i)
                self.drawSquare(painter, rect.left() + x * self.squareWidth(),
                    boardTop + (Board.BoardHeight - y - 1) * self.squareHeight(),
                    self.curPiece.shape())


    def keyPressEvent(self, event):

        if not self.isStarted or self.curPiece.shape() == Tetrominoe.NoShape:
            super(Board, self).keyPressEvent(event)
            return

        key = event.key()

        if key == Qt.Key_P:
            self.pause()
            return

        if self.isPaused:
            return

        elif key == Qt.Key_Left:
            self.tryMove(self.curPiece, self.curX - 1, self.curY)

        elif key == Qt.Key_Right:
            self.tryMove(self.curPiece, self.curX + 1, self.curY)

        elif key == Qt.Key_Down:
            self.tryMove(self.curPiece.rotateRight(), self.curX, self.curY)

        elif key == Qt.Key_Up:
            self.tryMove(self.curPiece.rotateLeft(), self.curX, self.curY)

        elif key == Qt.Key_Space:
            self.dropDown()

        elif key == Qt.Key_D:
            self.oneLineDown()

        else:
            super(Board, self).keyPressEvent(event)


    def timerEvent(self, event):

        if event.timerId() == self.timer.timerId():

            if self.isWaitingAfterLine:
                self.isWaitingAfterLine = False
                self.newPiece()
            else:
                self.oneLineDown()

        else:
            super(Board, self).timerEvent(event)


    def clearBoard(self):

        for i in range(Board.BoardHeight * Board.BoardWidth):
            self.board.append(Tetrominoe.NoShape)


    def dropDown(self):

        newY = self.curY

        while newY > 0:

            if not self.tryMove(self.curPiece, self.curX, newY - 1):
                break

            newY -= 1

        self.pieceDropped()


    def oneLineDown(self):

        if not self.tryMove(self.curPiece, self.curX, self.curY - 1):
            self.pieceDropped()


    def pieceDropped(self):

        for i in range(4):

            x = self.curX + self.curPiece.x(i)
            y = self.curY - self.curPiece.y(i)
            self.setShapeAt(x, y, self.curPiece.shape())

        self.removeFullLines()

        if not self.isWaitingAfterLine:
            self.newPiece()


    def removeFullLines(self):

        numFullLines = 0
        rowsToRemove = []

        for i in range(Board.BoardHeight):

            n = 0
            for j in range(Board.BoardWidth):
                if not self.shapeAt(j, i) == Tetrominoe.NoShape:
                    n = n + 1

            if n == 10:
                rowsToRemove.append(i)

        rowsToRemove.reverse()


        for m in rowsToRemove:

            for k in range(m, Board.BoardHeight):
                for l in range(Board.BoardWidth):
                        self.setShapeAt(l, k, self.shapeAt(l, k + 1))

        numFullLines = numFullLines + len(rowsToRemove)

        if numFullLines > 0:

            self.numLinesRemoved = self.numLinesRemoved + numFullLines
            self.msg2Statusbar.emit(str(self.numLinesRemoved))

            self.isWaitingAfterLine = True
            self.curPiece.setShape(Tetrominoe.NoShape)
            self.update()


    def newPiece(self):

        self.curPiece = Shape()
        self.curPiece.setRandomShape()
        self.curX = Board.BoardWidth // 2 + 1
        self.curY = Board.BoardHeight - 1 + self.curPiece.minY()

        if not self.tryMove(self.curPiece, self.curX, self.curY):

            self.curPiece.setShape(Tetrominoe.NoShape)
            self.timer.stop()
            self.isStarted = False
            self.msg2Statusbar.emit("Game over")



    def tryMove(self, newPiece, newX, newY):

        for i in range(4):

            x = newX + newPiece.x(i)
            y = newY - newPiece.y(i)

            if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight:
                return False

            if self.shapeAt(x, y) != Tetrominoe.NoShape:
                return False

        self.curPiece = newPiece
        self.curX = newX
        self.curY = newY
        self.update()

        return True


    def drawSquare(self, painter, x, y, shape):

        colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]

        color = QColor(colorTable[shape])
        painter.fillRect(x + 1, y + 1, self.squareWidth() - 2,
            self.squareHeight() - 2, color)

        painter.setPen(color.lighter())
        painter.drawLine(x, y + self.squareHeight() - 1, x, y)
        painter.drawLine(x, y, x + self.squareWidth() - 1, y)

        painter.setPen(color.darker())
        painter.drawLine(x + 1, y + self.squareHeight() - 1,
            x + self.squareWidth() - 1, y + self.squareHeight() - 1)
        painter.drawLine(x + self.squareWidth() - 1,
            y + self.squareHeight() - 1, x + self.squareWidth() - 1, y + 1)


class Tetrominoe(object):
    NoShape = 0
    ZShape = 1
    SShape = 2
    LineShape = 3
    TShape = 4
    SquareShape = 5
    LShape = 6
    MirroredLShape = 7

class Shape(object):
    coordsTable = (
        ((0, 0),     (0, 0),     (0, 0),     (0, 0)),
        ((0, -1),    (0, 0),     (-1, 0),    (-1, 1)),
        ((0, -1),    (0, 0),     (1, 0),     (1, 1)),
        ((0, -1),    (0, 0),     (0, 1),     (0, 2)),
        ((-1, 0),    (0, 0),     (1, 0),     (0, 1)),
        ((0, 0),     (1, 0),     (0, 1),     (1, 1)),
        ((-1, -1),   (0, -1),    (0, 0),     (0, 1)),
        ((1, -1),    (0, -1),    (0, 0),     (0, 1))
    )

    def __init__(self):
        self.coords = [[0,0] for i in range(4)]
        self.pieceShape = Tetrominoe.NoShape
        self.setShape(Tetrominoe.NoShape)

    def shape(self):
        return self.pieceShape

    def setShape(self, shape):
        table = Shape.coordsTable[shape]
        for i in range(4):
            for j in range(2):
                self.coords[i][j] = table[i][j]
        self.pieceShape = shape


    def setRandomShape(self):
        self.setShape(random.randint(1, 7))

    def x(self, index):
        return self.coords[index][0]

    def y(self, index):
        return self.coords[index][1]

    def setX(self, index, x):
        self.coords[index][0] = x

    def setY(self, index, y):
        self.coords[index][1] = y


    def minX(self):

        m = self.coords[0][0]
        for i in range(4):
            m = min(m, self.coords[i][0])

        return m


    def maxX(self):
        m = self.coords[0][0]
        for i in range(4):
            m = max(m, self.coords[i][0])
        return m


    def minY(self):
        m = self.coords[0][1]
        for i in range(4):
            m = min(m, self.coords[i][1])
        return m

    def maxY(self):
        m = self.coords[0][1]
        for i in range(4):
            m = max(m, self.coords[i][1])
        return m


    def rotateLeft(self):
        if self.pieceShape == Tetrominoe.SquareShape:
            return self
        result = Shape()
        result.pieceShape = self.pieceShape

        for i in range(4):

            result.setX(i, self.y(i))
            result.setY(i, -self.x(i))
        return result


    def rotateRight(self):
        if self.pieceShape == Tetrominoe.SquareShape:
            return self
        result = Shape()
        result.pieceShape = self.pieceShape

        for i in range(4):
            result.setX(i, -self.y(i))
            result.setY(i, self.x(i))
        return result

if __name__ == '__main__':
    app = QApplication([])
    tetris = Tetris()
    sys.exit(app.exec_())
'''
# КОНЕЦ ИГРЫ ТЕТРИС ==============================================================================================





#  3.6 Установка дополнительных модулей
# https://stepik.org/lesson/3378/step/2?auth=login&unit=961
# Скачайте файл. В нём указан адрес другого файла, который нужно скачать с использованием
# модуля requests и посчитать число строк в нём. Используйте функцию get для получения файла
# (имеет смысл вызвать метод strip к передаваемому параметру, чтобы убрать пробельные символы
# по краям). После получения файла вы можете проверить результат, обратившись к полю text.
# Если результат работы скрипта не принимается, проверьте поле url на правильность. Для
# подсчёта количества строк разбейте текст с помощью метода splitlines. В поле ответа введите
# одно число или отправьте файл, содержащий одно число.
'''
import requests
r = requests.get('https://stepic.org/media/attachments/course67/3.6.2/324.txt')
print(len(r.text.splitlines()))
'''
'''не мой код, тут еще строка открытия файла и чтения из него строки адреса
import requests
with open('dataset_3378_2.txt') as inf:
    r = requests.get(inf.readline().strip())
    print(len(r.text.splitlines()))
'''

# НЕ РЕШАЛ!!!! -----------------------------------------------------------------
# Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
# Первое слово в тексте последнего файла: "We". Скачайте предложенный файл.
# В нём содержится ссылка на первый файл из этого набора.
# Все файлы располагаются в каталоге по адресу:
# https://stepic.org/media/attachments/course67/3.6.3/
# Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.
'''
import requests
with open('dataset_3378_2.txt') as inf:
    r = requests.get(inf.readline().strip())
    print(len(r.text.splitlines()))
'''
# ---------------------------------------------------------------------------------------








# Python: основы и применение (мой второй курс)
# Прогресс по курсу:  34/300
# https://stepik.org/lesson/24461/step/8?auth=login&unit=6767
# 1.5 Введение в классы
# Реализуйте класс MoneyBox, для работы с виртуальной копилкой. Каждая копилка
# имеет ограниченную вместимость, которая выражается целым числом – количеством
# монет, которые можно положить в копилку. Класс должен поддерживать информацию
# о количестве монет в копилке, предоставлять возможность добавлять монеты в
# копилку и узнавать, можно ли добавить в копилку ещё какое-то количество монет,
# не превышая ее вместимость. При создании копилки, число монет в ней равно 0.
# Гарантируется: метод add(self,v) будет вызываться только если can_add(self,v) – True﻿.
'''
class MoneyBox:
    def __init__(self, capacity):       # конструктор с аргументом – вместимость копилки
        self.capacity = capacity
        self.count = 0

    def can_add(self, v):               # True, если можно добавить v монет, False иначе
        if self.count <= self.capacity - v:
            return True
        else:
            return False

    def add(self, v):                   # положить v монет в копилку
        if self.can_add(v) == True:
            self.count += v
            return True
        else:
            return False
# далее просто блок проверки:
x = MoneyBox(10)
x.add(5)
x.add(9)
x.add(3)
'''
# ----------------------------------------------------------------------------
# Python: основы и применение
# Прогресс по курсу:  44/300
# 1.5 Введение в классы
# Вам дается последовательность целых чисел и вам нужно ее обработать и вывести
# на экран сумму первой пятерки чисел из этой последовательности, затем сумму второй
# пятерки, и т. д. Но последовательность не дается вам сразу целиком. С течением
# времени к вам поступают её последовательные части. Например, сначала первые три
# элемента, потом следующие шесть, потом следующие два и т. д. Реализуйте класс Buffer,
# который будет накапливать в себе элементы последовательности и выводить сумму
# пятерок последовательных элементов по мере их накопления. Одним из требований
# к классу является то, что он не должен хранить в себе больше элементов, чем ему
# действительно необходимо, т. е. он не должен хранить элементы, которые уже вошли
# в пятерку, для которой была выведена сумма. Класс должен иметь следующий вид
#
# class Buffer:
#     def __init__(self):
#         # конструктор без аргументов
#     
#     def add(self, *a):
#         # добавить следующую часть последовательности
#
#     def get_current_part(self):
#         # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
#         # добавлены
# Обратите внимание, что во время выполнения метода add выводить сумму пятерок
# может потребоваться несколько раз до тех пор, пока в буфере не останется менее
# пяти элементов.

# ---------------------------------------------------------------------------------

'''
class Base:
    def __init__(self):
        self.val = 0

    def add_one(self):
        self.val += 1

    def add_many(self, x):
        for i in range(x):
            self.add_one()

class Derived(Base):
    def add_one(self):
        self.val += 10


a = Derived()
a.add_one()

b = Derived()
b.add_many(3)

print(a.val)
print(b.val)
# выведет: 10, 30
'''

'''
class A:
   def foo(self):
      print("A")

class B(A):
   pass

class C(A):
   def foo(self):
      print("C")

class D:
   def foo(self):
      print("D")

class E(B, C, D):
   pass

E().foo()
# выведет: C
'''


'''
#Чтение новостных заголовков с сайта Хакер.ру
import requests
from bs4 import BeautifulSoup

response = requests.get("https://xakep.ru/2019/09/04/sportcat/")
page = response.text

soup = BeautifulSoup(page, 'html.parser')

headings = map(lambda e: e.text, soup.select("h3.entry-title a span"))
for h in headings:
  print(h)
'''




'''
Не рабоает, проблемы с импортом
# Бинарная классификация
Научим нашу нейросеть распознавать, кошка или собака изображены на фото. Это классический пример, 
и к нему в Keras Datasets уже есть необходимый для обучения набор картинок. Иначе нам пришлось бы
вручную создать и классифицировать несколько тысяч фотографий.

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Activation, BatchNormalization, AveragePooling2D
from tensorflow.keras.optimizers import SGD, RMSprop, Adam
## pip install tensorflow-datasets
import tensorflow_datasets as tfds
import tensorflow as tf
import logging
import numpy as np
import time

def dog_cat_model():
  model = Sequential()
  model.add(Conv2D(32, (3, 3), input_shape=(128, 128, 3), activation='relu'))
  model.add(MaxPooling2D(pool_size=(2, 2)))
  model.add(Conv2D(32, (3, 3), activation='relu'))
  model.add(MaxPooling2D(pool_size=(2, 2)))
  model.add(Flatten())
  model.add(Dense(units=128, activation='relu'))
  model.add(Dense(units=1, activation='sigmoid'))
  model.compile(optimizer=Adam(),
    loss='binary_crossentropy',
    metrics=['accuracy'])
  return model

def dog_cat_train(model):
  splits = tfds.Split.TRAIN.subsplit(weighted=(80, 10, 10))
  (cat_train, cat_valid, cat_test), info = tfds.load('cats_vs_dogs',
    split=list(splits), with_info=True, as_supervised=True)

  def pre_process_image(image, label):
    image = tf.cast(image, tf.float32)
    image = image/255.0
    image = tf.image.resize(image, (128, 128))
    return image, label

  BATCH_SIZE = 32
  SHUFFLE_BUFFER_SIZE = 1000
  train_batch = cat_train.map(pre_process_image).shuffle(SHUFFLE_BUFFER_SIZE).repeat().batch(BATCH_SIZE)
  validation_batch = cat_valid.map(pre_process_image).repeat().batch(BATCH_SIZE)
  t_start = time.time()
  model.fit(train_batch, steps_per_epoch=4000, epochs=2,
    validation_data=validation_batch,
    validation_steps=10,
    callbacks=None)
  print("Training done, dT:", time.time() - t_start)

model = dog_cat_model()
dog_cat_train(model)
model.save('dogs_cats.h5')

def dog_cat_predict(model, image_file):
  label_names = ["cat", "dog"]

  img = keras.preprocessing.image.load_img(image_file,
    target_size=(128, 128))
  img_arr = np.expand_dims(img, axis=0) / 255.0
  result = model.predict_classes(img_arr)
  print("Result: %s" % label_names[result[0][0]])

  model = tf.keras.models.load_model('dogs_cats.h5')
dog_cat_predict(model, "cat.png#26759185")
dog_cat_predict(model, "dog1.png#26759185")
dog_cat_predict(model, "dog2.png#26759185")
'''






'''
3a. Задание можно выполнить на любом языке программирования.
Задача: разработать программу, которая на основании данных сервиса https://openweathermap.org/ 
(требует регистрации, достаточно бесплатного плана Free) будет выводить следующие данные для Вашего города:
1. День, с минимальной разницей "ощущаемой" и фактической температуры ночью (с указанием разницы в градусах Цельсия)
2. Максимальную продолжительностью светового дня (считать, как разницу между временем заката и рассвета)
за ближайшие 5 дней (включая текущий), с указанием даты.

import requests
import json
import time

API_KEY = "b702314ab6fb64cab3519c6f2aa8fa23"
long = 49.1221   # долгота Казани
lati  = 55.7887   # широта Казани
temp_night = []   # список ночных температур
temp_feels_like_night = []   # список ночных "ощущаемых" температур
temp_diff = []   # разница температур
sunrise = []   # список времени восхода
sunset = []   # список времени заката
sun_day = []   # список продолжительности светового дня

api_response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat="
     f"{lati}&lon={long}&exclude=minutely,hourly,alerts&appid={API_KEY}&units=metric").text
json_response = json.loads(api_response)

for i in range(5):
    temp_night.append(json_response["daily"][i]["temp"]["night"])
    temp_diff.append(json_response["daily"][i]["temp"]["night"])
    temp_feels_like_night.append(json_response["daily"][i]["feels_like"]["night"])
    temp_diff[i] = abs((temp_night[i]) - (temp_feels_like_night[i]))
    sunrise.append(json_response["daily"][i]["sunrise"])
    sun_day.append(json_response["daily"][i]["sunrise"])
    sunset.append(json_response["daily"][i]["sunset"])
    sun_day[i] = sunset[i] - sunrise[i]

ind = sun_day.index(max(sun_day)) #находим индекс максимума в списке
max_sun_day = time.strftime("%H:%M:%S", time.gmtime(max(sun_day)))
dt = json_response["daily"][ind]["dt"]
max_sun_day_date = time.strftime("%d.%m.%Y", time.gmtime(dt))

print("1) День, с минимальной разницей 'ощущаемой' и фактической температуры ночью -", min(temp_diff), "градусов Цельсия")
print("2) Максимальная продолжительность светового дня равна ", max_sun_day, ", дата", max_sun_day_date)
'''




'''
3.4 Распространённые форматы текстовых файлов: CSV, JSON
Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго
с 2001 года по настоящее время.
Одним из атрибутов преступления является его тип – Primary Type.
Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.
Файл с данными: Crimes.csv

import requests
import json

r = requests.get(f"https://stepik.org/media/attachments/lesson/24473/Crimes.csv")
print(type(r))
requests.

#json_response = json.loads(r)
#print(json_response)
'''

import requests
from bs4 import BeautifulSoup

response = requests.get("https://stepik.org/media/attachments/lesson/209717/1.html")
page = response.text

soup = BeautifulSoup(page, 'html.parser')

headings = map(lambda e: e.text, soup.select("h3.entry-title a span"))
for h in headings:
  print(h)
