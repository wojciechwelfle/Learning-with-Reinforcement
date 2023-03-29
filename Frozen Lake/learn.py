from environment import *
from agent import *
import time


class Learning(Environment, Agent):
    def __init__(self, environment, agent):
        super().__init__()
        self.environment = environment
        self.agent = agent

    def learn_agent(self, repeat_loop):
        print("Learning...")
        for i in range(repeat_loop + 1):
            self.environment.set_to_initial_pos()
            while not self.environment.is_end_position():
                pos = self.environment.get_position()
                action = self.agent.get_action(pos[0], pos[1])
                new_pos = self.environment.step(action)
                reward = self.environment.get_reward()

                self.agent.update(pos[0], pos[1], action, reward, new_pos[0], new_pos[1],
                                  self.environment.is_end_position())
        self.agent.display_states()
        print('\n')

    def show_agent_with_best_actions(self):
        print("#######START#######\n")
        self.environment.set_to_initial_pos()
        self.environment.display_board()
        while not self.environment.is_end_position():
            time.sleep(1)
            pos = self.environment.get_position()
            action = self.agent.get_best_action(pos[0], pos[1])
            self.environment.step(action)
            self.environment.display_board()
        print("########END########\n")
