# James Palmer
# Custom OpenAI Gym Minesweeper Environment
# October 2023

import gymnasium as gym
from gymnasium import spaces
import numpy as np
import time
from minesweeper_int_board_simplified import Minesweeper

class MinesweeperEnv(gym.Env):

    def __init__(self, render_mode = None, size = 10):
        self.startTime = 0
        self.firstTurn = True
        self.size = size
        self.minesweeper = Minesweeper(self.size)
        self.done = False
        self.gameDuration = 0
        self.numTurns = 0
        self.action_space = spaces.Discrete(self.size**2)
        self.observation_space = spaces.Box(low=-1, high=9, shape=(self.size, self.size), dtype=np.int64)

        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode
        
    # Resets all variables back to their original state and starts a new game of Minesweeper
    def reset(self, options=None, seed=None):
        self.minesweeper = Minesweeper(self.size)
        self.done = False
        self.firstTurn = True
        self.gameDuration = 0
        self.startTime = 0
        return self.getObservation(), {}

    # Performs the action specified by the model and calculates the appropriate reward
    def step(self, action):
        if self.firstTurn:
            self.startTime = time.time()
            self.firstTurn = False
        
        if self.done:
            raise ValueError("Episode has ended. Please reset the environment to try again.")

        row, col = divmod(action, self.size)
        # make uniqueMove true if uncovering a new tile
        uniqueMove = (self.minesweeper.gameBoard[row][col] == 9)
        self.minesweeper.uncoverTile(row, col)
        self.done = self.minesweeper.gameOver

        # calculating final reward
        if self.done:
            self.gameDuration = time.time() - self.startTime

            # calculating reward value on loss
            if not self.minesweeper.isWin():
                reward = -5

            # reward value on win
            else:
                reward = 10
                #print('WIN!')

        # calculating per-move reward
        else:
            if uniqueMove:
                reward = 1
            else:
                reward = -0.5

        return self.getObservation(), reward, self.done, False, {}

    # Returns a numpy array conversion of the 2D player board
    def getObservation(self):
        return np.array(self.minesweeper.gameBoard, dtype=np.int64)

    # Displays the player board
    def render(self):
        self.minesweeper.printGameBoard()

    # Displays the board that contains the locations of all mines
    def renderFinal(self):
        self.minesweeper.printBoard()

    # Returns true if the game ended in a win and false if not
    def isWin(self):
        return self.minesweeper.isWin()

    # Returns the duration of the game in seconds
    def getDuration(self):
        return self.gameDuration

    # no files / resources are in use, so close
    # does not do anything
    def close(self):
        pass
