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

	def __init__(self, Id, local_distance, env):
		self.id = Id
		self.loc_dist = random.uniform(1,50)
		self.qty_traded = 0
		self.payment = 0
		self.env = env
		self.dead = False

	def run(self):
		pass



class Farmer(Agent):
	"""docstring for Farmer."""

	brk_index = 0 #static variable to store the break even index
	
	def __init__(self, Id, env):
		super(Farmer, self).__init__(self, Id, bid, local_distance, env)

		self.true_type = max(0,random.gauss(60,40))
		self.bid = max(true_type,random.gauss(true_type+10,40))
		self.qty = random.uniform(0,20)
		self.action = self.env.process(self.run())



	def run(self):
		#Perform Book Keeping Functions and update reported type variable

	def get_bid(self):
		return self.bid




class Buyer(Agent):
	"""docstring for Buyer."""
	
	brk_index = 0 #static variable to store the break even index
	
	def __init__(self, Id, env):
		super(Buyer, self).__init__(self, Id, bid, local_distance, env)

		self.true_type=max(0,random.gauss(100,40))
		self.bid=max(0,min(true_type,random.gauss(true_type-10,40)))
		self.qty=random.uniform(0,20)
		self.action = self.env.process(self.run())


	def run(self):
		#Perform Book Keeping Functions

    	def get_bid(self):
            return self.bid
