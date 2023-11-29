import gymnasium as gym
import numpy as np

env = gym.make('MountainCarContinuous-v0', render_mode="human")
env.reset()

Action_SPACE = 3
DISCRETE_OS_SIZE = [20]*len(env.observation_space.high)
discrete_os_win_size = (env.observation_space.high - env.observation_space.low)/DISCRETE_OS_SIZE

q_table = np.random.uniform(low=-2, high=0, size=DISCRETE_OS_SIZE+[Action_SPACE])

done = False

while not done:
    action = np.array([2])
    new_state, reward, done, info, _ = env.step(action)

env.close()