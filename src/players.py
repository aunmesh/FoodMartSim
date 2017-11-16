import simpy
import numpy as np
import random


class Agent(object):

	'''Constructor for the super class Agent
		Args:
			id: Name of Agent
			True_Type: True Type of Agent
			bid: Bid of Agent
			Local_Distance: Local Distance of Agent from their market(to be used in the mechanism)
	'''

	def __init__(self, id, bid,local_distance, env):
		self.id = id		
		self.bid = bid
		self.loc_dist = local_distance
		self.env = env

class Farmer(Agent):
    """docstring for Farmer."""

    def __init__(self, id, bid, local_distance, env):
        super(Farmer, self).__init__(self, id, bid, local_distance, env)
        self.true_type=max(0,random.gauss(60,40))
        self.qty=random.uniform(0,20)

class Buyer(Agent):
    """docstring for Buyer."""

    def __init__(self, id, bid, local_distance, env):
        super(Buyer, self).__init__(self, id, True_Type, bid, local_distance, env)
        self.true_type=max(0,random.gauss(100,40))
        self.qty=random.uniform(0,20)
