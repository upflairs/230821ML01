Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(4):
	print('*')

	
*
*
*
*
>>> 5+5
10
>>> a = 10
>>> a
10
>>> print(a)
10
>>> a = 15
>>> 
= RESTART: C:/Users/hp/Desktop/UFT/23082021MLAI01/day7/script.py =
>>> 
= RESTART: C:/Users/hp/Desktop/UFT/23082021MLAI01/day7/script.py =
40
>>> a
10
>>> c
40
>>> 50
50
>>> 'wow'
'wow'
>>> 
= RESTART: C:/Users/hp/Desktop/UFT/23082021MLAI01/day7/script.py =
40
>>> 
= RESTART: C:/Users/hp/Desktop/UFT/23082021MLAI01/day7/script.py =
>>> seg1
'\na = 10\nb = 30\nc = a+b\nprint(c)\n'
>>> print(seg1)

a = 10
b = 30
c = a+b
print(c)

>>> exec(seg1)
40
>>> b
30
>>> a
10
>>> c
40
>>> 
= RESTART: C:/Users/hp/Desktop/UFT/23082021MLAI01/day7/script.py =
>>> a
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> b
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    b
NameError: name 'b' is not defined
>>> c
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    c
NameError: name 'c' is not defined
>>> seg1
'\na = 10\nb = 30\nc = a+b\nprint(c)\n'
>>> exec(seg1)
40
>>> a
10
>>> b
30
>>> c
40
>>> print(seg2)

print('nice')
print('what to do??')

>>> exec(seg2)
nice
what to do??
>>> 
= RESTART: C:/Users/hp/Desktop/UFT/23082021MLAI01/day7/script.py =
4 5 6
6 5 4
nice great 40
>>> 
= RESTART: C:/Users/hp/Desktop/UFT/23082021MLAI01/day7/script.py =
4 5 6+6 5 4
nice great 40
>>> 
= RESTART: C:/Users/hp/Desktop/UFT/23082021MLAI01/day7/script.py =
4 5 6+6 5 4
nice&&great&&40
>>> 
= RESTART: C:/Users/hp/Desktop/UFT/23082021MLAI01/day7/script.py =
Enter your name:Peeyush Sanam
>>> a
'Peeyush Sanam'
>>> type(a)
<class 'str'>
>>> 
= RESTART: C:/Users/hp/Desktop/UFT/23082021MLAI01/day7/script.py =
Enter your name:Peeyush Sanam
Enter your age: 29
>>> a
'Peeyush Sanam'
>>> b
'29'
>>> type(b)
<class 'str'>
>>> print(a)
Peeyush Sanam
>>> 
= RESTART: C:/Users/hp/Desktop/UFT/23082021MLAI01/day7/script.py =
Enter your name:Peeyush Sanam
Enter your age: 29
>>> b
29
>>> int('29')
29
>>> int('29.2')
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    int('29.2')
ValueError: invalid literal for int() with base 10: '29.2'
>>> float('29.2')
29.2
>>> eval('29')
29
>>> eval('29.3')
29.3
>>> eval('5-4')
1
>>> float('29')
29.0
>>> 
= RESTART: C:/Users/hp/Desktop/UFT/23082021MLAI01/day7/script.py =
*
**
***
****
*****
>>> or i in range(4):
	print(
		
SyntaxError: invalid syntax
>>> 