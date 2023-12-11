import gymnasium as gym
import numpy as np

env = gym.make('FrozenLake-v1', map_name="4x4", is_slippery=False, render_mode = 'human')

LEARNING_RATE = 0.1
DISCOUNT = 0.95
Action_SPACE = 4
EPISODES = 250
SHOW_EVERY = 20
REWARD_POSITION = 3 * 4 + 3

# env.reset()

print(env.observation_space)

OS_SIZE = [4]*4

q_table = np.random.uniform(low=0, high=1, size=OS_SIZE+[Action_SPACE])


for episode in range(EPISODES):
    if episode % SHOW_EVERY == 0:
        render = True
        print(episode)
    else:
        render  = False

    state = np.array(env.reset()[0])

    done = False
    while not done:
        action = np.argmax(q_table[state])
        new_state, reward, done, info, _ = env.step(action)
        print(new_state)
        if render:
            env.render()

        if not done:
            max_future_q = np.max(q_table[new_state])
            current_q = q_table[state+(action,)]
            new_q = (1-LEARNING_RATE)*current_q + LEARNING_RATE*(reward + DISCOUNT*max_future_q)
            q_table[state+(action,)] = new_q

        elif new_state == REWARD_POSITION:
            q_table[state+(action,)] = 1

        state = new_state

env.close()