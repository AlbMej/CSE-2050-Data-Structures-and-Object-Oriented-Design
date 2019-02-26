from fractions import Fraction
from itertools import permutations as perms

class Postfix_Expression:

	def __init__(self, exp):
		self.ops = {'+': Fraction.__add__, '-': Fraction.__sub__, '*': Fraction.__mul__,
            '/': Fraction.__truediv__, '%': Fraction.__mod__, 'c': concatenate}
		self.cards = {str(i): i for i in range(2,10)}
		self.cards.update({'A': 1, '0': 10, 'J': 11, 'Q': 12, 'K': 13})

	def evaluate(self, seq):
		"""
		If the element is an operation (i.e. is either ‘+’, ‘-’, ‘*’, ‘/’, ‘%’ or ‘c’) 
		the next two elements will always be card values
		"""
		stack = []
		for i in seq:
			if i in self.ops and stack:
				try:
					val2 = stack.pop()
					val1 = stack.pop()
				except IndexError:
					return False
				if self.ops is Fraction.__truediv__ and val2 == 0: return None
				stack.append(self.ops[i](val1,val2))
			else:
				stack.append(self.cards[i])
		return stack[-1]

	def isvalid(self, seq):
		return not (self.evaluate(seq) is False or self.evaluate(seq) is None)

def concatenate(a, b):
	pass
