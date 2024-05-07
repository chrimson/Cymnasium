# CYSE 689 Final Project
# Chris Limson
# climson@gmu.edu
# 2024/05/07

import gymnasium as gym
import cymnasium

env = gym.make('cymnasium/HIDS-v0')
observation, info = env.reset()

for i in range(10):
  print("State:  %s" % env.unwrapped.states[observation])

  action = env.action_space.sample()
  print("Action: %s" % env.unwrapped.actions[action])

  observation, reward, terminate, truncate, info = env.step(action)
  print("Reward: %d\n" % reward)

env.close()
