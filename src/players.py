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

	def __init__(self, Id, bid,local_distance, env):
		self.id = Id		
		self.bid = bid
		self.loc_dist = local_distance
		self.env = env

	def run(self):
		pass



class Farmer(Agent):
	"""docstring for Farmer."""

	def __init__(self, Id, bid, local_distance, env):
		super(Farmer, self).__init__(self, Id, bid, local_distance, env)

		self.true_type=max(0,random.gauss(60,40))
		self.qty=random.uniform(0,20)


		self.action = self.env.process(self.run())

                self.rep_type = DUMMY_VAR
	

	def run(self):
		#Perform Book Keeping Functions and update reported type variable

	def get_reported_type(self):
		return self.rep_type




class Buyer(Agent):
	"""docstring for Buyer."""

	def __init__(self, Id, bid, local_distance, env):
		super(Buyer, self).__init__(self, Id, True_Type, bid, local_distance, env)

		self.true_type=max(0,random.gauss(100,40))
		self.qty=random.uniform(0,20)

		self.action = self.env.process(self.run())
		self.

	def run(self):
		#Perform Book Keeping Functions 

        def get_reported_type(self):
                return self.rep_type


