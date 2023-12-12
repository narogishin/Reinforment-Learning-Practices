import gymnasium as gym
import numpy as np

env = gym.make('CartPole-v1', render_mode="human")

LEARNING_RATE = 0.5
DISCOUNT = 0.95
Action_SPACE = 2
EPISODES = 2500
SHOW_EVERY = 200
EPSILON = 0.1

GOAL_ANGLE = env.observation_space.high[2]/8
print(" goal angle : ", GOAL_ANGLE)

# print(env.reset()[0])

def get_discrete_state(state):
    discrete_state = (state - env.observation_space.low)/discrete_os_win_size
    return tuple(discrete_state.astype(np.int64))

DISCRETE_OS_SIZE = [5]*len(env.observation_space.high)
discrete_os_win_size = (env.observation_space.high - env.observation_space.low)/DISCRETE_OS_SIZE

q_table = np.random.uniform(low=0, high=1, size=DISCRETE_OS_SIZE+[Action_SPACE])

for episode in range(EPISODES):
    if episode % SHOW_EVERY == 0:
        render = True
        print(episode)
    else:
        render  = False

    discrete_state = get_discrete_state(env.reset()[0])

    done = False
    i = 0
    while not done:
        if np.random.random() > EPSILON:
            action = np.argmax(q_table[discrete_state])
        else:
            action = np.random.choice([0, 1])
        new_state, reward, done, info, _ = env.step(action)
        new_discrete_state = get_discrete_state(new_state)
        # print(reward)
        # if render:
        env.render()

        if not done:
            max_future_q = np.max(q_table[new_discrete_state])
            current_q = q_table[discrete_state+(action,)]
            new_q = (1-LEARNING_RATE)*current_q + LEARNING_RATE*(reward + DISCOUNT*max_future_q)
            q_table[discrete_state+(action,)] = new_q

        # elif -GOAL_ANGLE <= new_state[2] <= GOAL_ANGLE:
        #     q_table[discrete_state+(action,)] = 1

        discrete_state = new_discrete_state
        i+=1
        print(f"{i}/200")

env.close()