Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = 'this is a python sting'
>>> s1 = "this is a python sting"
>>> type(s)
<class 'str'>
>>> type(s1)
<class 'str'>
>>> print(s)
this is a python sting
>>> print(s1)
this is a python sting
>>> s
'this is a python sting'
>>> s1
'this is a python sting'
>>> # Operations
>>> #-------------
>>> # 1. Item Accessing
>>> # 2. Item Insertion
>>> # 3. Item Assignment
>>> # 4. Item Deletion
>>> 
>>> # < Built-in Functions >
>>> # < Additional Functionalities >
>>> 
>>> len(s)
22
>>> s + s1
'this is a python stingthis is a python sting'
>>> 'hello' + ' go'
'hello go'
>>> 
>>> s * 2
'this is a python stingthis is a python sting'
>>> s * 3
'this is a python stingthis is a python stingthis is a python sting'
>>> 
>>> ##
>>> # Item Indexing, Items Slicing
>>> s[0]
't'
>>> s[21]
'g'
>>> s[5]
'i'
>>> s[-1]
'g'
>>> s[0]
't'
>>> s[len(s)-1]
'g'
>>> s[-2]
'n'
>>> s[0:4:1]
'this'
>>> s[10:16:1]
'python'
>>> s[5:5+6:1]
'is a p'
>>> s[-5:22:1]
'sting'
>>> s[-5:-1:1]
'stin'
>>> s[-5:50:1]
'sting'
>>> s[-12:-6:1]
'python'
>>> s[10:-6:1]
'python'
>>> s[10:-6:]
'python'
>>> s[10:-6]
'python'
>>> s[:4]
'this'
>>> s[:10]
'this is a '
>>> s[-5:]
'sting'
>>> s[0:4:-1]
''
>>> s[4:0:-1]
' sih'
>>> s[-1:-6:-1]
'gnits'
>>> s[-7:-13:-1]
'nohtyp'
>>> s[:-6:-1]
'gnits'
>>> s[3::-1]
'siht'
>>> s[::-1]
'gnits nohtyp a si siht'
>>> s[::]
'this is a python sting'
>>> s
'this is a python sting'
>>> s[:]
'this is a python sting'
>>> s[::2]
'ti sapto tn'
>>> s[5:15:3]
'iayo'
>>> 
>>> # item insertion
>>> s
'this is a python sting'
>>> s1
'this is a python sting'
>>> s1 + ' of mine'
'this is a python sting of mine'
>>> s1
'this is a python sting'
>>> s1[:10] + 'new ' + s1[10:]
'this is a new python sting'
>>> 
>>> s1 += ' of mine'
>>> s1
'this is a python sting of mine'
>>> 
>>> # item assignment
>>> s[0]
't'
>>> s[0] = 'P'
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    s[0] = 'P'
TypeError: 'str' object does not support item assignment
>>> 
>>> 
>>> # item deletion
>>> del s[2]
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    del s[2]
TypeError: 'str' object doesn't support item deletion
>>> 
>>> 
>>> # Built-in Functions
>>> ###
>>> # upper, lower, format, join, split, strip, count, index, find
>>> # islower, isupper, isalpha, isalnum, isnumeric
>>> # startswith, endswith, ljust, rjust, lstrip, rstrip
>>> s.upper()
'THIS IS A PYTHON STING'
>>> s.lower()
'this is a python sting'
>>> s.split()
['this', 'is', 'a', 'python', 'sting']
>>> len(s.split())
5
>>> e = 'peeyush@upflairs.com'
>>> e1 = 'peeyush.sanam@gmail.com'
>>> s.split('@')
['this is a python sting']
>>> e.split('@')
['peeyush', 'upflairs.com']
>>> e.split('@')[-1]
'upflairs.com'
>>> 
>>> 'wow'.join('amazing')
'awowmwowawowzwowiwownwowg'
>>> 
>>> '_'.join(s.split())
'this_is_a_python_sting'
>>> k = '   this is something '
>>> k
'   this is something '
>>> k.strip()
'this is something'
>>> k.lstrip()
'this is something '
>>> k.rstrip()
'   this is something'
>>> s.count('i')
3
>>> s.index('g')
21
>>> s.index('i')
2
>>> s
'this is a python sting'
>>> s.find('i')
2
>>> s.index('z')
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    s.index('z')
ValueError: substring not found
>>> s.find('hello')
-1
>>> s.islower()
True
>>> s.isupper()
False
>>> s.isnumeric()
False
>>> '345'.isnumeric()
True
>>> 'hi'.isalpha()
True
>>> 'hi bye'.isalpha()
False
>>> 'hi bye'.isalnum()
False
>>> 'hibye'.isalnum()
True
>>> 'hibye45654'.isalnum()
True
>>> s.startswith('a')
False
>>> s.endswith('k')
False
>>> s.endswith('g')
True
>>> s.endswith('ng')
True
>>> s.endswith('sting')
True
>>> print('hello hi',45)
hello hi 45
>>> print('hello hi',45); print('this is amazing',66)
hello hi 45
this is amazing 66
>>> 
>>> print('hello hi'.ljust(18),45); print('this is amazing'.ljust(18),66)
hello hi           45
this is amazing    66
>>> print('hello hi'.rjust(18),45); print('this is amazing'.rjust(18),66)
          hello hi 45
   this is amazing 66
>>> print('hello hi'.center(20)); print('this is amazing'.center(20))
      hello hi      
  this is amazing   
>>> 
>>> 
>>> a = 10
>>> b = 'hi'
>>> c = 34.6
>>> p = 'he said {} I will do {} calls in next {} minutes for next {} days'
>>> p.format(b,a,c,a)
'he said hi I will do 10 calls in next 34.6 minutes for next 10 days'
>>> p1 = 'he said {0} I will do {1} calls in next {2} minutes for next {1} days'
>>> p1.format(b,a,c)
'he said hi I will do 10 calls in next 34.6 minutes for next 10 days'
>>> 'hello hi'.ljust(18)
'hello hi          '
>>> 'hello hi'.ljust(40)
'hello hi                                '
>>> print('hello hi                                ',60)
hello hi                                 60
>>> print('hello hi'.ljust(18),45); print('this is amazing'.ljust(18),6600)
hello hi           45
this is amazing    6600
>>> 
>>> 
>>> s3 = 'this is a paragraph
SyntaxError: EOL while scanning string literal
>>> s3 = 'this is a paragraph'
>>> s3 = '''this is a paragraph
and this is another line
or ye ab teesri line bhi ho gayi
or dekho forth me bhi chala gya
and yes it can continue
as much as we want'''
>>> s4 = 'this is a paragraph\nan this is another line\nkjgfdjgdf kjkjdf jkhkjrt \n jkfdhgjhfd'
>>> s4
'this is a paragraph\nan this is another line\nkjgfdjgdf kjkjdf jkhkjrt \n jkfdhgjhfd'
>>> s3
'this is a paragraph\nand this is another line\nor ye ab teesri line bhi ho gayi\nor dekho forth me bhi chala gya\nand yes it can continue\nas much as we want'
>>> 
>>> print(s3)
this is a paragraph
and this is another line
or ye ab teesri line bhi ho gayi
or dekho forth me bhi chala gya
and yes it can continue
as much as we want
>>> print(s4)
this is a paragraph
an this is another line
kjgfdjgdf kjkjdf jkhkjrt 
 jkfdhgjhfd
>>> s5 = """this is a paragraph
and this is another line
or ye ab teesri line bhi ho gayi
or dekho forth me bhi chala gya
and yes it can continue
as much as we want"""
>>> print(s5)
this is a paragraph
and this is another line
or ye ab teesri line bhi ho gayi
or dekho forth me bhi chala gya
and yes it can continue
as much as we want
>>> 