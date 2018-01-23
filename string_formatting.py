# !/usr/bin/python
def foo():
    return 'Xxx'
print '{0} , {1} , {2} , {3}'.format('values', 1000, True, None)
print '{} , {} , {} , {}'.format('values', 1000, True, None)
c = (1, 2, 3)
#print '{0[2]} , {0[1]} , {0[0]}'.format(c)(d){'k1': 'some value', 'k2': 101, 'k3': foo}
print 'k1 is `{0[0]}` ; k2 is `{0[1]}` ; k3 is `{0[2]}`'.format(d.values())
print 'k1 is `{}` ; k2 is `{}` ; k3 is `{}`'.format(*d.values())
print 'k1 is `{k1}` ; k2 is `{k2}` ; k3 is `{k3}`'.format(**d)
print '{:+f}; {:+f}'.format(3.14, -3.14) # Always print the sign
print "int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)
print "int: {0:#d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)
print '{:,}'.format(1234567890)