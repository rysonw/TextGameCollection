This is a class called ShipGame that allows two people to play the game [Battleship](https://en.wikipedia.org/wiki/Battleship_(game)). Each player has their own 10x10 grid they place their ships on. On their turn, they can fire a torpedo at a square on the enemy's grid. Player 'first' gets the first turn to fire a torpedo, after which players alternate firing torpedos. A ship is sunk when all of its squares have been hit. When a player sinks their opponent's final ship, they win.

The ShipGame class includes these methods:
* an init method that has no parameters and sets all data members to their initial values
* `place_ship` takes as arguments: the player (either 'first' or 'second'), the length of the ship, the coordinates of the square it will occupy that is closest to A1, and the ship's orientation - either 'R' if its squares occupy the same row, or 'C' if its squares occupy the same column (there are a couple of examples below). If a ship would not fit entirely on that player's grid, or if it would overlap any previously placed ships on that player's grid, or if the length of the ship is less than 2, the ship should not be added and the method should **return False**. Otherwise, the ship should be added and the method should **return True**. You may assume that all calls to place_ship() are made before any other methods are called (besides the init method, of course). You should not enforce turn order during the placement phase.
* `get_current_state` returns the current state of the game: either 'FIRST_WON', 'SECOND_WON', or 'UNFINISHED'.
* `fire_torpedo` takes as arguments the player firing the torpedo (either 'first' or 'second') and the coordinates of the target square, e.g. 'B7'. If it's not that player's turn, or if the game has already been won, it should just **return False**. Otherwise, it should record the move, update whose turn it is, update the current state (if this turn sank the opponent's final ship), and **return True**. If that player has fired on that square before, that's not illegal - it just wastes a turn. You can assume `place_ship` will not be called after firing of the torpedos has started.
* `get_num_ships_remaining` takes as an argument either "first" or "second" and returns how many ships the specified player has left.

Examples of the placeShip method:  
`place_ship('first', 4, 'G9', 'C')`

```
  1 2 3 4 5 6 7 8 9 10
A
B
C
D
E
F
G                 x
H                 x
I                 x
J                 x
```

`place_ship('second', 3, 'E3', 'R')`

```
  1 2 3 4 5 6 7 8 9 10
A
B
C
D
E     x x x
F
G                 
H                 
I                 
J                
```

As a simple example, your class could be used as follows:
```
game = ShipGame()
game.place_ship('first', 5, 'B2', 'C')
game.place_ship('first', 2, 'I8', 'R')
game.place_ship('second', 3, 'H2, 'C')
game.place_ship('second', 2, 'A1', 'C')
game.place_ship('first', 8, 'H2', 'R')
game.fire_torpedo('first', 'H3')
game.fire_torpedo('second', 'A1')
print(game.get_current_state())
```

WILL ADD A GAME LOOP WITH USER INPUT AT LATER DATE