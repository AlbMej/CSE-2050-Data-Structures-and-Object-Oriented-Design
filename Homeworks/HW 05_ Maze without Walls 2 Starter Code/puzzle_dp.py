from puzzle import Puzzle
from collections import deque

class PuzzleDP(Puzzle):

    def distances(self, end):
        rev = self.reverse()
        tovisit = {end}
        visited = set()
        dist = {end: 0}
        d = 1
        while tovisit:
            # Add all the tovisit positions to the visited set.
            visited.update(tovisit)
            # set s to be the set of positions that can reach the tovisit set.
            # Be sure to leave out those positions that were already visited.
            s = set.union(*(rev[p] for p in tovisit)) - visited
            # Update the distances to all the positions in s
            dist.update({p:d for p in s})
            # The set s is the next set to visit.
            tovisit = s
            # update the distance.
            d += 1
        return dist

    def getNeighbors(self, position, step):
    	neighbors = []
    	r, c = position
    	if self.onboard((r + step, c)): #Going down
    		neighbors.append((r + step, c))

    	if self.onboard((r, c + step)): #Going right
    		neighbors.append((r, c + step))

    	if self.onboard((r - step, c)): #Going up
    		neighbors.append((r - step, c))

    	if self.onboard((r, c - step)): #Going left
    		neighbors.append((r, c - step))

    	return neighbors

    """def pathsolve(self, start,end, visited = None, path = []):
                    path.append(start)
                    #visited.add(start)
            
                    #if not visited:
                    #    visited = set()
                    
                    if start == end: return path
                    r, c = start
                    step = self.maze[r][c]
                    for neighbor in self.getNeighbors(start, step):
                        if neighbor not in path:
                            path = self.pathsolve(neighbor, end, visited, path) 
                            #if newpath: return newpath
            
                    #path.add(end)
                    return path"""


    def pathsolve(self,start,end):
    	def pathsolve1(start,end, visited = None):
		    v = None
		    if not visited:
		        visited = set()
		    if start == end: return [end]
		    if start in visited: return None
		    visited.add(start)
		    if self.onboard(start):
		        r, c = start
		        step = self.maze[r][c]
		        if self.maze[r][c] == 0: return None

		        v = pathsolve1((r+step,c), end, visited) 
		        if v is not None:
		        	v.append(start)
		        	return v

		        v = pathsolve1((r,c+step), end, visited) 
		        if v is not None:
		        	v.append(start)
		        	return v

		        v = pathsolve1((r-step,c), end, visited) 
		        if v is not None:
		        	v.append(start)
		        	return v

		        v = pathsolve1((r,c-step), end, visited) 
		        if v is not None:
		        	v.append(start)
		        	return v
		    else:
		        return None
    	return pathsolve1(start,end)[::-1]

    def pathsolve(self, start, end, visited = None):
	    def pathsolve1(start,end, visited = None):
	        v = None
	        if not visited:
	            visited = set()
	        if start == end:
	        	x = deque([end])
	        	return x

	        if start in visited: return None
	        visited.add(start)
	        if self.onboard(start):
	            r, c = start
	            step = self.maze[r][c]
	            if self.maze[r][c] == 0: return None

	            v = pathsolve1((r+step,c), end, visited)  
	            if v is not None:
	                v.appendleft(start)
	                return v

	            v = pathsolve1((r,c+step), end, visited) 
	            if v is not None:
	                v.appendleft(start)
	                return v

	            v = pathsolve1((r-step,c), end, visited) 
	            if v is not None:
	                v.appendleft(start)
	                return v

	            v = pathsolve1((r,c-step), end, visited) 
	            if v is not None:
	                v.appendleft(start)
	                return v
	        else:
	            return None
	    return list(pathsolve1(start,end))

    def bfs(self, start, end):
        queue = deque([[start]])
        visited = set()
        while queue:
            path = queue.popleft()
            vertix = path[-1]
            if vertix == end: return path
            elif vertix not in visited:
                visited.add(vertix)
                for nbr in self.graph[vertix]:
                    queue.append(path + [nbr])
        
    def reverse(self):
        mappings = {}
        for r in range(len(self.maze)):
            for c in range(len(self.maze[0])):
                cur = (r,c)
                step = self.maze[r][c]
                neighbors = self.getNeighbors(cur, step)
                for i in neighbors:
                  if i in mappings:
                    mappings[i].add(cur)
                  else:
                    mappings[i] = set()
                    mappings[i].add(cur)
        return mappings

    def solve(self,start,end, visited = None):
        return min(self.distances(end)) != 0

