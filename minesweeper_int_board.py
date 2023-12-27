# James Palmer
# Class Conversion of Minesweeper Game
# Changed so that board stores integers, not strings
# October 2023

import random

class Minesweeper:
    def __init__(self, size):
        self.size = size
        self.board = self.createBoard()

        # fills in non-mine tiles with number of adjacent mines
        for i in range(size):
            for j in range(size):
                self.countAdjMines(i, j)

        self.gameBoard = [[9 for _ in range(self.size)] for _ in range(self.size)]
        self.gameOver = False
        self.startTime = None

    # Creates the board that stores the mine locations and the number of adjacent mines
    # Return Value: 2D array representing Minesweeper board
    def createBoard(self):
        numMines = int(self.size**2 * 0.20) # 20% of tiles will be mines

        # creates board with placeholder value, 9
        board = [[9 for _ in range(self.size)] for _ in range(self.size)]

        # randomly selects mine locations
        mineLocs = random.sample(range(self.size**2), numMines)
        for tile in mineLocs: # creates row and column indices for mines
            row, col = divmod(tile, self.size)
            board[row][col] = -1

        return board

    # Counts the number of mines adjacent to a specified tile
    # and replaces the value stored in that tile with count of mines
    def countAdjMines(self, row, col):
        if self.board[row][col] != -1:
            count = 0

            # list of all possible directions to check
            directions = [[1,0], [-1,0], [0,-1], [0,1], [-1,1], [1,1], [-1,-1], [1,-1]]

            # loop that adds the values of directions to row and col
            # to search adjacent tiles
            for i in range(len(directions)):
                addr = directions[i][0]
                addc = directions[i][1]
                nrow = row + addr
                ncol = col + addc

                # checks to see if nrow and ncol are valid and then looks
                # to see if that tile contains a mine
                if(
                    nrow >= 0 and nrow < self.size and
                    ncol >= 0 and ncol < self.size and
                    self.board[nrow][ncol] == -1
                ):
                    count += 1

            self.board[row][col] = count

    # Prints the board that contains the locations of all mines and numbers of adjacent mines
    # Used as observation in minesweeper_env.py
    def printBoard(self):
        print('--------------')
        print('MINE LOCATIONS')
        print('--------------')
        print()
        # printing column labels
        print('    ' + ' '.join([str(i).rjust(2) for i in range(self.size)]))
        print('  --' + '-' * (self.size * 3))
        for i in range(self.size):
            print(str(i).ljust(2) + '|', end=' ')  # printing row labels
            for j in range(self.size):
                print(str(self.board[i][j]).rjust(2), end=' ')
            print()

    # Prints the player's board, with all 9s replaced by spaces
    def printGameBoard(self):
        print()
        print()
        # printing column labels
        print('    ' + ' '.join([str(i).rjust(2) for i in range(self.size)]))
        print('  --' + '-' * (self.size * 3))
        for i in range(self.size):
            print(str(i).ljust(2) + '|', end = ' ') # printing row labels
            for j in range(self.size):
                if self.gameBoard[i][j] == 9:
                    print('  ', end = ' ')
                else:
                    print(str(self.gameBoard[i][j]).rjust(2), end = ' ')
            print()

    # If the user selects a tile containing a 0, this function will uncover all adjacent tiles
    # containing 0s as well.
    def uncoverEmpty(self, row, col):
        # Checking that row and col are within range
        # and that the tile has not yet been uncovered
        # and that the tile contains a 0
        if(
            0 <= row and row < self.size and 0 <= col and col < self.size
            and self.gameBoard[row][col] == 9 and self.board[row][col] == 0
        ):
            self.gameBoard[row][col] = self.board[row][col]

            # list of all possible directions to check (no diagonals)
            directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

            # loop through recursive calls for each direction
            for i in range(len(directions)):
                addr = directions[i][0]
                addc = directions[i][1]
                nrow = row + addr
                ncol = col + addc
                self.uncoverEmpty(nrow, ncol)

    # Replaces the value in the player's board with the value stored in the mine-containing board
    def uncoverTile(self, row, col):
        if self.board[row][col] == -1:
            self.gameOver = True
        else:
            self.gameBoard[row][col] = self.board[row][col]

    # Replaces the value in the player's board with the value stored in the mine-containing board
    # Also calls uncoverEmpty if the player selects a 0
    def uncoverTilePlayer(self, row, col):
        if self.board[row][col] == -1:
            self.gameOver = True
        else:
            if self.board[row][col] == 0:
                self.uncoverEmpty(row, col)
            self.gameBoard[row][col] = self.board[row][col]

    # Returns true if the game resulted in a win, and a false if not.
    def isWin(self):
        return (all(self.gameBoard [i][j] != 9 or self.board[i][j] == -1 for i in range(self.size) for j in range(self.size)))

    # Allows a human player to play Minesweeper
    def playHuman(self):
        #self.printBoard()

        while not self.gameOver:
            self.printGameBoard()
            row = int(input("Enter row number: "))
            col = int(input("enter column number: "))
            self.uncoverTilePlayer(row, col)
                
            # checks if the player has uncovered all tiles that are not mines
            if self.isWin():
                   self.gameOver = True
                   self.printBoard()
                   print("Congratulations! You won!")

if __name__ == "__main__":
    size = int(input("Enter the size of the board: "))
    game = Minesweeper(size)
    game.playHuman()
