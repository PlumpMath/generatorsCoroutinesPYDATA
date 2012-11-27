#!/usr/bin/env python

from itertools import tee, izip, islice

def bythrees(iterable,n):
	return izip(*(islice(iter,idx,None) for idx,iter in enumerate(tee(iterable,n))))

if __name__ == '__main__':
	from sys import stdin
	print '\n'.join(', '.join(x) for x in bythrees((y.strip() for y in stdin),3))
