class Nim:
    def __init__(self, rows = [2,3,4]):
        self.rows = rows

    def isover(self):
        return sum(self.rows) == 1

    def moves(self):
        moves = []
        #print(self.rows, "ROWS")
        for index,item in enumerate(self.rows):
            #print(index,item, "EN")
            #if isinstance(item, Nim): print("Item:", item, item.rows, "MOVES")
            for j in range(item):
                moves.append(Nim(self.rows[:index] + [j] + self.rows[index+1:]))
                #print(moves, "MOVES")
        return moves

    def draw(self):
        return False

    # This way, we will be able to have ordered trees.
    def __lt__(self, other):
        self.rows < other.rows

    # We add a hash function so that we can have a set of Nim GameStates.
    def __hash__(self):
        return hash(tuple(self.rows))

    def __eq__(self, other):
        return self.rows == other.rows
"""
n1 = Nim([1,2,1])
n1moves = n1.moves()
mvlist = []
for mv in n1moves:
	mvlist.append(mv)
print(mvlist)
"""