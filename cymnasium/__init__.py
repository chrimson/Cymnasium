# CYSE 689 Final Project
# Chris Limson
# climson@gmu.edu
# 2024/05/07

from gymnasium.envs.registration import register

register(
    id="cymnasium/HIDS-v0",
    entry_point="cymnasium.envs:HIDS",
)
