Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = [4,5,10,11,9,3,8]
>>> for i in range(7):
	print(i)

	
0
1
2
3
4
5
6
>>> a[0]
4
>>> for i in range(7):
	print(a[i])

	
4
5
10
11
9
3
8
>>> for i in range(7):
	print(a[i]*2)

	
8
10
20
22
18
6
16
>>> for i in range(len(a)):
	print(a[i]*2)

	
8
10
20
22
18
6
16
>>> b = [3,6,7,89,0,1,3]
>>> for i in range(len(a)):
	print(a[i]*2, b[i]*2)

	
8 6
10 12
20 14
22 178
18 0
6 2
16 6
>>> a
[4, 5, 10, 11, 9, 3, 8]
>>> for i in range(len(a)):
	print(a[i]*2)
	print(b[i]*2)

	
8
6
10
12
20
14
22
178
18
0
6
2
16
6
>>> for i in range(len(a)):
	print(a[i]*2)
for i in range(len(b)):
	
SyntaxError: invalid syntax
>>> for i in range(len(a)):
	print(a[i]*2)

	
8
10
20
22
18
6
16
>>> for i in range(len(b)):
	print(b[i]*2)

	
6
12
14
178
0
2
6
>>> a[11]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a[11]
IndexError: list index out of range
>>> for i in range(15):
	print(b[i]*2)

	
6
12
14
178
0
2
6
Traceback (most recent call last):
  File "<pyshell#28>", line 2, in <module>
    print(b[i]*2)
IndexError: list index out of range
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a
[4, 5, 10, 11, 9, 3, 8]
>>> for i in a:
	print(i*2)

	
8
10
20
22
18
6
16
>>> 
= RESTART: C:/Users/hp/Desktop/UFT/23082021MLAI01/day6/script.py
a is: [4, 5, 7, 3, 6, 3, 6, 3, 6, 12, 34, 83, 3, 7, 91, 4]
b is: [8, 10, 14, 6, 12, 6, 12, 6, 12, 24, 68, 166, 6, 14, 182, 8]
>>> 
= RESTART: C:/Users/hp/Desktop/UFT/23082021MLAI01/day6/script.py
a is: [4, 5, 7, 3, 6, 3, 6, 3, 6, 12, 34, 83, 3, 7, 91, 4]
b is: [8, 10, 14, 6, 12, 6, 12, 6, 12, 24, 68, 166, 6, 14, 182, 8]
[5, 7, 3, 3, 3, 83, 3, 7, 91]
>>> 
= RESTART: C:/Users/hp/Desktop/UFT/23082021MLAI01/day6/script.py
a is: [4, 5, 7, 3, 6, 3, 6, 3, 6, 12, 34, 83, 3, 7, 91, 4]
b is: [8, 10, 14, 6, 12, 6, 12, 6, 12, 24, 68, 166, 6, 14, 182, 8]
[5, 7, 3, 3, 3, 83, 3, 7, 91]
>>> 