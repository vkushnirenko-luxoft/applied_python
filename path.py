# !/usr/bin/python
import os
path='/tmp/1'
def _tree(path):
    f=open('/tmp/tree.txt','w+')
    for root, dirs, files in os.walk(path):
        print (root)
        f.write(os.path.join(root,"\n"))
        for dir in dirs:
            print (dir)
            f.write(os.path.join(dir,"\n"))
            for name in files:
                print (name)
                f.write("%s\n" %name)
    f.close()

_tree(path)