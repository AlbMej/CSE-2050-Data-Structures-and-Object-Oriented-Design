### In this assignment, we modify the binary search algorithm we covered in
### class, so that it can returns the index of the item, if the item is in the
### sorted list L. Otherwise, it returns None.
### Note the binary search code in class only returns True but not the index if
### the item is in the sorted list L.


def bs(L, item):
    left, right = 0, len(L)
    while right - left > 1:
        median = (right + left)//2
        if item < L[median]:
            right = median
        else:
            left = median
    return right > left and L[left] == item

def bs1(L, item):
    left, right = 0, len(L)
    while right - left > 1:
        median = (right + left)//2
        if item < L[median]:
            right = median
        else:
            left = median
    ### add your code below
    if right > left and L[left] == item: return left

L = [i for i in range(20)]
print(L)
items = [10 + i for i in range(20)]
for item in items:
    print(item, bs(L, item), bs1(L, item))

print()
print(bs1(L, 20), None)

