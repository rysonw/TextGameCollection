
class Player(object):
    """
    A class for the player role in the Mancala Game
    """

    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name


class Mancala(object):
    """
    Class to represent function of a normal Mancala game
     """
    def __init__(self):
        """
        Init for Mancala object, currently includes the board which is
        a matrix; one array for each player's board. Also includes 
        the number of current active player objects
        """
        self._board = [[4, 4, 4, 4, 4, 4, 0], [4, 4, 4, 4, 4, 4, 0]] #pit, pit, pit, pit, pit, pit, store
        self._curr_number_players = 0
        self._current_player_turn = "player1"
        self._p1_name = ""
        self._p2_name = ""

    def create_player(self, name):
        """
        A function that creates a player object. There can only be 2 players max. 
        Current number of player objects gets updated.
        """
        if self._curr_number_players == 0:
            p1 = Player(name)
            self._curr_number_players += 1
            self._p1_name = p1.get_name()
            return p1
        elif self._curr_number_players == 1:
            p2 = Player(name)
            self._curr_number_players += 1
            self._p2_name = p2.get_name()
            return p2
        else:
            return


    def print_board(self):
        """
        A function that returns stats about the current state of the board. 
        We refer back to the self._board and print the indexes to satisfy the requirements
        needed.
        """
        store1 = str(self._board[0][6])
        store2 = str(self._board[1][6])

        print("player1: ")
        print("store: " + store1)
        print(self._board[0][0:6])

        print("player2: ")
        print("store: " + store2)
        print(self._board[1][0:6])


    def return_winner(self):
        """
        A function that returns the winner of the game if one player's pits are empty.  
        We refer back to the self._board and check to see if the right indexes are 0.
        """
        if self._board[0][0:6] == [0, 0, 0, 0, 0, 0]:
            p2_remaining = 0
            for i in range(6): #Grab remaining marbles from other player's side
                if self._board[1][i] != 0:
                    p2_remaining += self._board[1][i]
                    self._board[1][i] = 0
            
            self._board[1][6] += p2_remaining
            
        elif self._board[1][0:6] == [0, 0, 0, 0, 0, 0]:
            p1_remaining = 0
            for i in range(6): #Grab remaining marbles from other player's side
                if self._board[0][i] != 0:
                    p1_remaining += self._board[0][i]
                    self._board[0][i] = 0
            
            self._board[0][6] += p1_remaining

        else:
            return "Game has not ended"

        #Compare both stores

        if self._board[0][6] > self._board[1][6]:
            return "Winner is player 1: " + self._p1_name
        
        elif self._board[0][6] < self._board[1][6]:
            return "Winner is player 2: " + self._p2_name
        
        else:
            return "It's a tie"

    def play_game(self, player_i, pit_i):
        """
        A function that simulates the mancala game loop. This function is the center of the code
        and will use the return_winner function
        """
        if pit_i > 6 or pit_i <= 0:
            return "Invalid number for pit index"

        if (player_i == 1 and self._current_player_turn != "player1") or (player_i == 2 and self._current_player_turn != "player2"):
            return "Invalid Player"

        if self._board[0][0:5] == [0, 0, 0, 0, 0, 0] or self._board[1][0:5] == [0, 0, 0, 0, 0, 0]:
            self.return_winner()

        #Save current pit marble number in temp variable and distribute, 
        #if we reach the end of an array then we check to see which player it is
        #and check to see if this is their store

        #Perform a check to see if the pit actually has marbles

        marbles_to_move = self._board[player_i - 1][pit_i - 1] #temp variable
        self._board[player_i - 1][pit_i - 1]  = 0 #Replace index with 0
        board_side = player_i - 1
        turn_again = False #Flag for turn repeats

        while marbles_to_move > 0:
            pit_i += 1

            if pit_i - 1 == 6: #Check for skipping opposite player's store
                if board_side != player_i - 1:
                    continue
            
            if marbles_to_move == 1: #Special Rules Check
                if pit_i - 1 == 6 and player_i - 1 == board_side: #Special Rule #1
                    self._board[board_side][pit_i - 1] += 1 #Increase Store
                    marbles_to_move -= 1
                    turn_again = True
                    print(self._current_player_turn + " take another turn.")
                    continue
                elif board_side == player_i - 1 and self._board[board_side][pit_i - 1] == 0: #Special Rule #2
                    if player_i == 1:
                        self._board[0][6] += (self._board[1][6 - pit_i] + 1)
                    elif player_i == 2:
                        self._board[1][6] += (self._board[0][6 - pit_i] + 1)
                    marbles_to_move -= 1
                    continue
                else: #Last Marble lands on a non-empty pit that is not a store
                    self._board[board_side][pit_i - 1] += 1
                    marbles_to_move -= 1
                    continue
            
            if pit_i - 1 == 6 and board_side == 0: #swapping to otherside of the mancala board
                if player_i == 1:
                    self._board[0][6] += 1
                    marbles_to_move -= 1
                board_side = 1
                pit_i = 0
                continue
            elif pit_i - 1 == 6 and board_side == 1:
                if player_i == 2:
                    self._board[1][6] += 1
                    marbles_to_move -= 1
                board_side = 0
                pit_i = 0
                continue

                        
            self._board[board_side][pit_i - 1] += 1
            marbles_to_move -= 1         

        if turn_again == False: #update current player turn
            if self._current_player_turn == "player1":
                self._current_player_turn = "player2"
            else:
                self._current_player_turn = "player1"

        turn_again = False
        
        return list(self._board[0] + self._board[1])


    #get/set functions

    def get_current_board(self):
        return self._board


