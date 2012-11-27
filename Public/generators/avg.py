#!/usr/bin/env python
from __future__ import division

def pairwise( iterable, n=2 ):
	from itertools import tee, izip, islice
	return izip(*(islice(it,pos,None) for pos,it in enumerate(tee(iterable, n))))

if __name__ == '__main__':
	from sys import stdin
	from itertools import count,takewhile,imap
	input = imap(int,imap(str.rstrip,takewhile(bool,(stdin.readline() for _ in count()))))

	for x in pairwise(input,3):
		print sum(x)/len(x)


