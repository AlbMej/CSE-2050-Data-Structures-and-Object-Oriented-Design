from configuration import Configuration
from collections import deque

class CoinPuzzle:
    def __init__(self, pennies, dimes):
        self.board = Configuration((1,) * pennies + (10,) * dimes + (0,))
        self.graph = self.create_graph(self.board)

    def create_graph(self, board, vertices = [], graph = {}):
        moves = board.moves()
        graph[board] = set(moves)
        for mv in moves:
            if mv not in vertices:
                vertices += [mv]
                self.create_graph(mv,vertices, graph)
        return graph

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


    def bfs2(self, start, end):
        tovisit = deque([(start, [(start)])])
        visited = set()
        while tovisit:
            vertix,path = tovisit.popleft()
            if vertix == end: return path
            elif vertix not in visited:
                visited.add(vertix)
                for nbr in self.graph[vertix]:
                    tovisit.append((nbr,path + [nbr]))
            
    def solve(self,a,b):
        return self.bfs(a,b)