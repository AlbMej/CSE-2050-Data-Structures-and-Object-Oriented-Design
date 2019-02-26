### Code for thought #7
### In this assignment, we use a few examples to understand list comprehensions
### and learn how to use list comprehension to read files

L = [1, 2, 3, 4, 5]

for i in range(len(L)):
    L[i] += 10

print(L)

L = [1, 2, 3, 4, 5]

L = [ x + 10 for x in L]
print(L)

print([x + y for x in '456' for y in '123'])

A = '456'
B = '123'
### Use list comprehension to finish the following line of code so that
### the assert statement is does not lead to an error

L_AB = [y + x for y in B for x in A]                                  
assert(L_AB == ['14', '15', '16', '24', '25', '26', '34', '35', '36'])

### Below we learn how to use list comprehension and zip together to create
### two dimensional lists

L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]
print(zip(L1, L2))

print(list(zip(L1, L2)))

### Below we learn how to use list comprehension to handle files

### When you submit your code, comment out all the following code to ensure
### Mimir will not timeout

##f = open('list-comprehension.py')
##lines = f.readlines()
##f.close()
##for line in lines:
##    print(line)
##
##lines = [line.rstrip() for line in open('list-comprehension.py')]
##for line in lines:
##    print(line)
##
##lines = [line.rstrip().upper() for line in open("list-comprehension.py")]
##for line in lines:
##    print(line)
##    
##lines = [line.rstrip().upper().split() for line in open("list-comprehension.py")]
##for line in lines:
##    print(line)


