from fractions import gcd

class Box:
	def __init__(self, length, width, height):
		self.length = length
		self.width = width
		self.height = height

	def volume(self):
		return self.length * self.width * self.height

	def __lt__(self, other):
		return self.volume() < other.volume()

	def __eq__(self, other):
		return self.volume() == other.volume()

	def __le__(self, other):
		return self.volume() <= other.volume()

class Truck:
	def __init__(self, boxes):
		self.boxes = boxes

	def sort(self, key = None):
		self.boxes.sort(key = key)

	def sortbyvolume(self):
		self.boxes.sort(key = lambda v: v.volume())

	def sortbylength(self):
		self.boxes.sort(key = lambda v: v.length)

	def sortbyheight(self):
		self.boxes.sort(key = lambda v: v.height)

	def rotate(self, k):
		def reverse(L, start, end):
			if start < 0: end = -1
			while start < end:
				L[start], L[end] = L[end], L[start]
				start += 1
				end -= 1
			return L

		if k == 0 or k == len(self.boxes): return self
		if k < 0: 
			reverse(self.boxes, 0, len(self.boxes) - 1)
			reverse(self.boxes, k, len(self.boxes)-1)
			reverse(self.boxes, 0, len(self.boxes) - 1 + k)
		else:
			reverse(self.boxes, 0, len(self.boxes)-1)
			reverse(self.boxes, 0, k-1)
			reverse(self.boxes,k, len(self.boxes)-1)



	"""def rotate(self,k):
					step = k % len(self.boxes)
					num_of_sets = gcd(n,k)
					for i in range(0, gcd(n,k)):
						j = i
						temp = self.boxes[i]"""
"""lst = [Box(1, 1, 1), Box(1, 1, 1), Box(1, 1, 1), Box(1, 2, 1), Box(3, 1, 1), Box(1, 2, 2),
               Box(2, 2, 1), Box(4, 1, 1), Box(1, 5, 1), Box(1, 2, 3), Box(1, 6, 1), Box(7, 1, 1), Box(1, 7, 1)]
tr = Truck(lst)

print([b.volume() for b in tr.boxes])
tr.rotate(4)

print([b.volume() for b in tr.boxes])"""