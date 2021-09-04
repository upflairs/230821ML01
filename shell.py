Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/hp/Desktop/UFT/23082021MLAI01/day10/script.py
name,age,subject
kishore,20,science
rahul,19,physics
ajay,20,science
vineeta sharma,18,science
>>> r
'name,age,subject\nkishore,20,science\nrahul,19,physics\najay,20,science\nvineeta sharma,18,science'
>>> d = {}
>>> r.split('\n')
['name,age,subject', 'kishore,20,science', 'rahul,19,physics', 'ajay,20,science', 'vineeta sharma,18,science']
>>> r = r.split('\n')
>>> r
['name,age,subject', 'kishore,20,science', 'rahul,19,physics', 'ajay,20,science', 'vineeta sharma,18,science']
>>> r[0]
'name,age,subject'
>>> r[0].split(',')
['name', 'age', 'subject']
>>> keys = r[0].split(',')
>>> d = {k:[] for k in keys}
>>> d
{'name': [], 'age': [], 'subject': []}
>>> 
>>> r[1:]
['kishore,20,science', 'rahul,19,physics', 'ajay,20,science', 'vineeta sharma,18,science']
>>> keys = r.pop(0).split(',')
>>> r
['kishore,20,science', 'rahul,19,physics', 'ajay,20,science', 'vineeta sharma,18,science']
>>> values = [i.split(',') for i in r]
>>> values
[['kishore', '20', 'science'], ['rahul', '19', 'physics'], ['ajay', '20', 'science'], ['vineeta sharma', '18', 'science']]
>>> 
>>> dict(zip(keys,values))
{'name': ['kishore', '20', 'science'], 'age': ['rahul', '19', 'physics'], 'subject': ['ajay', '20', 'science']}
>>> list(zip(values))
[(['kishore', '20', 'science'],), (['rahul', '19', 'physics'],), (['ajay', '20', 'science'],), (['vineeta sharma', '18', 'science'],)]
>>> list(zip(*values))
[('kishore', 'rahul', 'ajay', 'vineeta sharma'), ('20', '19', '20', '18'), ('science', 'physics', 'science', 'science')]
>>> dict(zip(keys,zip(*values)))
{'name': ('kishore', 'rahul', 'ajay', 'vineeta sharma'), 'age': ('20', '19', '20', '18'), 'subject': ('science', 'physics', 'science', 'science')}
>>> 
= RESTART: C:/Users/hp/Desktop/UFT/23082021MLAI01/day10/script.py
['name,age,subject', 'kishore,20,science', 'rahul,19,physics', 'ajay,20,science', 'vineeta sharma,18,science']
{'name': ('kishore', 'rahul', 'ajay', 'vineeta sharma'), 'age': ('20', '19', '20', '18'), 'subject': ('science', 'physics', 'science', 'science')}
>>> 
>>> 
>>> d + d
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    d + d
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> e = {'ekor':[2,34,6,2]}
>>> d
{'name': ('kishore', 'rahul', 'ajay', 'vineeta sharma'), 'age': ('20', '19', '20', '18'), 'subject': ('science', 'physics', 'science', 'science')}
>>> e
{'ekor': [2, 34, 6, 2]}
>>> **d
SyntaxError: invalid syntax
>>> {**d}
{'name': ('kishore', 'rahul', 'ajay', 'vineeta sharma'), 'age': ('20', '19', '20', '18'), 'subject': ('science', 'physics', 'science', 'science')}
>>> {d}
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    {d}
TypeError: unhashable type: 'dict'
>>> {[4,5,6],6}
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    {[4,5,6],6}
TypeError: unhashable type: 'list'
>>> d
{'name': ('kishore', 'rahul', 'ajay', 'vineeta sharma'), 'age': ('20', '19', '20', '18'), 'subject': ('science', 'physics', 'science', 'science')}
>>> 
>>> {**d, **e}
{'name': ('kishore', 'rahul', 'ajay', 'vineeta sharma'), 'age': ('20', '19', '20', '18'), 'subject': ('science', 'physics', 'science', 'science'), 'ekor': [2, 34, 6, 2]}
>>> f = {'ekor':'kuch bhi'}
>>> {**e, **f}
{'ekor': 'kuch bhi'}
>>> 
>>> zip(e,d)
<zip object at 0x000001FD1143B6C0>
>>> list(zip(e,d))
[('ekor', 'name')]
>>> s='hello'
>>> b='niche'
>>> list(zip(s,b))
[('h', 'n'), ('e', 'i'), ('l', 'c'), ('l', 'h'), ('o', 'e')]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
= RESTART: C:/Users/hp/Desktop/UFT/23082021MLAI01/day10/script.py
['name,age,subject', 'kishore,20,science', 'rahul,19,physics', 'ajay,20,science', 'vineeta sharma,18,science']
{'name': ('kishore', 'rahul', 'ajay', 'vineeta sharma'), 'age': ('20', '19', '20', '18'), 'subject': ('science', 'physics', 'science', 'science')}
{'name': ('kishore', 'rahul', 'ajay', 'vineeta sharma'), 'age': ('20', '19', '20', '18'), 'subject': ('science', 'physics', 'science', 'science'), 'ekor': [2, 34, 6, 2]}
>>> 
= RESTART: C:/Users/hp/Desktop/UFT/23082021MLAI01/day10/script.py
>>> 
= RESTART: C:/Users/hp/Desktop/UFT/23082021MLAI01/day10/script.py
>>> 
= RESTART: C:\Users\hp\Desktop\UFT\23082021MLAI01\day10\script.py
>>> first()
hi
hello
>>> k = first()
hi
hello
>>> k
>>> print(k)
None
>>> 
>>> second()
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    second()
TypeError: second() missing 1 required positional argument: 'x'
>>> second(45)
90
>>> k = second(45)
90
>>> k
>>> 
>>> third()
'hello'
>>> k = third()
>>> k
'hello'
>>> 
= RESTART: C:\Users\hp\Desktop\UFT\23082021MLAI01\day10\script.py
>>> k = third()
wow
>>> k
'hello'
>>> 
= RESTART: C:\Users\hp\Desktop\UFT\23082021MLAI01\day10\script.py
>>> k = third()
wow
>>> k
'hello'
>>> 
>>> m = fourth(56)
>>> m
112
>>> x
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> 
= RESTART: C:\Users\hp\Desktop\UFT\23082021MLAI01\day10\script.py
Traceback (most recent call last):
  File "C:\Users\hp\Desktop\UFT\23082021MLAI01\day10\script.py", line 53, in <module>
    print(x)
NameError: name 'x' is not defined
>>> 
= RESTART: C:\Users\hp\Desktop\UFT\23082021MLAI01\day10\script.py
10
34
10
10
>>> 
= RESTART: C:\Users\hp\Desktop\UFT\23082021MLAI01\day10\script.py
10
20
10
>>> 
= RESTART: C:\Users\hp\Desktop\UFT\23082021MLAI01\day10\script.py
10
20
20
>>> 
= RESTART: C:\Users\hp\Desktop\UFT\23082021MLAI01\day10\script.py
10
30 20
20
>>> 
= RESTART: C:\Users\hp\Desktop\UFT\23082021MLAI01\day10\script.py
10
30
30 20
20
>>> 
= RESTART: C:\Users\hp\Desktop\UFT\23082021MLAI01\day10\script.py
10
200
30 20
20
>>> 
= RESTART: C:\Users\hp\Desktop\UFT\23082021MLAI01\day10\script.py
10
30 20
200
20
>>> 
= RESTART: C:\Users\hp\Desktop\UFT\23082021MLAI01\day10\script.py
10
30 20
30
20
>>> 
= RESTART: C:\Users\hp\Desktop\UFT\23082021MLAI01\day10\script.py
10
30 20
200
20
>>> 
= RESTART: C:\Users\hp\Desktop\UFT\23082021MLAI01\day10\script.py
10
30 20
200
20
>>> 
= RESTART: C:\Users\hp\Desktop\UFT\23082021MLAI01\day10\script.py
10
30 20
200
200
20
>>> 
= RESTART: C:\Users\hp\Desktop\UFT\23082021MLAI01\day10\script.py
>>> five(3,4,6)
27
>>> five(3,4)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    five(3,4)
TypeError: five() missing 1 required positional argument: 'z'
>>> five(5)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    five(5)
TypeError: five() missing 2 required positional arguments: 'y' and 'z'
>>> 
= RESTART: C:\Users\hp\Desktop\UFT\23082021MLAI01\day10\script.py
>>> six(5,8,2)
(21, 3, 16)
>>> a,b,c = six(7,3,87)
>>> a
268
>>> b
-80
>>> c
261
>>> a,b,c = six(5,8,2)
>>> a
21
>>> b
3
>>> c
16
>>> # keyword arguments
>>> five(5,87,3)
266
>>> five(x=20,z=30,y=3)
110
>>> five(20,30,3)
110
>>> 
= RESTART: C:\Users\hp\Desktop\UFT\23082021MLAI01\day10\script.py
>>> five(x=20,z=30,y=3)
690
>>> five(20,30,3)
150
>>> 
= RESTART: C:\Users\hp\Desktop\UFT\23082021MLAI01\day10\script.py
>>> seven(20,30,3)
150
>>> seven(20,30)
50
>>> five(20,30)
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    five(20,30)
TypeError: five() missing 1 required positional argument: 'z'
>>> 
= RESTART: C:\Users\hp\Desktop\UFT\23082021MLAI01\day10\script.py
>>> seven()
0
>>> seven(5)
5
>>> seven(z=30,x=3)
90
>>> seven(3,4,'hi')
'hihihihihihihi'
>>> seven(3,4,[4,'ko'])
[4, 'ko', 4, 'ko', 4, 'ko', 4, 'ko', 4, 'ko', 4, 'ko', 4, 'ko']
>>> 
= RESTART: C:\Users\hp\Desktop\UFT\23082021MLAI01\day10\script.py
>>> eight()
()
>>> eight(4)
(4,)
>>> eight(4,6)
(4, 6)
>>> eight(4,6,6,2,6,2,6,2,5,2,5,2,6,8)
(4, 6, 6, 2, 6, 2, 6, 2, 5, 2, 5, 2, 6, 8)
>>> k = [4,5,7,8]
>>> eight(k)
([4, 5, 7, 8],)
>>> eight(*k)
(4, 5, 7, 8)
>>> 
>>> nine()
{}
>>> nine(name='python', number=10)
{'name': 'python', 'number': 10}
>>> nine(name='python', number=[4,56,8])
{'name': 'python', 'number': [4, 56, 8]}
>>> 