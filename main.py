import gym

env = gym.make("MountainCar-v0", render_mode="rgb_array")
state = env.reset()

done = False

while not done:
    action = 2
    new_state, reward, done, info, _ = env.step(action)
    env.render()

env.close()