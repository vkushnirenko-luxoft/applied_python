# !/usr/bin/python
import os
path='/tmp/1'
_listdir=[]
for root in os.walk(path):
    _listdir.append(root)
print (_listdir)

print ("")
for root in iter(_listdir):
    print root

print ("")
for root, dirs, files in os.walk(path):
    for name in files:
        print os.path.join(root, name)
