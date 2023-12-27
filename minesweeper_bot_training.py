# James Palmer
# PPO model to learn how to play Minesweeper
# This program is only the learning phase

import gymnasium as gym
from gymnasium.envs import classic_control
from stable_baselines3 import PPO

# creates Gym environment with board dimensions boardSize x boardSize
boardSize = int(input("Enter the size of the board you would like to create a model for: "))
env = gym.make("MinesweeperEnv-v0", size = boardSize)

# creates PPO model for given environment
# NOTE: batch_size, learning_rate, and total_timesteps can all be changed to modify
# how the model will learn.
# batch_size must be a multiple of 32
# learning rate is in the range of 0 to 1
model = PPO("MlpPolicy", env, batch_size = 32, learning_rate = 0.00001, verbose = 2)

# runs training for PPO model
model.learn(total_timesteps = 40000000)

# saves model in zip file
model.save("ppo_minesweeper")
print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('The model has been saved as "ppo_minesweeper".')
print(f'REMEMBER: This model will only work on {boardSize}x{boardSize} boards.')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
