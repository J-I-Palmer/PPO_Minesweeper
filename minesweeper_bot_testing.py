# James Palmer
# Program to test saved PPO model for Minesweeper

import gymnasium as gym
from gymnasium.envs import classic_control
from stable_baselines3 import PPO

# Creating the Gymnasium environment
boardSize = int(input("Enter the board size the model was trained on: "))
env = gym.make("MinesweeperEnv-v0", size = boardSize)

# Loading the trained model
model = PPO.load("ppo_minesweeper")

numWins = 0
avgGameDuration = 0
numGames = 10000
numTurns = 0
print("TESTING......")

# TRAINING LOOP
for i in range(numGames):
    obs, _ = env.reset()

    done = False
    while not done:
        action, states = model.predict(obs)
        obs, rewards, done, _, _ = env.step(action)
        numTurns += 1
    if env.unwrapped.isWin():
        numWins += 1
    avgGameDuration += env.unwrapped.getDuration()

# Calculating performance metrics
avgGameDuration = avgGameDuration / numGames
numTurns = numTurns / numGames
successRate = numWins / numGames * 100
        

print()
print(f"The model won {numWins} out of {numGames} games of Minesweeper for a success rate of {successRate:.2f}%.")
print(f"Each game took an average of {numTurns:.1f} turns and {avgGameDuration:.6f} seconds.")

