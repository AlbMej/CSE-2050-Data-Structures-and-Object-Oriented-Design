### In this assignment, we will count the number of inversions in a list.
### We will do so by making minor changes to the following mergesort code.
### If i < j and L[j] > L[i], then we say this is an inversion in list L.
### For example, the number of inversions in the following list L is 6.
### L = [4, 3, 2, 1]
### The number of inversions in the following list L is 0.
### L = [1, 2, 3, 4]
### The number of inversions in the following list L is 1.
### L = [1, 2, 4, 3]


def mergesort(L):
    # Base Case:
    if len(L) < 2:
        return
    
    # Divide!
    mid = len(L)//2
    A = L[:mid]
    B = L[mid:]
    
    # Conquer!
    mergesort(A)
    mergesort(B)
    
    # Combine!
    merge(A, B, L)
    
def merge(A, B, L):
    i = 0 # index into A
    j = 0 # index into B
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            L[i+j] = A[i]
            i = i + 1
        else:
            L[i+j] = B[j]
            j = j + 1
    # Add any remaining elements once one list is empty
    L[i+j:] = A[i:] + B[j:]

### Observe how we change the code from above to return the number of inversions

def sortandcount(L):
    # Base Case:
    if len(L) < 2:
        return 0
    # Divide!
    mid = len(L)//2
    A = L[:mid]
    B = L[mid:]
    
    # Conquer!
    count_a = sortandcount(A)
    count_b = sortandcount(B)
    
    # Combine!
    count = mergeandcount(A, B, L)
    return count_a + count_b + count

def mergeandcount(A, B, L):
    i = 0 # index into A
    j = 0 # index into B
    count = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            L[i+j] = A[i]
            i = i + 1
        else:
            ### add one line of code here
            count += (len(A) - i)
            L[i+j] = B[j]
            j = j + 1
    # Add any remaining elements once one list is empty
    L[i+j:] = A[i:] + B[j:]
    return count 

print("Before:")
L = [5, 4, 3, 2, 1]
print(L)
print("After:")
mergesort(L)
print(L)

print("Before:")
L = [5, 4, 3, 2, 1]
print(L)
print("After:")
print(sortandcount(L))
print(L)

### This is a nice example of divide and conquer.
### Analyze the running time of the algorithm.

print("-------------------------------------------------------")
L = [5, 4, 3, 2, 1]
print(sortandcount(L), 10)
L = [6, 5, 4, 3, 2, 1]
print(sortandcount(L), 15)
L = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(sortandcount(L), 45)
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sortandcount(L), 0)


