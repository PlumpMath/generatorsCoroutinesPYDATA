def latch(value):
	while True:
		v = (yield value)
		if v is not None:
			value = v

x = latch('first')
print '1', next(x)
print '2', next(x)
print '3', x.send('second') 
print '4', next(x)
print '5', next(x)
print '6', next(x)
