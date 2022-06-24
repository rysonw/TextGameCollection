class ShipGame:
    def __init__(self):
        self.__board1 = [[False for x in range(10)] for y in range(10)]
        self.__board2 = [[False for x in range(10)] for y in range(10)]
        self.__game_state = "UNFINISHED"
        self.__current_turn = "first"
        self.__p1ships = 0
        self.__p2ships = 0

    def update_state(self):
        # updates the game state
        # check if complete board is False or Not
        # if complete board is not False, game is unfinished
        # if complete board is False, the opposite player has one
        if self.__current_turn == "first":
            for i in range(10):
                for j in range(10):
                    if self.__board1[i][j] == True:
                        return
            self.__game_state = "SECOND_WON"
        else:
            for i in range(10):
                for j in range(10):
                    if self.__board2[i][j] == True:
                        return
            self.__game_state = "FIRST_WON"

    def place_ship(self, player, length, coordinate, orientation):
        if length < 2 or length > 10:
            return False
        if player == "first":
            self.set_p1ships(1)
            if orientation == 'R':
                if ord(coordinate[0])-65 + length > 10:
                    return False
                for i in range(length):
                    if self.__board1[ord(coordinate[0])-65 + i][int(coordinate[1])-1] == True:
                        return False
                for i in range(length):
                    self.__board1[ord(coordinate[0])-65 +
                                  i][int(coordinate[1])-1] = True
                return True
            elif orientation == 'C':
                if int(coordinate[1])-1 + length > 10:
                    return False
                for i in range(length):
                    if self.__board1[ord(coordinate[0]) - 65][int(coordinate[1]) - 1 + i]:
                        return False
                for i in range(length):
                    self.__board1[ord(coordinate[0]) -
                                  65][int(coordinate[1])-1 + i] = True
                return True
        elif player == "second":
            self.set_p2ships(1)
            if orientation == 'R':
                if ord(coordinate[0])-65 + length > 10:
                    return False
                for i in range(length):
                    if self.__board2[ord(coordinate[0]) - 65 + i][int(coordinate[1]) - 1]:
                        return False
                for i in range(length):
                    self.__board2[ord(coordinate[0])-65 +
                                  i][int(coordinate[1])-1] = True
                return True
            elif orientation == 'C':
                if int(coordinate[1])-1 + length > 10:
                    return False
                for i in range(length):
                    if self.__board2[ord(coordinate[0])-65][int(coordinate[1])-1 + i] == True:
                        return False
                for i in range(length):
                    self.__board2[ord(coordinate[0]) -
                                  65][int(coordinate[1])-1 + i] = True
                return True
        else:
            return False

    def set_p1ships(self, x):
        self.__p1ships += x

    def set_p2ships(self, x):
        self.__p2ships += x

    def get_current_state(self):
        # returns either 'FIRST_WON', 'SECOND_WON', or 'UNFINISHED'
        return self.__game_state



    def get_current_state(self):
        # returns either 'FIRST_WON', 'SECOND_WON', or 'UNFINISHED'
        return self.__game_state

    def fire_torpedo(self, attacker, coordinate):
        if self.__game_state != "UNFINISHED" or attacker != self.__current_turn:
            if attacker == "first":
                self.__current_turn = "second"
            else:
                self.__current_turn = "first"
            return False
        if attacker == "first":
            self.__current_turn = "second"
        else:
            self.__current_turn = "first"
        if attacker == "first":
            self.__board2[ord(coordinate[0])-65][int(coordinate[1])-1] = False
        if attacker == "second":
            self.__board1[ord(coordinate[0])-65][int(coordinate[1])-1] = False
        self.update_state()
        return True

    def get_num_ships_remaining(self, player):
        # returns the number of ships remaining for the given player
        # player is either 'first' or 'second'

        if player == "first":
            return self.__p1ships

        elif player == "second":
            return self.__p2ships


game = ShipGame()
game.place_ship('first', 5, 'B2', 'C')
game.place_ship('first', 2, 'I8', 'R')
game.place_ship('second', 2, 'A1', 'C')
game.place_ship('first', 8, 'H2', 'R')
game.fire_torpedo('first', 'H3')
game.fire_torpedo('second', 'A1')
print(game.get_current_state())

