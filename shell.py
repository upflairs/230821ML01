Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # LIST
>>> a = [4,6,7,'hello',[41,63],3.4]
>>> type(a)
<class 'list'>
>>> len(a)
6
>>> print(a)
[4, 6, 7, 'hello', [41, 63], 3.4]
>>> 
>>> ## Additional Func
>>> a + [5,6,7]
[4, 6, 7, 'hello', [41, 63], 3.4, 5, 6, 7]
>>> a*3
[4, 6, 7, 'hello', [41, 63], 3.4, 4, 6, 7, 'hello', [41, 63], 3.4, 4, 6, 7, 'hello', [41, 63], 3.4]
>>> 
>>> ## Item Access
>>> a[0]
4
>>> a[-1]
3.4
>>> a[3]
'hello'
>>> a[3][0]
'h'
>>> a[3][::-1]
'olleh'
>>> a[-2]
[41, 63]
>>> a[-2][-1]
63
>>> a[:3]
[4, 6, 7]
>>> ## Item Insertion
>>> a += [10]
>>> a
[4, 6, 7, 'hello', [41, 63], 3.4, 10]
>>> a += [100,'go',[43,234]]
>>> a
[4, 6, 7, 'hello', [41, 63], 3.4, 10, 100, 'go', [43, 234]]
>>> a += ['nice']
>>> a
[4, 6, 7, 'hello', [41, 63], 3.4, 10, 100, 'go', [43, 234], 'nice']
>>> a += 'wow'
>>> a
[4, 6, 7, 'hello', [41, 63], 3.4, 10, 100, 'go', [43, 234], 'nice', 'w', 'o', 'w']
>>> 
>>> ## Item Assignment
>>> a[0]
4
>>> a[0] = 'kuch or'
>>> a
['kuch or', 6, 7, 'hello', [41, 63], 3.4, 10, 100, 'go', [43, 234], 'nice', 'w', 'o', 'w']
>>> 
>>> ## Item Deletion
>>> del a[-3:]
>>> a
['kuch or', 6, 7, 'hello', [41, 63], 3.4, 10, 100, 'go', [43, 234], 'nice']
>>> 
>>> ## List built-in functions
>>> # append, insert, count, index, sort, pop, remove
>>> # clear, copy
>>> a.append(55)
>>> a
['kuch or', 6, 7, 'hello', [41, 63], 3.4, 10, 100, 'go', [43, 234], 'nice', 55]
>>> a.insert(5,'bye')
>>> a
['kuch or', 6, 7, 'hello', [41, 63], 'bye', 3.4, 10, 100, 'go', [43, 234], 'nice', 55]
>>> help(a.insert)
Help on built-in function insert:

insert(index, object, /) method of builtins.list instance
    Insert object before index.

>>> a.count(4)
0
>>> a.index(100)
8
>>> a.index('python')
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a.index('python')
ValueError: 'python' is not in list
>>> a.pop(7)
10
>>> a
['kuch or', 6, 7, 'hello', [41, 63], 'bye', 3.4, 100, 'go', [43, 234], 'nice', 55]
>>> a.remove('kuch or')
>>> a
[6, 7, 'hello', [41, 63], 'bye', 3.4, 100, 'go', [43, 234], 'nice', 55]
>>> a.sort()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> b = [4,73,7,34,67,657,365,8]
>>> b.sort()
>>> b
[4, 7, 8, 34, 67, 73, 365, 657]
>>> b.sort(reverse=True)
>>> b
[657, 365, 73, 67, 34, 8, 7, 4]
>>> b.clear()
>>> b
[]
>>> b=[]
>>> 
>>> a
[6, 7, 'hello', [41, 63], 'bye', 3.4, 100, 'go', [43, 234], 'nice', 55]
>>> c = a
>>> c
[6, 7, 'hello', [41, 63], 'bye', 3.4, 100, 'go', [43, 234], 'nice', 55]
>>> d = a.copy()
>>> d
[6, 7, 'hello', [41, 63], 'bye', 3.4, 100, 'go', [43, 234], 'nice', 55]
>>> 
>>> c[0] = 66
>>> d[0] = 106
>>> c
[66, 7, 'hello', [41, 63], 'bye', 3.4, 100, 'go', [43, 234], 'nice', 55]
>>> d
[106, 7, 'hello', [41, 63], 'bye', 3.4, 100, 'go', [43, 234], 'nice', 55]
>>> a
[66, 7, 'hello', [41, 63], 'bye', 3.4, 100, 'go', [43, 234], 'nice', 55]
>>> a[1] = 707
>>> a
[66, 707, 'hello', [41, 63], 'bye', 3.4, 100, 'go', [43, 234], 'nice', 55]
>>> c
[66, 707, 'hello', [41, 63], 'bye', 3.4, 100, 'go', [43, 234], 'nice', 55]
>>> 

>>> ## additional func
>>> 707 in a
True
>>> 
>>> 
>>> ###############################################################
>>> 
>>> ## Tuple
>>> t = (5,7,8,'go',3.4, (4,8,6), [3,45,'ki'])
>>> type(t)
<class 'tuple'>
>>> len(t)
7
>>> t + t
(5, 7, 8, 'go', 3.4, (4, 8, 6), [3, 45, 'ki'], 5, 7, 8, 'go', 3.4, (4, 8, 6), [3, 45, 'ki'])
>>> t*2
(5, 7, 8, 'go', 3.4, (4, 8, 6), [3, 45, 'ki'], 5, 7, 8, 'go', 3.4, (4, 8, 6), [3, 45, 'ki'])
>>> t*3
(5, 7, 8, 'go', 3.4, (4, 8, 6), [3, 45, 'ki'], 5, 7, 8, 'go', 3.4, (4, 8, 6), [3, 45, 'ki'], 5, 7, 8, 'go', 3.4, (4, 8, 6), [3, 45, 'ki'])
>>> 
>>> 
>>> t[0]
5
>>> t[-1]
[3, 45, 'ki']
>>> t[-1][2]
'ki'
>>> t[-1][2][0]
'k'
>>> # item insertion
>>> t += (45,67)
>>> t
(5, 7, 8, 'go', 3.4, (4, 8, 6), [3, 45, 'ki'], 45, 67)
>>> t += 'wow'
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    t += 'wow'
TypeError: can only concatenate tuple (not "str") to tuple
>>> t += ('hi')
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    t += ('hi')
TypeError: can only concatenate tuple (not "str") to tuple
>>> t += (100)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    t += (100)
TypeError: can only concatenate tuple (not "int") to tuple
>>> t += (100,)
>>> t
(5, 7, 8, 'go', 3.4, (4, 8, 6), [3, 45, 'ki'], 45, 67, 100)
>>> t += ('hi',)
>>> 
>>> t += 120,
>>> t
(5, 7, 8, 'go', 3.4, (4, 8, 6), [3, 45, 'ki'], 45, 67, 100, 'hi', 120)
>>> t += 140,'nice',5.6
>>> t
(5, 7, 8, 'go', 3.4, (4, 8, 6), [3, 45, 'ki'], 45, 67, 100, 'hi', 120, 140, 'nice', 5.6)
>>> 
>>> 
>>> ## item assignment
>>> t[0] = 55
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    t[0] = 55
TypeError: 'tuple' object does not support item assignment
>>> 
>>> ## item deletion
>>> del t[0]
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    del t[0]
TypeError: 'tuple' object doesn't support item deletion
>>> 
>>> 
>>> ## Tuple Built-in functions
>>> t.count(7)
1
>>> t.index(67)
8
>>> ###########################################################################
>>> 
>>> ## Dictionary
>>> 
>>> ai = {'name':['anushka','amit','arnav'], 'sem':[3,3,3]}
>>> ml = {'name':['sanjeev','sandhya','saroj'], 'sem':[3,5,5], 'branch':['cs','ec','ec']}
>>> 
>>> type(ai)
<class 'dict'>
>>> type(ml)
<class 'dict'>
>>> 
>>> len(ai)
2
>>> len(ml)
3
>>> print(ai)
{'name': ['anushka', 'amit', 'arnav'], 'sem': [3, 3, 3]}
>>> print(ml)
{'name': ['sanjeev', 'sandhya', 'saroj'], 'sem': [3, 5, 5], 'branch': ['cs', 'ec', 'ec']}
>>> 
>>> # Access
>>> ai['name']
['anushka', 'amit', 'arnav']
>>> ai[0]
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    ai[0]
KeyError: 0
>>> ai['name'][0]
'anushka'
>>> ai['name'][0][::-1]
'akhsuna'
>>> 
>>> ai['branch'] = ['ec','it','cs']
>>> ai
{'name': ['anushka', 'amit', 'arnav'], 'sem': [3, 3, 3], 'branch': ['ec', 'it', 'cs']}
>>> # upar wala tha item insertion
>>> 
>>> # now  we'll do item assignment
>>> ai['sem'] = [5,5,3]
>>> ai
{'name': ['anushka', 'amit', 'arnav'], 'sem': [5, 5, 3], 'branch': ['ec', 'it', 'cs']}
>>> ai['name'][1] = 'sumit'
>>> ai
{'name': ['anushka', 'sumit', 'arnav'], 'sem': [5, 5, 3], 'branch': ['ec', 'it', 'cs']}
>>> 
>>> # deletion
>>> del ai['branch']
>>> ai
{'name': ['anushka', 'sumit', 'arnav'], 'sem': [5, 5, 3]}
>>> 
>>> 
>>> ## Built-in functions
>>> # copy, get, keys, values, pop
>>> ai['name']
['anushka', 'sumit', 'arnav']
>>> ai['branch']
Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    ai['branch']
KeyError: 'branch'
>>> ai.get('branch')
>>> ai.get('name')
['anushka', 'sumit', 'arnav']
>>> 
>>> ai.keys()
dict_keys(['name', 'sem'])
>>> ai.keys()[0]
Traceback (most recent call last):
  File "<pyshell#167>", line 1, in <module>
    ai.keys()[0]
TypeError: 'dict_keys' object is not subscriptable
>>> list(ai.keys())[0]
'name'
>>> list(ai.keys())[1]
'sem'
>>> 
>>> ai.values()
dict_values([['anushka', 'sumit', 'arnav'], [5, 5, 3]])
>>> 
>>> 
>>> ml
{'name': ['sanjeev', 'sandhya', 'saroj'], 'sem': [3, 5, 5], 'branch': ['cs', 'ec', 'ec']}
>>> 
>>> ml['stream'] = ml['branch']
>>> del ml['branch']
>>> 
>>> ml
{'name': ['sanjeev', 'sandhya', 'saroj'], 'sem': [3, 5, 5], 'stream': ['cs', 'ec', 'ec']}
>>> 
>>> 
>>> ml['semester'] = ml.pop('sem')
>>> ml
{'name': ['sanjeev', 'sandhya', 'saroj'], 'stream': ['cs', 'ec', 'ec'], 'semester': [3, 5, 5]}
>>> 
>>> 
>>> ####################################################################
>>> ## Set - A collection of unique elements
>>> s = {4,5,76,3,76,3,6,3,'fdhj',6,3,43,4,6,2657,4,5,7,4,67,3,68,4}
>>> type(s)
<class 'set'>
>>> len(s)
11
>>> print(s)
{2657, 3, 4, 5, 6, 7, 67, 68, 43, 76, 'fdhj'}
>>> 
>>> s[0]
Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    s[0]
TypeError: 'set' object is not subscriptable
>>> 
>>> 
>>> # Built-in Functions
>>> ## add, difference, union, intersection,
>>> ## pop, remove
>>> 
>>> ####################################################################
>>> ## Boolean - True, False
>>> # bool()
>>> 
>>> bool(30)
True
>>> bool(-30)
True
>>> bool(1)
True
>>> bool(0)
False
>>> bool([3,4,5])
True
>>> bool((4,5,))
True
>>> bool([])
False
>>> bool(())
False
>>> bool(None)
False
>>> # Anything which is zero or empty is False in boolean
>>> # anything non-zero or non-empty is True in boolean
>>> 