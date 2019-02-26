from scale import Scale
from bigScale import bigScale
import random

def defects(s):
    #return index of defective coin. Use weigh method to divide
    left, right = 0, len(s)-1
    #c= 0
    while left != right:
        #if c == 24: break
        mid = (left+right)//2
        #print(left,mid,right)
        if (right-left+1) % 2 == 0:
            if s.weigh((left,mid+1),(mid+1,right+1)) == 1:
                left = mid + 1
                #right2 = mid 
            elif s.weigh((left,mid+1),(mid+1,right+1)) == -1:
                right = mid
                #left2 = mid + 1
        else:
            #If defective coin is in the middle
            if s.weigh((left,mid),(mid + 1,right+1)) == 0 and s.weigh((left,mid),(mid,right+1)) == 1:
                return mid
            elif s.weigh((left,mid),(mid + 1,right+1)) == 1:
                left = mid + 1
            elif s.weigh((left,mid),(mid + 1,right+1)) == -1:
                right = mid -1
        #c += 1
    #print(left, left2, right, "***")
    return left


#L = [2,2,2,2,2,2,2,1]
#print(defects(Scale(L)), L.index(1))

"""L= [1,1,1,1,1,1,1,1,2]
s = Scale(L)
print(defects(s), 8)

L= [1,1,1,1,2,1,1,1,1]
s = Scale(L)
print(defects(s), 4)

L= [1,2,1,1,1]
s = Scale(L)
print(defects(s), 1)

L = [1,1,1,1,2,1,1,1]
print(defects(Scale(L)), L.index(2))
L2 = [1,1,1,1,2,1,1,1,1]
print(defects(Scale(L2)), L2.index(2))
L3 = [10,10,10,10,20,10,10,10,10]
print(defects(Scale(L3)), L3.index(20))

#L= [1] * 1 + [2] + [1] * 10
#L= [1, 2, 1, 1]

L = [1,2,1,1,1,1]
s = Scale(L)
print(defects(s), L.index(2))"""

