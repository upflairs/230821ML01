##v = input()
##x,y = v.split('#')
##x = [int(i) for i in x.split()]
##y = [int(i) for i in y.split()]
##print(x,y)

v = input().split(',')
v.sort()
print(','.join(v))
