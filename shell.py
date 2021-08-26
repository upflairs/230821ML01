Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 5+5
10
>>> 
========= RESTART: C:/Users/hp/Desktop/UFT/23082021MLAI01/day2/code2.py ========
hello
-2
>>> 5-6
-1
>>> a=10
>>> a,b=30,40
>>> a
30
>>> b
40
>>> c=d=e=50
>>> c
50
>>> d
50
>>> e
50
>>> k = 60,70,90
>>> k
(60, 70, 90)
>>> type(k)
<class 'tuple'>
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> len(keyword.kwlist)
36
>>> 7/4
1.75
>>> 7//4
1
>>> 7**4
2401
>>> 14%3
2
>>> a = 10
>>> b = 10.0
>>> c = 10+0j
>>> type(a)
<class 'int'>
>>> type(b)
<class 'float'>
>>> type(c)
<class 'complex'>
>>> print(a,b,c)
10 10.0 (10+0j)
>>> 
>>> float(a)
10.0
>>> int(c)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    int(c)
TypeError: can't convert complex to int
>>> complex(a)
(10+0j)
>>> 
>>> 
>>> c.real
10.0
>>> int(c.real)
10
>>> c.imag
0.0
>>> c.conjugate
<built-in method conjugate of complex object at 0x0000027FC4114E50>
>>> c.conjugate()
(10-0j)
>>> 
>>> #############################
>>> 