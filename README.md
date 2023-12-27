# PPO_Minesweeper
This is a series of programs that implement OpenAI's Proximal Policy Optimization algorithms in order to create a model that can play the game of Minesweeper.

Present are two different versions of Minesweeper that can be played by a user or used to train a model. Additionally, a Gymnasium environment that provides the interface for interaction between the model and the Minesweeper program is included.
Lastly, the training and testing programs are included for model creation, training, and testing.

The following are instructions for use of the Minesweeper game, environment, and PPO model included in this zip file. First some libraries need to be downloaded: gymnasium, numpy, and stable_baselines3.

Once all three of the above libraries (and their dependencies) have been installed, minesweeper_env.py will need to be registered in the gymnasium library. Navigate to where the Gymnasium library code was stored. For example, the path may look like: <pre>C:\Users\ example \AppData\Local\Programs\Python\Python311\Lib\site-packages\gymnasium</pre> Once inside of the Gymnasium library, navigate to the envs directory. Once there, navigate to the classic_control directory. Paste minesweeper_env into this directory. Next, the file __init__.py inside of the classic_control directory will need to be edited to include this line:
from gymnasium.envs.classic_control.minesweeper_env import MinesweeperEnv

Then, navigate back to the envs directory and edit its __init__.py file by adding the following: 
<pre>register(
  id='MinesweeperEnv-v0',
  entry_point="gymnasium.envs.classic_control.minesweeper_env:MinesweeperEnv",
  max_episode_steps=1000,
)</pre>

This will register the Minesweeper environment under the name “MinesweeperEnv-v0”. Now that the environment has been registered, the PPO model programs can be run. 

NOTE: The training program must be run before the testing program. Failure to do so will result in a runtime error since the testing program will attempt to access a file that does not exist yet.
To start training the PPO model, run minesweeper_bot_training.py. This program will only take one input from the user: the size of the board. All Minesweeper boards produced by minesweeper_int_board.py and minesweeper_int_board_simplified.py create boards that have the same size for both height and width, so only one integer is taken as input. Therefore, the total number of tiles on the board will be the square of the input. Once the training period has completed, minesweeper_bot_testing can be run to evaluate the effectiveness of the model. You will need to input the size of the board again since the Gymnasium environment must be constructed again. The testing program will run for a fairly long time, so do not close it early thinking that something is wrong with it. Once testing has concluded, you will be presented with statistics on the model’s performance.

If you would like to play Minesweeper yourself, both minesweeper_int_board and minesweeper_int_board_simplified have that functionality. Just run either program by itself and you can play as much Minesweeper as you would like.
