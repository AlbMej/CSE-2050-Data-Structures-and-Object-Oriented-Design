from itertools import permutations

class Configuration:
    def __init__(self, t):
        #Pennies are 1, dimes are 10, the blank space is 0 
        self.t = tuple(t)

    def moves(self):
        moves = []
        slow = fast = 0
        while fast < len(self.t) and slow < len(self.t):
            if slow > (fast + 2): break
            elif self.t[fast] == 0:
                if slow >= (fast - 2):
                    while slow <= (fast + 2) and slow < len(self.t):
                        if slow == fast: 
                            slow += 1
                            continue
                        temp = list(self.t)
                        temp[fast], temp[slow] = temp[slow], temp[fast]
                        moves.append(tuple(temp))
                        slow += 1
                else: slow +=1
            else:
                fast += 1
        return moves

    def moves(self):
        board = list(self.t)
        zero = board.index(0)
        for i in [-2,-1,1,2]: #Reachable positions away from i 
            coin = zero + i #Coin index
            if -1 < coin < len(self.t):
                board[zero],board[coin] = board[coin], board[zero]
                yield Configuration(board)
                board[coin], board[zero]= board[zero], board[coin]

    def moves(self):
        board = list(self.t)
        zero = board.index(0)
        moves = []
        for i in [-2,-1,1,2]:
            coin = zero + i
            if -1 < coin < len(self.t):
                board[zero],board[coin] = board[coin], board[zero]
                moves.append(Configuration(board))
                board[coin], board[zero]= board[zero], board[coin]
        return moves

    def __eq__(self, other):
        return self.t == other

    def __hash__(self):
        return hash(self.t)

