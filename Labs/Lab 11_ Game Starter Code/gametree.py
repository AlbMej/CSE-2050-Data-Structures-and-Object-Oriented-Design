from nim import Nim

class GameTree:
    def __init__(self, gamestate):
        self.moves = set() #The children AKA all possible 
        for mv in gamestate.moves():
        	if len(mv.rows) == 1: return
        	#print([m for m in mv.rows], gamestate.moves())
        	self.moves.add(GameTree(Nim(mv.rows)))


#Below is a basic gamestate (Incase I ever want to implement another game).
class GameState:
	def __init__(self):
		pass

	def moves(self):
		#return a list of all possible moves the current player can make.  A move is another `GameState`.
		pass

	def isover(self):
		#return `True` if and only if the game is over and the current player has lost.
		pass

	def draw(self):
		#return True if and only if the current game state is a draw (that is, a tie). *Note, there are no ties in Nim*.
		pass

