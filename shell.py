Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [4,6,32,7,8,3]
>>> b = []
>>> for i in a:
	b+= [i*2]

	
>>> b
[8, 12, 64, 14, 16, 6]
>>> b1 = [i*2 for i in a]
>>> b1
[8, 12, 64, 14, 16, 6]
>>> 
>>> 4/2
2.0
>>> range(18/2)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    range(18/2)
TypeError: 'float' object cannot be interpreted as an integer
>>> range(18//2)
range(0, 9)
>>> 
>>> d = []
>>> for i in a:
	if i<10 and not i%2:
		d+=[i]

		
>>> d
[4, 6, 8]
>>> d1 = [i for i in a if i<10 and not i%2]
>>> d1
[4, 6, 8]
>>> ['{} is odd'.format(i) if i%2 else '{} is even'.format(i) for i in a]
['4 is even', '6 is even', '32 is even', '7 is odd', '8 is even', '3 is odd']
>>> ['{} is {}'.format(i, 'odd' if i%2 else 'even') for i in a]
['4 is even', '6 is even', '32 is even', '7 is odd', '8 is even', '3 is odd']
>>> 
>>> [[j for j in range(i)] for i in a]
[[0, 1, 2, 3], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2]]
>>> [[j*i for j in range(i)] for i in range(a)]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    [[j*i for j in range(i)] for i in range(a)]
TypeError: 'list' object cannot be interpreted as an integer
>>> [[j*i for j in range(i)] for i in a]
[[0, 4, 8, 12], [0, 6, 12, 18, 24, 30], [0, 32, 64, 96, 128, 160, 192, 224, 256, 288, 320, 352, 384, 416, 448, 480, 512, 544, 576, 608, 640, 672, 704, 736, 768, 800, 832, 864, 896, 928, 960, 992], [0, 7, 14, 21, 28, 35, 42], [0, 8, 16, 24, 32, 40, 48, 56], [0, 3, 6]]
>>> 
>>> [i if i<5 else (i*2 if i<10 else i//2)for i in a]
[4, 12, 16, 14, 16, 3]
>>> a
[4, 6, 32, 7, 8, 3]
>>> 
>>> 
>>> 
>>> c = {i:i**2 for i in a}
>>> c
{4: 16, 6: 36, 32: 1024, 7: 49, 8: 64, 3: 9}
>>> c
{4: 16, 6: 36, 32: 1024, 7: 49, 8: 64, 3: 9}
>>> for i in c:
	print(i)

	
4
6
32
7
8
3
>>> c1 = {'name':[4,5,6],'some':[4,8,3]}
>>> for i in c1:
	print(i)

	
name
some
>>> s = 'mnbadsbnamnbanmbamnbanmbasabns'
>>> {i:c1[i]*2 for i in c1}
{'name': [4, 5, 6, 4, 5, 6], 'some': [4, 8, 3, 4, 8, 3]}
>>> {'ab':i*2 for i in c1.values()}
{'ab': [4, 8, 3, 4, 8, 3]}
>>> 
>>> 
>>> s = 'mnbadsbnamnbanmbamnbanmbasabns'
>>> s.count('m')
5
>>> s.count('n')
7
>>> list(set(list(s)))
['s', 'n', 'b', 'm', 'a', 'd']
>>> for i in list(set(list(s))):
	print(i, s.count(i))

	
s 3
n 7
b 7
m 5
a 7
d 1
>>> list(s)
['m', 'n', 'b', 'a', 'd', 's', 'b', 'n', 'a', 'm', 'n', 'b', 'a', 'n', 'm', 'b', 'a', 'm', 'n', 'b', 'a', 'n', 'm', 'b', 'a', 's', 'a', 'b', 'n', 's']
>>> {i:s.count(i) for i in s}
{'m': 5, 'n': 7, 'b': 7, 'a': 7, 'd': 1, 's': 3}
>>> 
>>> 
>>> a = ['name','age']
>>> b = [['rohan','deepak','sakshi'], [23,21,22]]
>>> d = {a[i]:b[i] for i in range(2)}
>>> d
{'name': ['rohan', 'deepak', 'sakshi'], 'age': [23, 21, 22]}
>>> 
>>> e
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    e
NameError: name 'e' is not defined
>>> d
{'name': ['rohan', 'deepak', 'sakshi'], 'age': [23, 21, 22]}
>>> c
{4: 16, 6: 36, 32: 1024, 7: 49, 8: 64, 3: 9}
>>> b
[['rohan', 'deepak', 'sakshi'], [23, 21, 22]]
>>> b1
[8, 12, 64, 14, 16, 6]
>>> 
>>> 
>>> b1
[8, 12, 64, 14, 16, 6]
>>> for i in b1:
	print(i)

	
8
12
64
14
16
6
>>> for i in enumerate(b1):
	print(i)

	
(0, 8)
(1, 12)
(2, 64)
(3, 14)
(4, 16)
(5, 6)
>>> for i,v in enumerate(b1):
	print(i, v)

	
0 8
1 12
2 64
3 14
4 16
5 6
>>> for i,v in enumerate(b1):
	print(i)
	print(v)

	
0
8
1
12
2
64
3
14
4
16
5
6
>>> d = {v:b[i] for i,v in enumerate(a)}
>>> d
{'name': ['rohan', 'deepak', 'sakshi'], 'age': [23, 21, 22]}
>>> 
>>> a
['name', 'age']
>>> b
[['rohan', 'deepak', 'sakshi'], [23, 21, 22]]
>>> dict(zip(a,b))
{'name': ['rohan', 'deepak', 'sakshi'], 'age': [23, 21, 22]}
>>> list(zip(a,b))
[('name', ['rohan', 'deepak', 'sakshi']), ('age', [23, 21, 22])]
>>> 
>>> 
>>> 
>>> 
>>> for i in range(1,15):
	print('*'.center(2)*i)

	
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * * 
* * * * * * * * 
* * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * * 
* * * * * * * * * * * * 
* * * * * * * * * * * * * 
* * * * * * * * * * * * * * 
>>> for i in range(1,15):
	print('{}'.format(i).center(2)*i)

	
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
6 6 6 6 6 6 
7 7 7 7 7 7 7 
8 8 8 8 8 8 8 8 
9 9 9 9 9 9 9 9 9 
10101010101010101010
1111111111111111111111
121212121212121212121212
13131313131313131313131313
1414141414141414141414141414
>>> 
>>> for i in range(1,6):
	print(' '*(5-i)+('*'*i))

	
    *
   **
  ***
 ****
*****
>>> for i in range(5,0,-1):
	print(' '*(5-i)+('*'*i))

	
*****
 ****
  ***
   **
    *
>>> for i in range(1,7):
	for j in range(1,i):
		print(j,end='')
	print('')

	

1
12
123
1234
12345
>>> for i in range(1,7):
	for j in range(1,i+1):
		print(j,end='')
	print('')

	
1
12
123
1234
12345
123456
>>> for i in range(5,0,-1):
	print(' '*(5-i)+(i))

	
Traceback (most recent call last):
  File "<pyshell#112>", line 2, in <module>
    print(' '*(5-i)+(i))
TypeError: can only concatenate str (not "int") to str
>>> for i in range(5,0,-1):
	print(' '*(5-i)+str(i))

	
5
 4
  3
   2
    1
>>> for i in range(5,0,-1):
	print(i)

	
5
4
3
2
1
>>> for i in range(5,0,-1):
	print(' '*(5-i)+str(i)*(5-i))

	

 4
  33
   222
    1111
>>> 