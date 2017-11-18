import simpy
import numpy as np
from Market import *
from player import *

env = simpy.Environment()

farmer_pop = 15#Numeric value
buyer_pop = 15#Numeric value

time_steps = 10000 #Simulation Span


market = Market(env, India, farmer_pop, buyer_pop)

'''Embedding the process in the Environment,
cascaded constructor calls ensure individual agent
processes are also embedded into the environment.
See Market.py and players.py
'''
env.process(market.Trading())

env.run(until=time_steps)
