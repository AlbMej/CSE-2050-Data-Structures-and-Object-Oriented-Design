class Polynomial:
    def __init__(self, terms):
        self.terms = []
        for term in terms:
            if isinstance(term, Monomial):
                self.terms.append(term)
            else:
                self.terms.append(Monomial(*term))

    def evaluate(self, x):
    	result = 0
    	for term in self.terms:
        	result += (term.evaluate(x))
    	return result

    def __add__(self, other):
    	terms = self.terms + other.terms
    	result = Polynomial(terms)
    	result.reduce()
    	return result

    def __mul__(self, other):
        result = Polynomial([])
        for i in self.terms:
        	for j in other.terms:
        		result.terms.append(Monomial(i.coeff * j.coeff, i.exp + j.exp))
        return result

    def	__call__(self, x):
    	return self.evaluate(x)

    def	__neg__(self):
    	return	self * Monomial(-1,	0)

    def	__sub__(self, other):
    	return self + (-other)

    def prime(self):
        #result = Polynomial([i.prime() for i in self.terms])
        #return result
        self = Polynomial([i.prime() for i in self.terms])
        return self

    def root(self, guess = 0, iterations = 50):
        for i in range(iterations):
            if self.prime().evaluate(guess) == 0:
                guess += 1
            try:
                guess = guess - (self.evaluate(guess)/self.prime().evaluate(guess))
            except ZeroDivisionError:
                return guess 
        return guess

    # Combine like terms and eliminate zero monomials.
    def reduce(self):
        commonterms = {}
        for term in self.terms:
            if term.exp in commonterms:
                commonterms[term.exp] += term.coeff
            else:
                commonterms[term.exp] = term.coeff
        # Rebuild the list of terms
        self.terms = []
        for e,c in commonterms.items():
            if c != 0:
                self.terms.append(Monomial(c,e))
        self.terms.sort()
        return self

    def __eq__(self, other):
        self.reduce()
        other.reduce()
        return self.terms == other.terms

class Monomial(Polynomial):
    def __init__(self, coeff, exp):
        self.coeff = coeff
        self.exp = exp
        Polynomial.__init__(self, [self])

    def evaluate(self, x):
        try:
            return self.coeff * (x ** self.exp)
        except ZeroDivisionError:
            return 0

    def __eq__(self, other):
        # Make sure other is a Monomial.
        if isinstance(other, Monomial):
            if self.coeff == 0 and other.coeff == 0:
                return True
            else:
                return self.exp == other.exp and self.coeff == other.coeff
        else:
            return NotImplemented

    def __lt__(self, other):
        return (self.exp, self.coeff) < (other.exp, other.coeff)

    def __mul__(self, other):
        # Make sure other is a Monomial.
        if isinstance(other, Monomial):
            return Monomial(self.coeff * other.coeff, self.exp + other.exp)
        else:
            return NotImplemented

    def __neg__(self):
        return Monomial(-1,0) * self

    def prime(self):
    	#If constant, exponent becomes -1. Keep that in mind just in case I have to change it. 
    	return Monomial(self.coeff*self.exp, self.exp - 1)

"""root = 10
p = Polynomial([(1,1), (-root,0)])
for i in range(2):
    p = p * p
result = p.root()
print(result - root)
print(abs(result - root) < .02)

print("-----------------------------------")
# Should do better with a good guess.
result = p.root(11)
print('result: ',result, "root: ", root)
print('result - root: ', result - root)
print(abs(result - root) < .01)
print("-----------------------------------")
# Should do even better with more iterations.
result = p.root(11, 1000)
print('result: ',result, "root: ", root)
print('result - root: ', result - root)
print(abs(result - root) < .002)

print("-----------------------------------")
roots = [2, -4, 5, 8, -1]        
p=Polynomial([(1,0)])
for poly in [Polynomial([(1, 1), (-i, 0)]) for i in roots]:
    p*=poly
#print([(i.coeff,i.exp) for i in p.terms])
for r in roots:
    #print(r)
    print((abs(p.root(r-1) - r) < .001))
"""

