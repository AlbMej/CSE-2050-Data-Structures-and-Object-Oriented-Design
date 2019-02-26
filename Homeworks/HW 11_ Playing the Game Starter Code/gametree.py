from nim import Nim

class GameTree:
    def __init__(self, gamestate):
        self.gamestate = gamestate
        self.moves = [GameTree(c) for c in self.gamestate.moves()]
        #self.moves.sort(key = lambda x: x.gamestate)

    def __str__(self):
        buf, out = [self], []
        while buf:
            out.append("{}".format([node.gamestate.rows for
             node in buf])) #gamestate.rows for Nim
            if any(node for node in buf):
                children = []
                for node in buf:
                    for subnode in node.moves:
                        children.append(subnode if subnode else GameTree())
                buf = children
            else:
                break
        return "\n".join(out)

    def currentwins(self):
        #returns True if and only if victory is ensured for the current player
        #first check for a draw and then check if the game is over (base cases!). 
        if self.gamestate.draw() or self.gamestate.isover(): return False
        return any([mv.currentloses() for mv in self.moves])

    def currentloses(self):
        #returns True if and only if every move the current player can make leads to a game
        #state where victory is ensured for the other player.
        #first check for a draw and then check if the game is over (base cases!).
        """Return True only if all recursive calls return True"""
        if self.gamestate.draw(): return False
        if self.gamestate.isover(): return True
        else: return all([mv.currentwins() for mv in self.moves]) 

    def currentdraws(self):
        return not self.currentwins() and not self.currentloses()

    def __eq__(self, other):
        return (self.game, self.moves) == (other.game, other.moves)

"""n1 = Nim([2,3,4])
g1 = GameTree(n1)
print(g1.currentwins(), True)

n3 = Nim([1,0,1,1])
g3 = GameTree(n3)
#print([mv.gamestate.rows for mv in g3.moves])
print(g3.currentwins(), False)"""


n1 = Nim([2,3,4])
g1 = GameTree(n1)
#print(g1.currentloses(), False)
n2 = Nim([1,0,1])
g2 = GameTree(n2)
#print(g2.currentloses(), False)
n3 = Nim([1,0,1,1])
g3 = GameTree(n3)
#print(g3.currentloses(), True)