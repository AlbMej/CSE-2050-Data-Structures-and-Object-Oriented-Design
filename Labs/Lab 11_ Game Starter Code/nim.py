class Nim:
    def __init__(self, rows = [2,3,4]):
        self.rows = rows

    def isover(self):
        return self.rows.count(0) == len(self.rows)-1

    def moves(self):
        moves = []
        temprows = self.rows[:]
        for index,item in enumerate(self.rows):
            for j in range(item):
                moves.append(Nim(temprows[:index] + [j] + temprows[index+1:]))
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

