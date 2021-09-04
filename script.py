#############
##f = open('data.txt')
##r = f.read().split('\n')
##f.close()
##print(r)
##
##keys = r.pop(0).split(',')
##values = [i.split(',') for i in r]
##
##d = dict(zip(keys,zip(*values)))
##print(d)
##
###############
##
### **
##e = {'ekor':[2,34,6,2]}
##print({**d, **e})
#######################################


# User Defined Functions
#---------------------------
'''
def func_name(....):
    -------
    -------
    -------

global
local
nonlocal

'''

##def first():
##    print('hi')
##    print('hello')
##
##def second(x):
##    print(x*2)
##
##def third():
##    print('wow')
##    return 'hello'
##    print('nice')
##
##def fourth(x):
##    x = x+4
##    return x*2


##z = 10
##def new(y):
##    print(y)
##    print(z)
##
##print(z)
##new(34)
##print(z)

##z = 10
##def new():
##    z = 20
##    print(z)
##
##print(z)
##new()
##print(z)

##z = 10
##def new():
##    global z
##    z = 20
##    print(z)
##
##print(z)
##new()
##print(z)


##z = 10
##def new():   
##    global z
##    z = 20
##    y = 30    
##    print(y,z)
##    def xyz():        
##        def abcd():
##            nonlocal y            
##            p = 50
##            y = 200
##        abcd()
##        print(y)
##    xyz()    
##    print(y)
##        
##
##print(z)
##new()
##print(z)


def five(x,y,z):
    return (x+y)*z

def six(x,y,z):
    return x+y*z, x-z, y*z

def seven(x=0,y=0,z=1):
    return (x+y)*z


def eight(*x):
    # here the x treated as tuple    
    return x

def nine(**x):
    # here the x treated as dictionary
    return x


