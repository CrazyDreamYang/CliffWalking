import pygame
import sys
import numpy as np
import  gym
import matplotlib.pyplot as plt

STATES_COLORS = {
        0: (0, 0, 255),
        1: (255, 255, 0),
        2: (255, 255, 255),
        3: (255, 69, 0),
        4: (255, 20, 147),
    }
STATES_SPACE = [key for key in STATES_COLORS]
    # 可行位置 蓝色
    # 悬崖 橙黄色
    # 起点终点  白色
    # 智能体  红色
    # 道路 紫色
#STATES_LABELS = ["Map", "Cliff", "StartOrEnd", "Agent", "Route"]
# 重新渲染地图
class Map:
    def __init__(self, width: int, height: int, statesSpace: list):
        self.width = width
        self.height = height
        self.statesSpace = statesSpace
        self.grid = np.zeros((self.height, self.width), dtype=np.uint8)

    def setMap(self, cliff: list, start: int, end: int):
        for s in cliff:
            s = self.__from_id_width(s)
            self.grid[s[0]][s[1]] = 1

        start = self.__from_id_width(start)
        self.grid[start[0]][start[1]] = 2

        end = self.__from_id_width(end)
        self.grid[end[0]][end[1]] = 2

    def render(self, agnetPostion: int):

        Postion = self.__from_id_width(agnetPostion)
        rednerGrid  = np.copy(self.grid)
        rednerGrid[Postion[0]][Postion[1]] = 3

        canvas = np.zeros(rednerGrid.shape + (3,), dtype=np.uint8)
        for state in self.statesSpace:
            canvas[rednerGrid == state] = STATES_COLORS[state]

        return canvas

    def __from_id_width(self, id, width=12):
        return (id % width, id // width)

# 定义智能体
class QlearningAgent:
    def __init__(self, env, gamma=0.9, learning_rate=0.1, epsilon=0.1):
        self.gamma = gamma
        self.learing_rate = learning_rate
        self.epsilon = epsilon
        self.action_n = env.action_space.n
        self.q = np.zeros((env.observation_space.n, env.action_space.n))  # 初始化Q表

    # 根据状态选择动作
    def decide(self, state):
        if np.random.uniform() > self.epsilon:
            action = self.q[state].argmax()
        else:
            action = np.random.randint(self.action_n)
        return action

    # 更新Q表
    def learn(self, state, action, reward, next_state, done):
        u = reward + self.gamma * self.q[next_state].max() * (1. - done)
        td_error = u - self.q[state, action]
        self.q[state, action] += self.learing_rate * td_error

# 无渲染训练
def PlayQLearningNoRender(env, agent, render=False, train=False):
    # print('---------------------下一个回合开始-------------------------')

    episode_reward = 0  # 回合总奖励
    observation = env.reset()  # 开始回合

    # print(len(observation))
    while True:

        if render:
            env.render()
            #map.render(observation)
        action = agent.decide(observation)  # 从智能体中拿到动作
        next_observation, reward, done, _ = env.step(action)  # 执行动作，得到奖励，与下一个时刻的状态

        episode_reward += reward  # 计算一个回合的奖励
        if train:  # 是否训练策略/价值网络
            agent.learn(observation, action, reward, next_observation, done)
        if done:
            break
        observation = next_observation

    return episode_reward

# 渲染并显示训练结果
def PlayQLearningRender(env, agent, cliff_map, episodes, train=False):
    pygame.init()
    display = pygame.display.set_mode((600, 200))
    clock = pygame.time.Clock()

    episode_rewards = []  # 回合总奖励
    observation = env.reset()  # 开始回合
    done = False
    running = True
    #color = (255, 0, 0)
    # print(len(observation))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()

        for i in range(episodes):
            print(i)
            observation = env.reset()
            episode_reward = 0
            while not done:

                grid = cliff_map.render(observation)
                surf = pygame.surfarray.make_surface(grid)
                surf = pygame.transform.scale(surf, (600, 200))
                display.blit(surf, (0, 0))
                #pygame.draw.rect(display, color, pygame.Rect(x, y, 50, 50))
                pygame.display.flip()
                clock.tick(5)
                pygame.time.delay(60)

                action = agent.decide(observation)  # 从智能体中拿到动作
                next_observation, reward, done, _ = env.step(action)  # 执行动作，得到奖励，与下一个时刻的状态
                episode_reward += reward  # 计算一个回合的奖励
                if train:  # 是否训练策略/价值网络
                    agent.learn(observation, action, reward, next_observation, done)

                observation = next_observation

            done = False
            episode_rewards.append(episode_reward)
        running = False
    print("end")
    sys.exit()
    env.close()
    return episode_rewards

if __name__ == '__main__':
    map = Map(4, 12, STATES_SPACE)
    cliffHoles = [37, 38, 39, 40, 41, 42, 43, 44, 45, 46]
    map.setMap(cliffHoles, 36, 47)
    env = gym.make("CliffWalking-v0")
    agent = QlearningAgent(env)
    episode = 500
    episode_rewards = []
    # episode_rewards = PlayWithQLearning(env, agent, map, episode, True)
    for i in range(episode):
        episode_reward = PlayQLearningNoRender(env, agent, False, True)
        episode_rewards.append(episode_reward)
    fig = plt.figure(1)
    plt.plot(episode_rewards)
    #plt.show()

    PlayQLearningRender(env, agent, map, 20, False)

    q_map = get_q_map(map.grid, agent.q)
    v_map = get_v_map(map.grid, agent.q)
    fig = plt.figure(2)
    ax1 = plt.subplot(2, 1, 1)

    plt.imshow(vis_q_map(q_map))
    cmap_colors = convert2matplotlib_cmap(colors=ACTION_COLORS)
    patches = get_patches(cmap_colors, labels=ACTION_LABELS)
    plt.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.title('Q_MAP')

    ax1 = plt.subplot(2, 1, 2)
    v_image = plt.imshow(v_map, cmap='viridis')
    plt.colorbar(v_image, fraction=0.046, pad=0.04)
    plt.title('V_MAP')

    plt.show()



