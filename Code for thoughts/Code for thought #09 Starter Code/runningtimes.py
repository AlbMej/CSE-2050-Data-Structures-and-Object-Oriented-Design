### In this assignment, we analyze the running time of different functions.
### Use the way we count atomic operations to sum up the number
### of atomic operations. Then use big-O notation to represent the running
### times of the following functions.

### In each of the following examples, assume the input is a list of length n.

def fun1(L):
    newlist = []  # 2: creating a new list and variable assignment
    for i in L: # loops n times
        if i % 2 == 0:  # 1
            newlist.append(i)   # 1 (append is constant time on lists)
    return newlist  # 1 return

def fun2(L):
    return [L[i] for i in range(len(L)) if i % 2 ==0]

def fun3(L):
    x = 0 # 1
    for i in L: #loop n times
        for j in L: #loop n times
            x += i*j # 3 two arithmetic operations and assignment
    return x #1        
        
def fun4(L):
    x = 0 #1
    for j in range(1, len(L)): # loops n - 1 times
        for i in range(j): # loop j times
            x += L[i] * L[j] #5 two list accesses, two arithmetic operations
                                # and assignment
    return x #1

def runfunc(func, n):
    import time
    start = time.time()
    L = [i for i in range(0, n)]   
    func(L)
    end = time.time()
    return end - start

def timetrials(func, k, trials =30):
    totaltime = 0
    for i in range(trials):
        totaltime += runfunc(func, k)
    print(func, "average = %10.7f for k = %d" % (totaltime/trials, k))

## Comment out these timetrails function calls before you submit to
## ensure Mimir will not time out
    
##timetrials(fun1, 1024)
##timetrials(fun1, 1024*2)
##timetrials(fun1, 1024*4)
##
##timetrials(fun2, 1024)
##timetrials(fun2, 1024*2)
##timetrials(fun2, 1024*4)
##
##timetrials(fun3, 1024)
##timetrials(fun3, 1024*2)
##timetrials(fun3, 1024*4)
##
##timetrials(fun4, 1024)
##timetrials(fun4, 1024*2)
##timetrials(fun4, 1024*4)

### In the list T, write the corresponding running times of the above functions
### If a function has running time O(1), wirte 0 in the corresponding location
### in the list T. If a function has running time O(n), write 1;
### If a function has running time O(n^2), write 2.
### For example, an example will look like the following

T = [1, 1, 2, 2]




