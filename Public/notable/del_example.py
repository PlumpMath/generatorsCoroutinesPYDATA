class Foo(object):
	def __init__(self):
		print 'Foo.__init__'
	def __del__(self):
		print 'Foo.__del__'

x = Foo()
y = x
del x
print 'end of my programme'
