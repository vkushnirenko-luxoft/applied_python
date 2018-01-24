# !/usr/bin/python

l1 = [(1,3),(5,2),(7,3),(2,4),(1,7)]

#===way1
#l1.sort(key = lambda x: x[0])

#===way2
def getKey(x):
    return x[0]

l1.sort(key=getKey)

print l1
