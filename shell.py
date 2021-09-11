Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> range(10)
range(0, 10)
>>> r = range(10)
>>> r
range(0, 10)
>>> next(r)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    next(r)
TypeError: 'range' object is not an iterator
>>> def abc(k):
	return k**4

>>> abc(3)
81
>>> a = abc
>>> abc
<function abc at 0x000001FA5F2080D0>
>>> a
<function abc at 0x000001FA5F2080D0>
>>> b = lambda x:x**4
>>> b
<function <lambda> at 0x000001FA5F208160>
>>> lambda x:x**4
<function <lambda> at 0x000001FA5F208280>
>>> a = [6,8,2,5,7,2,81,23,56,7,2,8]
>>> [i*2 for i in a]
[12, 16, 4, 10, 14, 4, 162, 46, 112, 14, 4, 16]
>>> list(map(lambda x:x*2,a))
[12, 16, 4, 10, 14, 4, 162, 46, 112, 14, 4, 16]
>>> list(filter(lambda x:x%2 == 1, a))
[5, 7, 81, 23, 7]
>>> [i for i in a if i%2==1]
[5, 7, 81, 23, 7]
>>> list(map(lambda x:x**2,a))
[36, 64, 4, 25, 49, 4, 6561, 529, 3136, 49, 4, 64]
>>> list(map(lambda x:x%2 == 1, a))
[False, False, False, True, True, False, True, True, False, True, False, False]
>>> 0.2+0.1
0.30000000000000004
>>> round(0.2,1)
0.2
>>> round(0.2,1)+round(0.1,1)
0.30000000000000004
>>> dec(0.2)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    dec(0.2)
NameError: name 'dec' is not defined
>>> 
>>> 
>>> m = map(lambda x:x*2,a)
>>> m
<map object at 0x000001FA5F1E5A60>
>>> e = enumerate(a)
>>> z = zip(a,a)
>>> e
<enumerate object at 0x000001FA5F04D980>
>>> z
<zip object at 0x000001FA5F14B440>
>>> 
>>> filter(lambda x:x%2 == 1, a)
<filter object at 0x000001FA5F1F40D0>
>>> f = filter(lambda x:x%2 == 1, a)
>>> 
>>> 
>>> next(m)
12
>>> next(m)
16
>>> next(m)
4
>>> next(m)
10
>>> next(m)
14
>>> next(m)
4
>>> next(m)
162
>>> next(m)
46
>>> next(m)
112
>>> next(m)
14
>>> next(m)
4
>>> next(m)
16
>>> next(m)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    next(m)
StopIteration
>>> list(m)
[]
>>> m = map(lambda x:x*2,a)
>>> list(m)
[12, 16, 4, 10, 14, 4, 162, 46, 112, 14, 4, 16]
>>> list(m)
[]
>>> list(m)
[]
>>> next(m)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    next(m)
StopIteration
>>> m = map(lambda x:x*2,a)
>>> next(m)
12
>>> next(m)
16
>>> list(m)
[4, 10, 14, 4, 162, 46, 112, 14, 4, 16]
>>> list(m)
[]
>>> m = map(lambda x:x*2,a)
>>> for i in m:
	print(i)

	
12
16
4
10
14
4
162
46
112
14
4
16
>>> def mygen():
	yield 4
	yield 5

	
>>> mygen
<function mygen at 0x000001FA5F20E4C0>
>>> g = mygen()
>>> g
<generator object mygen at 0x000001FA5F1067B0>
>>> def abc(n):
	return n**3

>>> m = map(abc,a)
>>> list(m)
[216, 512, 8, 125, 343, 8, 531441, 12167, 175616, 343, 8, 512]
>>> 
>>> next(g)
4
>>> next(g)
5
>>> def tabgen(n):
	for i in range(1,11):
		yield n*i

		
>>> t =tabgen(3)
>>> t
<generator object tabgen at 0x000001FA5F205C80>
>>> next(t)
3
>>> next(t)
6
>>> next(t)
9
>>> next(t)
12
>>> list(t)
[15, 18, 21, 24, 27, 30]
>>> 
>>> n=5
>>> [n*i for i in range(1,11)]
[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
>>> gg = (n*i for i in range(1,11))
>>> gg
<generator object <genexpr> at 0x000001FA5F205C10>
>>> for i in gg:
	print(i)

	
5
10
15
20
25
30
35
40
45
50
>>> id(a)
2174849280704
>>> ord('a')
97
>>> ord('A')
65
>>> ord('0')
48
>>> chr(48)
'0'
>>> bin(4)
'0b100'
>>> # min, max, sum
>>> sorted(a)
[2, 2, 2, 5, 6, 7, 7, 8, 8, 23, 56, 81]
>>> a
[6, 8, 2, 5, 7, 2, 81, 23, 56, 7, 2, 8]
>>> 