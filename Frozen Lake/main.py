import threading
from learn import *

import tkinter as tk
import gui

env = Environment()
agent = Agent()
repeat = 1_500_000

learn = Learning(env, agent)
learn.learn_agent(repeat)

learn_thread = threading.Thread(target=learn.show_agent_with_best_actions)
learn_thread.start()


if __name__ == '__main__':
    root = tk.Tk()
    canvas = gui.EnvironmentGUI(root, env)
    canvas.pack()
    root.mainloop()
