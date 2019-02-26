from fractions import Fraction
from itertools import product, permutations as perms
from twentyfour import *

def find_postfix(pexp, s1):
    """
	I cleaned up all my code and combined a lot of the logic to make run much faster. 
    """
    results = set()
    s1 = ''.join(s1)
    #pcp = list(perms(s1))

    possible_forms = ["{} {} X {} {} X X", "{} {} {} {} X X X", "{} {} {} X {} X X", "{} {} X {} X {} X", "{} {} {} X X {} X"]
    #possible_forms = [s.format(s1[0],s1[1],s1[2],s1[3]) for s in possible_forms for p in pcp]
    #possible_forms = [s.format(p[0],p[1],p[2],p[3]) for s in possible_forms for p in pcp]

    for form in possible_forms:
	    for i,j,k in product(pexp.ops, repeat = 3):
	    	exp = form.format(s1[0],s1[1],s1[2],s1[3]).replace('X', i, 1).replace('X', j, 1).replace('X', k, 1)
	    	if 'c' in exp: continue	
    		if pexp.isvalid(exp) and pexp.evaluate(exp) == 24:
    			results.add(exp)
    return results
	    	

"""pexp = Postfix_Expression("8833")
results_set = set()
s1 = [0, 1, 2, 3]
for L in list(perms([0, 1, 2, 3], 4)):
    for i in range(4):
        s1[i] = pexp.exp[L[i]]
    results_set = results_set | find_postfix(pexp, s1)

for item in results_set:
    print(item)
print(len(results_set), ' solutions.')"""



"""pexp = Postfix_Expression("AAJA")
result = {"A A + J A + *"}
print(find_postfix(pexp, "AAJA"), result)
"""
"""pexp = Postfix_Expression("AAAJ")
result = {'J A + A A + *', 'A A + A J + *', 'A J + A A + *', 'A A + J A + *'} 
print(find_postfix(pexp, "AAJA"), result)"""

"""
pexp = Postfix_Expression("AKKJ")
result = {"A K % K J + *", "A K % K * J +"}
print(find_postfix(pexp, "AKKJ"), result)"""
