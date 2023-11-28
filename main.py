import gymnasium as gym
import numpy as np

env = gym.make('MountainCarContinuous-v0', render_mode="human")
env.reset()
done = False

while not done:
    action = np.array([2])
    new_state, reward, done, info, _ = env.step(action)
    env.render()

env.close()