class AMTicTacToe:
	def __init__(self, P1 = "X", board = "XXXOOOXXX"):
		self.board = board
		self.P1 = P1
		if P1 == "O": self.P2 = "X"
		else: self.P2 = "O"

	def moves(self):
		#return a list of all possible moves the current player can make.  A move is another `GameState`.
		P1,P2 = self.P1, self.P2
		moves = []
		for i in range(len(self.board)):
			if self.board[i] == "_":
				tempboard = self.board[:i] + P1 + self.board[i+1:]
				moves.append(TicTacToe(P1,self.board[:i] + P1 + self.board[i+1:]))
		return moves

	def isover(self):
		#return `True` if and only if the game is over and the current player has lost.
		total = 0
		for i in self.board:
			if total == 3: return True
			if i == self.P2: total +=1
			else: total = 0
		return False

	def draw(self):
		#return True if and only if the current game state is a draw (that is, a tie). *Note, there are no ties in Nim*.
		return self.board.count("O") + self.board.count("X") == len(board)

	def __hash__(self):
		return hash(tuple(self.board))

	def __eq__(self, other):
		return self._key == other._key

def wildcards(board):
    if '_' in board:
        indexes = [i for i, x in enumerate(board) if x == '_']
        final = []
        for _ in indexes:
            for val in ['O', 'X']:
                temp = [val if x == '_' else x for x in board]
                temp = ''.join(temp)
                final.append(temp)
        return final
    else:
        return [board]

class TicTacToe:
	def __init__(self, player = 'X', board = '_________'):
	        self.board = board
	        self.player = player

	def moves(self):
	    #Don't make any more moves after the game is over.
	    if not self.isover():
	        for i, mark in enumerate(self.board):
	            if mark == '_':
	                newboard = list(self.board)
	                #print(self.board, "board")
	                #print(newboard, "newboard")
	                newboard[i] = self.player
	                #print(newboard, "With player")
	                yield TicTacToe(self._otherplayer(), "".join(newboard))

	def isover(self):
		# The 8 possible lines
		#print(self._otherplayer(), "OTHER", self.board)
		lines = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
		for a,b,c in lines:
		    #print("abc", a,b,c)
		    if (self.board[a] == self.board[b] == self.board[c] == self._otherplayer()):
		        return True
		return False

	def draw(self):
		return '_' not in self.board

	def _key(self):
		return (self.board, self.player)

	def __lt__(self, other):
		self.board < other.board

	def __eq__(self, other):
		return self._key() == other._key()

	def _otherplayer(self):
		return 'X' if self.player == 'O' else 'O'

t1 = AMTicTacToe('X', 'OO_XX____')
#print([i.board for i in t1.moves()])

#t1 = TicTacToe('X', 'X__X__O_O')
t1 = TicTacToe('X', "XOX__XO_O")


print([i.board for i in t1.moves()])
#print([i.board for i in t1.moves()])
lines = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
for a,b,c in lines:
	print(a,b,c, "**")

for x,y in range(0,5):
	print(x,y)