class Puzzle:
	def __init__(self, maze):
		if not all(len(maze[0]) == len(i) for i in maze): raise ValueError
		self.maze = maze

	def onboard(self,position):
		x,y = position
		row, col= len(self.maze), len(self.maze[0])
		return (x >= 0 and x < row) and (y >= 0 and y < col)

	def __getitem__(self,position):
		if self.onboard(position): return self.maze[position[0]][position[1]]

	def rdsolve(self,start,end):
		if start == end: return True
		if self.onboard(start):
			r, c = start[0], start[1]
			step = self.maze[r][c]
			if self.maze[r][c] == 0: return False
			return self.rdsolve((r+step,c), end) or self.rdsolve((r,c+step), end)
		else:
			return False

	"""def solve(self,start,end, visited = None):
					if not visited:
						visited = set()
					if start == end: return True
					if start in visited: return False
					visited.add(start)
					if self.onboard(start):
						r, c = start[0], start[1]
						step = self.maze[r][c]
						if self.maze[r][c] == 0: return False
						return (self.solve((r+step,c), end, visited) 
							 or self.solve((r,c+step), end, visited) 
							 or self.solve((r-step,c), end, visited) 
							 or self.solve((r,c-step), end, visited) )
					else:
						return False"""

	def solve(self,start,end, visited = None):
		size = len(self.maze)
		if not visited:
			visited = set()
		if start == end: return True
		if start in visited: return False
		visited.add(start)
		r, c = start[0], start[1]
		step = self.maze[r][c]
		if self.maze[r][c] == 0: return False
		return ((r < size - step and self.solve((r+step,c), end, visited)) #down
			 or (c < size - step and self.solve((r,c+step), end, visited)) #right
			 or (r >= step and self.solve((r-step,c), end, visited)) #up
			 or (c >= step and self.solve((r,c-step), end, visited))) #left
		return False
