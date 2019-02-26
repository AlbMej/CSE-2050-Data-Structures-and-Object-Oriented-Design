## Change the following sorting algorithms so that each algorithm returns
## the number of swaps between the list items,
## the number of comparisons between list items,
## and the sum of these two operations in the sorting algorithm

def bubblesort(L):
    count_s = count_c = 0
    keepgoing = True
    while keepgoing:
        keepgoing = False
        for i in range(len(L) - 1):
            count_c += 1
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                count_s += 1
                keepgoing = True
    return count_s, count_c, count_s + count_c

def selectionsort(L):
    count_s = count_c = 0
    n = len(L)
    for i in range(n-1):
        max_index = 0
        for index in range(n-i):
            count_c += 1
            if L[index] > L[max_index]:
                max_index = index
        L[n-i-1], L[max_index] = L[max_index], L[n-i-1]
        count_s += 1
    return count_s, count_c, count_s + count_c

def insertionsort(L):
    count_s = count_c = 0
    n = len(L)
    for i in range(n):
        j = n - i - 1
        count_c += 1
        while j < n-1 and L[j] > L[j+1]:
            count_s += 1
            L[j], L[j+1] = L[j+1], L[j]
            j += 1
    return count_s, count_c, count_s + count_c

## The following function runs one of the sorting algorithm on lists
## whose size doubles every time, and display the number of swaps, number of
## comparisons, and total number of operations, and their corresponding scaling
## factor.
## Here the scaling factor shows how the number of total operations increases
## when the list size doubles. If the algorithm is O(n^2), then the scaling
## factor should approach 4 when the list size is large.

def run(fun, k):
    print("---------------------------------------------------------------")  
    print(fun)
    counts_s = []
    counts_c = []
    all_counts = []
    for j in range(k):        
        L = [i for i in range(2**j, 0, -1)]
        result = fun(L)
        counts_s.append(result[0])
        counts_c.append(result[1])
        all_counts.append(result[2])
  
    print("Number of swaps:")
    print(counts_s)
    L1 = [counts_s[i+1]/counts_s[i] for i in range(1, len(counts_s)-1)]
    print("Scaling factors:")
    for num in L1:
        print("%4.2f" % (num), end = ' ')
    print()
    
    print("Number of comparison:")
    print(counts_c)
    L2 = [counts_c[i+1]/counts_c[i] for i in range(1, len(counts_c)-1)]
    print("Scaling factors:")
    for num in L2:
        print("%4.2f" % (num), end = ' ')
    print()
    
    print("Total operations:")
    print(all_counts)
    L3 = [all_counts[i+1]/all_counts[i] for i in range(1, len(all_counts)-1)]
    print("Scaling factors:")
    for num in L3:
        print("%4.2f" % (num), end = ' ')
    print()
    
run(bubblesort, 11)
run(selectionsort, 11)
run(insertionsort, 11)

