# CYSE 689 Final Project
# Chris Limson
# climson@gmu.edu
# 2024/05/07

import gymnasium as gym

class HIDS(gym.Env):

  states = [
    "Benign Request",
    "SQL Injection Code",
    "PHP Script Request",
    "Hexadecimal-Encoded String",
    "Other Suspicious Request"
  ]

  actions = [
    "Alert",
    "Allow"
  ]

  def __init__(self):
    self.observation_space = gym.spaces.Discrete(len(self.states))
    self.action_space      = gym.spaces.Discrete(len(self.actions))

  def reset(self, seed=None, options=None):
    self.state = 0
    info = {}
    return self.state, info

  def step(self, action):
    # Reward function
    if self.state == self.states.index("Benign Request"):
      if action == self.actions.index("Allow"):
        reward = 1
      else:
        reward = 0

    if self.state == self.states.index("SQL Injection Code"):
      if action == self.actions.index("Alert"):
        reward = 1
      else:
        reward = -1

    if self.state == self.states.index("PHP Script Request"):
      if action == self.actions.index("Alert"):
        reward = 1
      else:
        reward = -1

    if self.state == self.states.index("Hexadecimal-Encoded String"):
      if action == self.actions.index("Alert"):
        reward = 1
      else:
        reward = -1

    if self.state == self.states.index("Other Suspicious Request"):
      if action == self.actions.index("Alert"):
        reward = 1
      else:
        reward = -1

    # Randomly pick the next state
    self.state = self.observation_space.sample()

    # Allow simulation to run endlessly, like the webserver
    terminate = False
    truncate = False

    info = {}
    return self.state, reward, terminate, truncate, info
