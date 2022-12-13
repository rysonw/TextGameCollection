class Player(object):
    """
    A class for the player role in the Mancala Game
    """

    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name


class TicTacToe(object):
    """
    Class to represent function of a normal a TicTacToe game
     """
    def __init__(self):
        """
        Init for TicTacToe Object. Board is made up of a matrix.
        """
        self._board = [["", "", ""], ["", "", ""], ["", "", ""]]
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
        """
        print(self._board[0])
        print(self._board[1])
        print(self._board[2])


    def return_winner(self):
        """
        A function that returns the winner of the game.  
        We refer back to the self._board and check to see if the right indexes are 0.
        """

        # check for a horizontal win
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        
        # check for a vertical win
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]
        
        # check for a diagonal win
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        
        # check for a tie
        if all(all(square != ' ' for square in row) for row in self.board):
            return 'Tie'
        
        # if no winner or tie yet, the game continues
        return None
        

    def play_game(self, player_i, pos_i): #P1 is X, P2 is O
        """
        A function that simulates the tic-tac-toe game loop.
        """
        row = 9 // pos_i #Better way to grab index??
        col = pos_i
        
        while player_i > 3:
            col -= 3
            

        # check if the chosen square is empty
        if self.board[row][col] == ' ':
            # place the current player's token in the chosen square
            self.board[row][col] = self.current_player
            # switch to the other player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        


    #get/set functions

    def get_current_board(self):
        return self._board