import simpy
import numpy as np
from Market import *
from players import *
from csvLogger import logger

logger = logger('ProfitvsNetTrade.log', ['Market_Profit','Net_Quantity_Traded','Farmer_pop','Buyer_pop'])

env = simpy.Environment()

farmer_pop = 15#Numeric value
buyer_pop = 15#Numeric value

time_steps = 10000 #Simulation Span


market = Market(env, 'India', farmer_pop, buyer_pop,logger)

'''Embedding the process in the Environment,
cascaded constructor calls ensure individual agent
processes are also embedded into the environment.
See Market.py and players.py
'''
env.process(market.Trading())

env.run(until=time_steps)
