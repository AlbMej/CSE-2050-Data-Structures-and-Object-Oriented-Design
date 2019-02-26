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
    	for i in range(len(self.terms)):
    		monomial = self.terms[i]
    		self.terms[i] = monomial.prime()
    	return self

    def root(self, guess = 0, iterations = 50):
    	for i in range(iterations):
    		guess = guess - (self.evaluate(guess)/self.prime().evaluate(guess))
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


#p = Polynomial([(3,7),(2,5),(1,2),(135,0)])
#print([(i.coeff,i.exp) for i in p.prime().terms])