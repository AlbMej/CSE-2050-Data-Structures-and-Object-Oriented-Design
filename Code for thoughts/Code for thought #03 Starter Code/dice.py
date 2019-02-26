### Code for thought #3
### In this code thought problem, we will solve the following mathmatical
### problem.

### A fair, twenty-faced die has 19 of its faces numbered from 1 through 19
### and has one blank face. Another fair, twenty-faced die has 19 of its faces
### numbered from 1 through 8 and 10 through 20 and has one blank face. When
### the two dice are rolled, what is the probability that the sum of the two
### numbers facing up will be 24? Express your answer as a common fraction.

### This is from my daughter's mathcounts problems.
### It is a good idea that you solve it using your brain first and then using
### your computer :)
from fractions import Fraction
import random

def is24():
    ### Below we use two lists to describe the two dice
    die1 = [ i for i in range(20)]
    die2 = [ i for i in range(21) if i is not 9]
    
    ### Note how we initilize the two lists above
    ### We are using list comprehension here
    ### Try to understand how these list comprehensions work
    ### Essentially, within the square brackets, you are just describing what
    ### elements should be included in this list

    ### To simplify the implementation, we use 0 to represent the blank face
    ### It would not cause any trouble for our specific problem here
    
    ### Note in the following we use len(die1) and len(die2) instead of 20
    ### This is a good style, and sometimes this can avoid unnecessary mistakes
    
    d1 = random.randrange(len(die1))
    d2 = random.randrange(len(die2))
    
    ### fill in your code below to finish this function
    """We can't roll a 15 from the 1st die because the only other option would then be to roll a 9
       from the second die and there is no 9 on the second die. We can't also roll a blank on
       the first die because...well it's blank and there is no number 24 on the second die.
       We also can roll anything less than 4 on the first die because the highest number on the
       2nd die is 20 and adding anything less than 4 to 20 is less than 24. So we also can't roll a 1,2, or 3.
       This same logic would apply to our second die roll except that die 1 has no face value of 20 and thus 
       a roll of 4 for die2 is also invalid in this special case."""
    max_rolls = len(die1) * len(die2)
    #So for die1 we have these cases: cannot roll a 0,1,2,3 or 15
    #So for die2 we have these cases: cannot roll a 0,1,2,3 or 4
    """Now that we have all the acceptable rolls from both dies we can find all the acceptable pairs
       and divide by our max_rolls to get our probability. There are no other possible pairs except for these.
       We can also find all the combos using a n^2 solution to this problem, aka the brute force method, by just 
       iterating through both die1 and die2 and see which numbers add up to 24. I don't actually have to save
       the list of combos I could just increment a value but just so you can see all the combos."""

    #O(N^2) way to get all pairs
    """
    combos = []
    for i in die1:
    	for j in die2:
    		if i + j == 24:
    			combos.append((i,j))
    """
    #Math way to get all pairs
    """
    valid_die1 = [i for i in die1 if i > 3 and i != 0 and i != 15]
    valid_die2 = [i for i in die2 if i > 4 and i != 0]
    acceptable_pairs = []
    for i in valid_die1:
    	for j in range(len(valid_die2)-1,-1,-1):
    		acceptable_pairs.append((i,valid_die2[j]))
    		valid_die2.pop()
    		break
    """
    #Another way using zip
    """
    valid_die1 = [i for i in die1 if i > 3 and i != 0 and i != 15]
    valid_die2 = [i for i in die2 if i > 4 and i != 0][::-1]
    pairs = list(zip(valid_die1,valid_die2))
    """
    #Answer (just realized we have to use d1 and d2.....whoops)
    #dec_answer = len(pairs)/max_rolls
    #common_fraction = Fraction(len(pairs),max_rolls)
    x = 0
    if die1[d1] + die2[d2] == 24:
    	x += 1
    return x
    
### We use a simulation to estimate the probability described in the problem
### We roll the two dice 100 thousand times and check how many times the sum
### of the faces of the two dice is 24
    
trials = 100000
random.seed(15)
s = 0
is24()
for i in range(trials):
    s += is24()

print("The estimate of the probability is")
print((s/trials)/1.0)







