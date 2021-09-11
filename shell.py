Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import keyword
>>> import math
>>> import numpy
>>> import os
>>> import calendar
>>> import datetime
>>> keyword.kwlist
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> keyword.softkwlist
[]
>>> math.sqrt(64)
8.0
>>> datetime.datetime.now()
datetime.datetime(2021, 9, 10, 20, 43, 48, 308098)
>>> print(datetime.datetime.now())
2021-09-10 20:43:59.189796
>>> print(calendar.calendar(2021))
                                  2021

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3       1  2  3  4  5  6  7       1  2  3  4  5  6  7
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       8  9 10 11 12 13 14
11 12 13 14 15 16 17      15 16 17 18 19 20 21      15 16 17 18 19 20 21
18 19 20 21 22 23 24      22 23 24 25 26 27 28      22 23 24 25 26 27 28
25 26 27 28 29 30 31                                29 30 31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
          1  2  3  4                      1  2          1  2  3  4  5  6
 5  6  7  8  9 10 11       3  4  5  6  7  8  9       7  8  9 10 11 12 13
12 13 14 15 16 17 18      10 11 12 13 14 15 16      14 15 16 17 18 19 20
19 20 21 22 23 24 25      17 18 19 20 21 22 23      21 22 23 24 25 26 27
26 27 28 29 30            24 25 26 27 28 29 30      28 29 30
                          31

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
          1  2  3  4                         1             1  2  3  4  5
 5  6  7  8  9 10 11       2  3  4  5  6  7  8       6  7  8  9 10 11 12
12 13 14 15 16 17 18       9 10 11 12 13 14 15      13 14 15 16 17 18 19
19 20 21 22 23 24 25      16 17 18 19 20 21 22      20 21 22 23 24 25 26
26 27 28 29 30 31         23 24 25 26 27 28 29      27 28 29 30
                          30 31

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3       1  2  3  4  5  6  7             1  2  3  4  5
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       6  7  8  9 10 11 12
11 12 13 14 15 16 17      15 16 17 18 19 20 21      13 14 15 16 17 18 19
18 19 20 21 22 23 24      22 23 24 25 26 27 28      20 21 22 23 24 25 26
25 26 27 28 29 30 31      29 30                     27 28 29 30 31

>>> os.startfile('d:/banner.mp4')
>>> import webbrowser
>>> webbrowser.open_new_tab('www.google.com/search?q=trending+bollywood+song')
True
>>> os.getcwd()
'C:\\Users\\hp\\AppData\\Local\\Programs\\Python\\Python39'
>>> 
>>> 
>>> ######################
>>> startfile('d:/banner.mp4')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    startfile('d:/banner.mp4')
NameError: name 'startfile' is not defined
>>> 
>>> 
>>> from os import startfile, getcwd
>>> 
>>> startfile('d:/banner.mp4')
>>> 
>>> from os import *
>>> 
>>> import matplotlib.pyplot
>>> i = matplotlib.pyplot.imread('d:/pic.jpg')
>>> matplotlib.pyplot.imshow(i)
<matplotlib.image.AxesImage object at 0x000001B15FBFF970>
>>> matplotlib.pyplot.show()
>>> 
>>> import matplotlib.pyplot as plt
>>> i2 = plt.imread('d:/pic.jpg')
>>> plt.imshow(i2); plt.show()
<matplotlib.image.AxesImage object at 0x000001B160772A60>
>>> 
>>> from os import startfile as sf, getcwd as gc
>>> sf('d:/banner.mp4')
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
======== RESTART: C:/Users/hp/Desktop/UFT/23082021ML01/day12/script.py =======
>>> 
======== RESTART: C:/Users/hp/Desktop/UFT/23082021ML01/day12/script.py =======
Traceback (most recent call last):
  File "C:/Users/hp/Desktop/UFT/23082021ML01/day12/script.py", line 4, in <module>
    app.geomtery('200x250')
  File "C:\Users\hp\AppData\Local\Programs\Python\Python39\lib\tkinter\__init__.py", line 2354, in __getattr__
    return getattr(self.tk, attr)
AttributeError: '_tkinter.tkapp' object has no attribute 'geomtery'
>>> 
======== RESTART: C:/Users/hp/Desktop/UFT/23082021ML01/day12/script.py =======
>>> 
======== RESTART: C:/Users/hp/Desktop/UFT/23082021ML01/day12/script.py =======

======== RESTART: C:/Users/hp/Desktop/UFT/23082021ML01/day12/script.py =======
>>> 
======== RESTART: C:/Users/hp/Desktop/UFT/23082021ML01/day12/script.py =======

======== RESTART: C:/Users/hp/Desktop/UFT/23082021ML01/day12/script.py =======
>>> 
======== RESTART: C:/Users/hp/Desktop/UFT/23082021ML01/day12/script.py =======
>>> 
======== RESTART: C:/Users/hp/Desktop/UFT/23082021ML01/day12/script.py =======

======== RESTART: C:/Users/hp/Desktop/UFT/23082021ML01/day12/script.py =======
>>> 
======== RESTART: C:/Users/hp/Desktop/UFT/23082021ML01/day12/script.py =======
>>> 
======== RESTART: C:/Users/hp/Desktop/UFT/23082021ML01/day12/script.py =======

======== RESTART: C:/Users/hp/Desktop/UFT/23082021ML01/day12/script.py =======
>>> 