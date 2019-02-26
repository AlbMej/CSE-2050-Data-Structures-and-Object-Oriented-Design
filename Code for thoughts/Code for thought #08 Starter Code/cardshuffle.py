### Code for thought #8
### In this assignment, we use an example to show that how one can improve run time
### of an algorithm by using some commonly used list operations more carefully.
### Specifically, we will implement a perfect shuffle algorithm to shuffle cards.
### Here are some interesting questions and facts about cards.
### Q: How many times should one mix a standard deck of cards to ensure that they
### are well shuffled?
### A: First, when we mention mixing cards, we mean a riffle shuffle. In 1992,
### researchers studied this problem with both computer simulations and mathematical
### proofs. They concluded that seven shuffles is enough to mix the cards well.

### What if we do perfect shuffles? A perfect riffle shuffle cuts the deck exactly
### in half and the shuffle perfectly alternates the cards with the top card staying
### on top. For example, a perfect shuffle permutes the cards numbered
### [1, 2, 3, 4, 5, 6, 7, 8] to [1, 5, 2, 6, 3, 7, 4, 8].

### In the following, I implemented a slower version of perfect shuffle.
### You job is to implement a fast version of the perfect shuffle.

import time
def perfectshuffle(cards):
    n = len(cards)
    cards1 = cards[:n//2][::-1]
    cards2 = cards[n//2:][::-1]
    cards.clear()
    for i in range(n//2):
        cards.append(cards1.pop())
        cards.append(cards2.pop())

    ### Add your code here

def perfectshuffleslow(cards):
    n = len(cards)
    ### Note here one has to use // instead of / for division. Find out why.
    cards1 = cards[:n//2]
    cards2 = cards[n//2:]

    ### It is worth mentioning that if we change the following line of code to be
    ### cards = []
    ### then this function will not work any more. Try it out and find out the reason.
    ### One should remember this since this could be a common mistake.
    
    cards.clear()
    for i in range(n//2):
        cards.append(cards1.pop(0))
        cards.append(cards2.pop(0))

def runperfectshuffle(n):
    start = time.time()
    cards = [ i for i in range(n)]   
    perfectshuffle(cards)
    end = time.time()
    return end - start

def runperfectshuffleslow(n):
    start = time.time()
    cards = [ i for i in range(n)]   
    perfectshuffleslow(cards)
    end = time.time()
    return end - start

### It can be proven that for a standard 52-card deck, after 8 consecutive perfect
### shuffles,  the shuffled deck will have the same order as the original deck.
### Run the following code to show it is the case.

n = 52
cards = [ i for i in range(n)] 
for i in range(8):
    perfectshuffleslow(cards)
    print("Shuffle", i + 1)
    print(cards)


def timetrials(func, k, trials =50):
    totaltime = 0
    for i in range(trials):
        totaltime += func(k)
    print("average = %10.7f for k = %d" % (totaltime/trials, k))

### Once you have implemented the perfectshuffle function correctly.
### Uncomment the following code and run the code to obtain the run time
### of your perfectshuffle function.
### Compare it with the run time of perfectshuffleslow and see whether you have
### dramatic improvement. (There should be dramatica improvement :)
### Note when you submit your code, you should comment out the following code to ensure
### Mimir will not time out.
    
"""print("perfectshuffle:")
timetrials(runperfectshuffle, 1024)
timetrials(runperfectshuffle, 1024*2)
timetrials(runperfectshuffle, 1024*4)
timetrials(runperfectshuffle, 1024*8)
timetrials(runperfectshuffle, 1024*16)
timetrials(runperfectshuffle, 1024*32)
timetrials(runperfectshuffle, 1024*64)
##
##
print("perfectshuffleslow:")
timetrials(runperfectshuffleslow, 1024)
timetrials(runperfectshuffleslow, 1024*2)
timetrials(runperfectshuffleslow, 1024*4)
timetrials(runperfectshuffleslow, 1024*8)
timetrials(runperfectshuffleslow, 1024*16)
timetrials(runperfectshuffleslow, 1024*32)
timetrials(runperfectshuffleslow, 1024*64)"""

### Below are from my output.
### It should be very clear that the runtime of perfectshuffle is O(n).
### The runtime of of pefectshuffleslow is O(n^2) even though is not as obvious
### as the pefectshuffle case.


##perfectshuffle:
##average =  0.0002650 for k = 1024
##average =  0.0005166 for k = 2048
##average =  0.0009799 for k = 4096
##average =  0.0020554 for k = 8192
##average =  0.0043387 for k = 16384
##average =  0.0088631 for k = 32768
##average =  0.0177036 for k = 65536
##perfectshuffleslow:
##average =  0.0003640 for k = 1024
##average =  0.0007698 for k = 2048
##average =  0.0018791 for k = 4096
##average =  0.0068081 for k = 8192
##average =  0.0233809 for k = 16384
##average =  0.0882502 for k = 32768
##average =  0.3961268 for k = 65536

        
