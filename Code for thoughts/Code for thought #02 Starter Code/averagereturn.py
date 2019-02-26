### Code for thought #2
### In this assignment, we use a function to calculate the average return of
### buying a powerball lottery ticket
### Below is the code we used in the previous code for thought
### The average return is just the diff we calucated below where we have
### diff = pay - cost

##print("Powerball calculator:")
##print("Input jackpot prize in million dollars.")
##jackpot = int(input())
##jackpot *= 1000000
##pay = jackpot*1/292201338.00
##pay = pay + 1000000/11688053.52
##pay = pay + 50000/913129.18
##pay = pay + 100/36525.17
##pay += 100/14494.11
##pay += 7/579.76
##pay += 7/701.33
##pay += 4/91.98
##pay += 4/38.32
##
##cost = 2
##diff = pay - cost
##
##print(jackpot, pay, diff)
##if diff > 0:
##    print("Buy!")
##else:
##    print("DO NOT BUY!!!")


def averagereturn(jackpot):
    ### Add your code below to finish this function
	jackpot *= 1000000
	pay = jackpot*1/292201338.00
	pay = pay + 1000000/11688053.52
	pay = pay + 50000/913129.18
	pay = pay + 100/36525.17
	pay += 100/14494.11
	pay += 7/579.76
	pay += 7/701.33
	pay += 4/91.98
	pay += 4/38.32

	cost = 2
	diff = pay - cost
	return diff





### Below code shows how to use a for loop for solve the problem of when should
### we buy a powerball lottery ticket.
### Note how the statemet
### break
### works
### Note when we loop this way, the jackpot value starts from 0 instead of 1

for jackpot in range(1000):
    if averagereturn(jackpot) > 0:
        print("Buy when jackpot is at least", jackpot, "millon dollars")
        break

### Below code shows how to solve the problem using a while loop

jackpot = 0
while averagereturn(jackpot) <= 0:
    jackpot += 1
print("Buy when jackpot is at least", jackpot, "millon dollars")
