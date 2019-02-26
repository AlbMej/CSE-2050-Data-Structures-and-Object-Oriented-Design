from boxarrangement import *
from intfunction import *
import random

class OrganizedTruck:
	def __init__(self, truck):
		self.truck = truck 

	def __iter__(self):
		smallest_index = self.find_min_index()

		for box in range(smallest_index, len(self)):
			yield self[box]

		for box in range(0, smallest_index):
			yield self[box]

	def __getitem__(self,index):
		return self.truck.boxes[index]

	def __len__(self):
		return len(self.truck.boxes)

	def find_min_index(self):
		left, right = 0, len(self)-1
		while left < right:
			middle = (left + right) // 2
			if self[middle] < self[right]:
				right = middle
			elif self[middle] > self[right]:
				left = middle+1
			else:
				right -=1 
		return left

	def min(self):
		left, right = 0, len(self)-1
		while left < right:
			middle = (left + right) // 2
			if self[middle] < self[right]:
				right = middle
			elif self[middle] > self[right]:
				left = middle+1
			else:
				right -=1 
		return self[left]

	def max(self):
		left, right = 0, len(self)-1
		while left < right:
			middle = (left + right) // 2
			if self[middle] < self[left]:
				right = middle - 1
			elif self[middle] > self[left]:
				left = middle
			else:
				left +=1 
		return self[left]

	def lower_bound(self, box):
		left = 0
		right = len(self) - 1
		lowest = -1
		while left <= right: 
			middle = (left + right) // 2
			#print(left,middle,right, '--->', self[left].volume(),self[middle].volume(),self[right].volume())
			#print([b.volume() for b in self.truck.boxes])
			#print()
			if self[middle] == box:
				lowest = middle
				right = middle -1

			elif self[left] <= self[middle]:
				if box >= self[left] and box <= self[middle]:
					right = middle - 1
				else:
					left = middle + 1
			elif box >= self[middle] and box <= self[right]:
				left = middle + 1
			else: 
				right = middle - 1
		return lowest

	def higher_bound(self, box):
		left = 0
		right = len(self) - 1
		highest = -1
		while left <= right: 
			middle = (left + right) // 2		
			#print(left,middle,right, '--->', self[left].volume(),self[middle].volume(),self[right].volume())
			#print([b.volume() for b in self.truck.boxes])
			#print()
			if self[middle] == box:
				highest = middle
				left = middle + 1

			if self[left] <= self[middle]:
				#if box == 

				if box >= self[left] and box < self[middle]:
					right  = middle - 1
				else:
					left = middle + 1
			if box >= self[middle] and box <= self[right]:
				left = middle + 1
			else: 	
				right = middle - 1
		#print(highest, "+")
		return highest

	def search(self, box):
		count = []
		low = self.lower_bound(box)
		high = self.higher_bound(box)
		if low == -1 and high == -1: return None
		if low == -1 or high == -1: return [box]
		return [box] * (high - low + 1)
		


l = [1,1,1,2,3,4,4,4,5,6,6,7,7]
 #   0,1,2,3,4,5,6,7,8,9,10,11,12
l = [6,6,7,7,1,1,1,2,3,4,4,4,5]
lst = [Box(1, 1, 1), Box(1, 1, 1), Box(1, 1, 1), Box(1, 2, 1), Box(3, 1, 1), Box(1, 2, 2),
       Box(2, 2, 1), Box(4, 1, 1), Box(1, 5, 1), Box(1, 2, 3), Box(1, 6, 1), Box(7, 1, 1), Box(1, 7, 1)]
tr = Truck(lst)
tr.rotate(4)
ot = OrganizedTruck(tr)

#print([b.volume() for b in ot.truck.boxes])
#print([b.volume() for b in ot.search(Box(2, 2, 1))], [4, 4, 4])
#print([b.volume() for b in ot.search(Box(1, 1, 6))], [6, 6])

#print([ot.lower_bound(Box(1, 1, 6))] , "|", 0)
#print([ot.higher_bound(Box(1, 1, 6))] , "|", 1)
#print([b.volume() for b in ot.search(Box(1, 1, 1))], [1, 1, 1])
#print(ot.search(Box(1, 1, 0)), None)
#print(ot.search(Box(1, 4, 3)) == None)
tr.rotate(4)

#print([b.volume() for b in tr.boxes])
#print([b.volume() for b in ot.search(Box(2, 2, 1))], [4, 4, 4])
#print([b.volume() for b in ot.search(Box(1, 1, 6))], [6, 6])
#print([b.volume() for b in ot.search(Box(2, 1, 1))], [2])