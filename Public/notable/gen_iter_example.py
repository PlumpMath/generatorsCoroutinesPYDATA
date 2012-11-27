class Foo(object):
	def __init__(self):
		print 'Foo.__init__'
		self.x = 0
	def __iter__(self):
		print 'Foo.__iter__'
		return self
	def __next__(self):
		if self.x == 5: raise StopIteration()
		print 'Foo.__next__'
		self.x += 1
		return self.x
	next = __next__
	
print 'before for loop'
for x in Foo():
	print 'iteration'
	print 'x = ', x
print 'after for loop'
