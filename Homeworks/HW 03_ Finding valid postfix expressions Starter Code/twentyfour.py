from fractions import Fraction
from itertools import permutations as perms

class Postfix_Expression:

	def __init__(self, exp):
		self.ops = {'+': Fraction.__add__, '-': Fraction.__sub__, '*': Fraction.__mul__,
            '/': Fraction.__truediv__, '%': Fraction.__mod__, 'c': concatenate}
		self.cards = {str(i): i for i in range(2,10)}
		self.cards.update({'A': 1, '0': 10, 'J': 11, 'Q': 12, 'K': 13})
		self.exp = exp
	def evaluate(self, seq):
		"""
		If the element is an operation (i.e. is either ‘+’, ‘-’, ‘*’, ‘/’, ‘%’ or ‘c’) 
		the next two elements will always be card values
		"""
		stack = []
		for i in seq:
			if i == ' ': continue
			if i in self.ops and stack:
				try:
					val2 = stack.pop()
					val1 = stack.pop()
					stack.append(self.ops[i](val1,val2))
				except:
					return False
				#if self.ops is Fraction.__truediv__ and val2 == 0: return None
			else:
				stack.append(self.cards[i])
		return stack[-1]

	def isvalid(self, seq):
		return not (self.evaluate(seq) is False or self.evaluate(seq) is None)

def concatenate(a, b):
	try:
		if a < 0 and b < 0:
			return int(str(-a) + str(-b))
		if a < 0 or b < 0:
			return -int(str(abs(int(a))) + str(abs(int(b))))
		else:
			return int(str(a)+str(b))
	except:
		return int(str(int(a)) + str(int(b)))


def isint(n):
	"""
	Checks if a string can be converted into an int
	"""
	try:
		int(n)
		return True
	except ValueError:
		return False

def isfloat(n):
	"""
	Checks if a string can be converted into a float
	Warning: if a string can be converted into an int it'll turn it into a float. '1' would return 1.0
	"""
	try:
		float(n)
		return True
	except ValueError:
		return False

x = Postfix_Expression('AAJ')