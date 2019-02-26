# Playing the Game

For this assignment, you will implement some new methods on your `GameTree` class so that it can determine who will win a game.  We say that **victory is ensured** in a game if there is a way to play so that no matter what the other player does, you will still win.  This is the same as saying that you can make a move so that no matter what the other player does you can make a move so that no matter what the other player does you can make a move so that... until you win.

There are two main methods to implement:

  - `currentwins` - returns `True` if and only if  victory is ensured for the current player.

  - `currentloses` - returns `True` if and only if every move the current player can make leads to a game state where victory is ensured for the other player.

This will be a slightly odd kind of traversal of the GameTree because it will alternate between the two players.  The logic for `currentwins` and `currentloses` will be different (and opposite).  In both cases, you will want to first check for a draw and then check if the game is over (base cases!).
