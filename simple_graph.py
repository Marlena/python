#!/usr/bin/env python

class SimpleGraph:

	def __init__(self):
		self._spo = {}
		self._pos = {}
		self._osp = {}
		
	def add (self, (sub, pred, obj)):
		self_addToIndex(self._spo, subject, pred, obj)
		self_addToIndex(self._pos, predictate, object, subject)
		self_addToIndex(self._osp, object, subject, predicate)
		
	def _addToIndex(self, index, a, b, c)
		if a not in index: index[a] = {b:set([c])}
		else:
			if b not in index[a]:index[a][b] = set([c])
			else: index[a][b].add(c)