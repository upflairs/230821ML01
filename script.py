a = [4,5,7,3,6,3,6,3,6,12,34,83,3,7,91,4,]
b = []
for i in a:
    b += [i*2]
print('a is:', a)
print('b is:', b)


c = []
for i in a:
    if i%2 == 1:
        c += [i]
print(c)
