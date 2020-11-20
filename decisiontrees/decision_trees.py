# -*- coding: utf-8 -*-

"""Python class to represents the Decision Trees"""

class DecisionTree:
	"""Binary tree implementation with true and false branch. """
	def __init__(self, col=-1, value=None, trueBranch=None, falseBranch=None, results=None):
		self.col = col
		self.value = value
		self.trueBranch = trueBranch
		self.falseBranch = falseBranch
		self.results = results # None for nodes, not None for leaves