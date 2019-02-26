class Mapping:
	class Entry:
		def __init__(self, key, value):
			self.key = key
			self.value = value
		def __str__(self):
			return "%d: %s" % (self.key, self.value)
	
	# Child class needs to implement this!
	def get(self, key):
		raise NotImplemented

	# Child class needs to implement this!
	def put(self, key, value):
		raise NotImplemented

	# Child class needs to implement this!
	def __len__(self):
		raise NotImplemented

	# Child class needs to implement this!
	def _entryiter(self):
		raise NotImplemented

	def __iter__(self):
		return (e.key for e in self._entryiter())

	def values(self):
		return (e.value for e in self._entryiter())

	def items(self):
		return ((e.key, e.value) for e in self._entryiter())

	def __contains__(self, key):
		try:
			return (self.get(key) is not None)
		except:
			return False

	def __getitem__(self, key):
		return self.get(key)

	def __setitem__(self, key, value):
		self.put(key, value)

	def __str__(self):
		return "{%s}" % (", ".join([str(e) for e in self]))

class ListMapping(Mapping):
	def __init__(self):
		self._entries = []

	def put(self, key, value):
		e = self._entry(key)
		if e is not None:
			e.value = value
		else:
			self._entries.append(Mapping.Entry(key, value))

	def get(self, key):
		e = self._entry(key)
		if e is not None:
			return e.value
		else:
			raise KeyError

	def _entry(self, key):
		for e in self._entries:
			if e.key == key:
				return e
		return None

	def _entryiter(self):
		return (e for e in self._entries)

	def __len__(self):
		return len(self._entries)

class HashMapping(Mapping):
	def __init__(self, size = 100):
		self._size = size
		self._buckets = [ListMapping() for i in range(self._size)]
		self._length = 0

	def _entryiter(self):
		return (e for b in self._buckets for e in b._entryiter())

	def get(self, key):
		b = self._bucket(key)
		return b[key]

	def put(self, key, value):
		b = self._bucket(key)
		if key not in b:
			self._length += 1
		b[key] = value

		# Check if we need more buckets.
		if self._length > self._size:
			self._double()

	def __len__(self):
		return self._length

	def _bucket(self, key):
		return self._buckets[hash(key) % self._size]

	def _double(self):
		# Save the old buckets
		oldbuckets = self._buckets
		# Reinitialize with more buckets.
		self.__init__(self._size * 2)
		for bucket in oldbuckets:
			for key, value in bucket.items():
				self[key] = value

