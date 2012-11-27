from itertools import islice
class partialdict(dict):
	def __missing__(self, key):
		return self[frozenset(islice(iter(key),1,None))]
class gentype(object):
	dispatch = partialdict({frozenset(): lambda gen,arg: (gen(arg),'')})
	def __init__(self, gentype):
		self.gentype = gentype
	def __call__(self, gen):
		return typed(gen, gentype=self.gentype)
class typed(object):
	def __init__(self, gen, gentype):
		self.gen, self.gentype = gen, gentype
	def __call__(self, arg):
		arg_gentype = arg.gentype if isinstance(arg, wrapped) else ''
		dispatch = gentype.dispatch[frozenset([self.gentype, arg_gentype])]
		rv, rv_type = dispatch(self.gen, arg)
		if not isinstance(rv, wrapped) or rv.gentype != rv_type:
			rv = wrapped(rv, rv_type)
		return rv 
class wrapped(object):
	def __init__(self, gen, gentype):
		self.gen, self.gentype = gen, gentype
	def __iter__(self):
		return self
	def __next__(self):
		return next(self.gen)
	next = __next__
	def send(self, *args, **kwargs):
		return self.gen.send(*args, **kwargs)
	def throw(self, *args, **kwargs):
		return self.gen.throw(*args, **kwargs)
	def close(self, *args, **kwargs):
		return self.gen.close(*args, **kwargs)

passthrough = gentype('passthrough')
gentype.dispatch[frozenset([passthrough.gentype, passthrough.gentype])] = \
  lambda gen,arg: (arg, passthrough.gentype)
gentype.dispatch[frozenset([passthrough.gentype])] = \
  lambda gen,arg: (arg, passthrough.gentype)

@passthrough
def f(xs):
	print 'fff'
	for x in xs:
		yield x

@passthrough
def g(xs):
	print 'ggg'
	for x in xs:
		yield x

def h(xs):
	print 'hhh'
	for x in xs:
		yield x

result = f(g(h(x for x in xrange(10))))
print result
print list(result)
