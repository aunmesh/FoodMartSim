import simpy
import numpy as np
import random
import math

class Agent(object):

	'''Constructor for the super class Agent
		Args:
			id: Name of Agent
			True_Type: True Type of Agent
			bid: Bid of Agent
			Local_Distance: Local Distance of Agent from their market(to be used in the mechanism)
	'''
	def __init__(self, Id, env):
		self.id = Id
		self.env = env
		self.dead = False


	def __init__(self, Id, env):
		self.id = Id
		self.loc_dist = math.floor(random.uniform(1,50))

'''
	def __init__(self, Id, local_distance, env):
		self.id = Id
		self.env = env
		self.loc_dist = random.uniform(1,50)

		self.qty_traded = 0
		self.payment = 0

		self.dead = False
'''

class Farmer(Agent):
	"""docstring for Farmer."""

	brk_index = 0 #static variable to store the break even index

	def __init__(self, Id, env):

		super(Farmer, self).__init__(self, Id, env)

		self.true_type = math.floor(max(1,random.gauss(60,40)))
		self.bid = math.floor(max(true_type,random.gauss(true_type+10,40)))
		self.qty = math.floor(random.uniform(1,20))

		self.action = self.env.process(self.run())

		self.loc_dist = random.uniform(1,50)
		self.qty_traded = 0
		self.payment = 0

	#
	def run(self):
		pass
		#Perform Book Keeping Functions and update reported type variable

	def get_bid(self):
		return self.bid

class Buyer(Agent):
	"""docstring for Buyer."""

	brk_index = 0 #static variable to store the break even index

	def __init__(self, Id, env):
		super(Buyer, self).__init__(self, Id, env)

		self.true_type=math.floor(max(1,random.gauss(100,40)))
		self.bid=math.floor(max(0,min(true_type,random.gauss(true_type-10,40))))
		self.qty = math.floor(random.uniform(1,20))
		self.action = self.env.process(self.run())

	#Define some action here
	def run(self):
		pass#Perform Book Keeping Functions
