def slowslicesum(L):
    return max((sum(L[i:j]), i, j) for j in range(len(L)+1) for i in range(j))

def quadraticslicesum(L):
    P = [sum(L[:i]) for i in range(len(L) + 1)]
    sums = []
    for j in range(len(L) + 1):
        for i in range(j+1):
            sums.append((P[j] - P[i], i, j))
    return max(sums)

def prefix(A, low = None, high = None):
	if low is None and high is None:
		low, high = 0, len(L)
	P = [0] * high
	P[low] = A[low]
	for k in range(low, high):
		P[k] = P[k - 1] + A[k]
	return P[-1], high

def prefix(L, low = None, high= None):
	if low is None and high is None:
		low, high = 0, len(L)
	mid = (low + high)//2
	left_sum = float('-inf')
	left_total = 0
	left_index = 0
	for i in range(low, high+1):
		left_total = sum(L[low:i])
		if left_total >= left_sum:
			left_sum, left_index = left_total, i
	return (left_sum,left_index)

def suffix(L,low = None, high= None):
	if low is None and high is None:
		low, high = 0, len(L)
	right_sum = 0
	right_total = 0 
	right_index = 0
	for j in range(high,low-1,-1):
		right_total = sum(L[j:high])
		if right_total >= right_sum:
			right_sum, right_index = right_total, j 
	return (right_sum,right_index)

def prefix(A, low = None, high = None):
	if low is None and high is None:
		low, high = 0, len(A)-1 
	prefix_sum = 0
	total = 0
	index = -1
	for k in range(low, high+1):
		total += A[k]
		if total >= prefix_sum:
			prefix_sum = total
			index = k
	return prefix_sum, index + 1

def suffix(A, low = None, high = None):
	if low is None and high is None:
		low, high = 0, len(A) 
	suffix_sum = 0
	total = 0
	index = high
	for k in range(high-1, low-1, -1):
		total += A[k]
		if total >= suffix_sum:
			suffix_sum = total
			index = k
	return suffix_sum, index 

"""def slicesum(nums):
    maxx = -2**31
    rs = 0
    for i in nums:   
        if rs + i < i:   
            rs = i  
        else:
            rs += i
        if rs > maxx:
           maxx = rs 
    return maxx

def slicesum(L, low = None, high = None):
	if not low and not high:
		low, high = 0, len(L)
	if low > high:
		return -2147483647
	mid = (low+high)//2

	#largest_prefix =  max(prefix(L, low,mid), largest_prefix, key = lambda x: x[0])
	#largest_suffix =  max(suffix(L, mid+1,high), largest_suffix, key = lambda x: x[0])
	right_prefix = prefix(L, mid+1, high)
	left_suffix =  suffix(L, low,mid+1)

	crossing_sum = left_suffix[0] + right_prefix[0]
	#largest_sum = max(left_suffix[0],right_prefix[0],crossing_sum)

	try_left = slicesum(L,low,mid)
	try_right = slicesum(L, mid+1, high) 

	return max(crossing_sum, max(right_prefix,left_suffix))

def slicesum(L):
	low, high = 0, len(L)
	#if low == high: return L[low]
	mid = (low+high)//2
	right_prefix = prefix(L[mid+1:])
	left_suffix =  suffix(L[:mid+1])
	crossing_sum = left_suffix[0] + right_prefix[0]
	biggest_slice = max(left_suffix[0],right_prefix[0],crossing_sum)

	print(left_suffix,right_prefix,biggest_slice,"*")
	return biggest_slice, left_suffix[1], mid+right_prefix[1]


def slicesum(L, low = None, high = None):
	if low is None and high is None:
		low, high = 0, len(L) - 1
	if low == high:
		print("**")
		return #L[low]
	mid = (low+high)//2

	#largest_prefix =  max(prefix(L, low,mid), largest_prefix, key = lambda x: x[0])
	#largest_suffix =  max(suffix(L, mid+1,high), largest_suffix, key = lambda x: x[0])
	right_prefix = prefix(L, mid+1, high)
	left_suffix =  suffix(L, low,mid+1)

	crossing_sum = left_suffix[0] + right_prefix[0]
	largest_sum = max(left_suffix[0],right_prefix[0],crossing_sum)

	try_left = slicesum(L,low,mid)
	try_right = slicesum(L, mid+1, high) 

	return max(crossing_sum, max(right_prefix,left_suffix))

def slicesum(L, low = None, high = None):
	if low is None and high is None:
		low, high = 0, len(L) - 1

	if low == high:
		print('Back up')
		return L[low]
	else:
		mid = (low+high)//2
		#print(low, mid, high)
		lefthalf = L[:mid+1]
		righthalf = L[mid+1:]

		right_prefix = prefix(righthalf)
		left_suffix =  suffix(lefthalf)
		crossing_sum = (left_suffix[0] + right_prefix[0], left_suffix[1],right_prefix[1])
		largest_sum = max(right_prefix,left_suffix,crossing_sum, key = lambda x: x[0])


		try_left = slicesum(L,low,mid)
		try_right = slicesum(L, mid+1, high)

		print(left_suffix, right_prefix, "*", crossing_sum, largest_sum)
		print()
		return largest_sum

def slicesum(L, low= None, high= None):
  if low is None and high is None:
    low, high = 0, len(L) - 1
		
  if low == high:
    return L[low], low, high
  
  mid = (low+high)//2
  right_prefix = prefix(L, mid+1, high)
  left_suffix = suffix(L, low, mid+1)
  crossing_sum = (left_suffix[0] + right_prefix[0], left_suffix[1],right_prefix[1])
  
  #print(left_suffix, right_prefix, "*", crossing_sum)
  return max(slicesum(L,low,mid), slicesum(L, mid+1, high), crossing_sum, key = lambda x: x[0])


def maxSubArrayHelper(nums, l, r):
  if max(nums) < 0: return 0,0,0
  if l > r: return -2147483647,l,r
  m = (l+r) // 2

  leftMax = suffix(nums, l, m)
  rightMax = prefix(nums, m, r)
  
  leftAns = maxSubArrayHelper(nums, l, m-1)
  rightAns = maxSubArrayHelper(nums, m+1 , r)
  cross = (leftMax[0]  + rightMax[0], leftMax[1],rightMax[1])
  
  #print(leftMax[0],nums[m],rightMax[0], leftAns[0], rightAns[0])
  return max(cross, max(leftAns, rightAns, key = lambda x: x[0]), key = lambda x: x[0])
        
def slicesum(nums):
  return maxSubArrayHelper(nums, 0, len(nums)-1)"""

def slicesum(L, low = None, high = None):
	if low is None and high is None:
		if max(L) <= 0: return 0,0,0
		low, high = 0, len(L) - 1
	if low == high: return L[low], low , high+1
	else:
		mid = (low+high)//2
		lefthalf = L[low:mid]
		righthalf = L[mid:high+1]

		#print(lefthalf, righthalf,"**")
		right_prefix = prefix(righthalf)
		left_suffix =  suffix(lefthalf)
		
		try_left = slicesum(L,low,mid)
		try_right = slicesum(L, mid+1, high)
		
		cross = (left_suffix[0] + right_prefix[0],low + left_suffix[1],mid + right_prefix[1])
		return max(cross,try_left,try_right, key = lambda x: x[0])


