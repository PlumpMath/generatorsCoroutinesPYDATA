class Blah(object):
	def __init__(self):
		print 'Blah.__init__'
	def __enter__(self):
		print 'Blah.__enter__'
	def __exit__( self, *args ):
		print 'Blah.__exit__', args

with Blah():
	print 'inside foo'
	raise Exception()
