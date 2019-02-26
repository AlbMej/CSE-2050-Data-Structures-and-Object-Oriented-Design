### Code for thought #6

### In this assignment, we read the following code and then run the code.
### Do we see the expected output? Why?

### Next, we fix the code so that it generates the expected output.

L = [i for i in range(10)]

### We want to print out the reversed list L
L.reverse()
print(L)

### What do you learn about functions(methods) from this assignment?
#The reverse function reverses the list inplace. To print it out we must call reverse on a prior line then print the list
#or call the funtion reversed which returns an iterator and then we can turn that into a list (list(reversed(list))).
