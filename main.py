import gymnasium as gym
import numpy as np

env = gym.make('MountainCar-v0', render_mode="human")

LEARNING_RATE = 0.1
DISCOUNT = 0.95
Action_SPACE = 3

def get_discrete_state(state):
    discrete_state = (state - env.observation_space.low)/discrete_os_win_size
    return tuple(discrete_state.astype(np.int))

DISCRETE_OS_SIZE = [20]*len(env.observation_space.high)
discrete_os_win_size = (env.observation_space.high - env.observation_space.low)/DISCRETE_OS_SIZE

q_table = np.random.uniform(low=-2, high=0, size=DISCRETE_OS_SIZE+[Action_SPACE])

discrete_state = get_discrete_state(env.reset()[0])
print(discrete_state)

done = False

while not done:
    action = np.argmax(q_table[discrete_state])
    new_state, reward, done, info, _ = env.step(action)
    new_discrete_state = get_discrete_state(new_state)
    env.render()

    if not done:
        max_future_q = np.max(q_table[new_discrete_state])
        current_q = q_table[discrete_state+(action,)]
        new_q = (1-LEARNING_RATE)*current_q + LEARNING_RATE*(reward + DISCOUNT*max_future_q)
        q_table[discrete_state+(action,)] = new_q

    elif new_state >= env.goal_position:
        q_table[discrete_state+(action,)] = 0

    discrete_state = new_discrete_state

env.close()