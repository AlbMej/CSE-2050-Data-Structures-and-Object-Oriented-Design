## Given a list of n integers stored in a non-decreasing order, find floor value of
## input ‘key’. If the key is in the list, then key will be returned. Otherwise, the
## floor value is defined as the largest number in the list that is smaller than the key.
## If such a number does not exist in the list, we return None.

## For example, L = [-1, 2, 3, 5, 6, 8, 9, 10] and key = 7, we should return 6 as outcome.
## On the other hand, if L = [1, 2, 3] and key = 0, we should return None.
## More examples: 
## L = [-2, -1, 0, 0, 0, 0, 2, 3, 4, 6], key = 0, and the output is 0.
## L = [-3, -1, 0, 2, 4, 5, 6, 7, 8, 12, 20], key = 100, and the output is 20.

## Implement the function floorvalue(L, key), so that code like the following can work correctly.
## print(floorvalue([-2, -1, 2, 3, 4, 6]), 5)

## The running time of the function needs to be O(log n), where n is the size of the input list. 

def floorvalue(L, item):
    ## add your code here
    left, right = 0, len(L)
    while right - left > 1:
    	mid = (right + left)//2
    	if item < L[mid]:
    		right = mid
    	else: 
    		left = mid
    return L[left] if L[left] <= item else None

L = [-3, -1, 0, 2, 4, 5, 6, 7, 8, 12, 20]
print("****************")
print(floorvalue(L, 0))
print(floorvalue(L, 7))
print(floorvalue(L, 100))

L = [0, 0, 2, 2, 3, 3, 3, 3, 3, 3, 4, 5, 10, 18, 45, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
print("****************")
print(floorvalue(L, 0))
print(floorvalue(L, 7))
print(floorvalue(L, 100))

L = [-2, -1, 0, 0, 0, 0, 2, 3, 4, 6]
print("****************")
print(floorvalue(L, 0))
print(floorvalue(L, 7))
print(floorvalue(L, 100))

L = [-3, -1, 0, 2, 4, 6, 7, 8, 12, 20, 22]
print("****************")
print(floorvalue(L, 0))
print(floorvalue(L, 7))
print(floorvalue(L, 100))

L = [2, 4, 5, 6, 7, 8, 12, 20]
print("****************")
print(floorvalue(L, 0))
print(floorvalue(L, 7))
print(floorvalue(L, 100))

L = [-3, -1, 0, 2, 6, 8, 12, 14, 20]
print("****************")
print(floorvalue(L, 0))
print(floorvalue(L, 7))
print(floorvalue(L, 100))

L = [i for i in range(1000000)]
print("****************")
print(floorvalue(L, -1))
print(floorvalue(L, 0))
print(floorvalue(L, 10000000))
