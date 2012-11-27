def gen():
	print 'at the top'
	yield 1
	print 'code between 1 and 2'
	yield 2
	print 'at the bottom'

for x in xrange(15):
	print

print 'creating the generator'
g = gen()
print 'created the generator'

print

print 'asking for the first value'
print next(g)
print 'asked for the first value'

print

print 'asking for the second value'
print next(g)
print 'asked for the second value'

