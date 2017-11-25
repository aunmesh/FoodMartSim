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

'''
	def __init__(self, Id, env):
		self.id = Id
		self.loc_dist = math.floor(random.uniform(1,50))
'''

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

	FARMER_TYPE_MU = 60
	FARMER_TYPE_VAR = 10

	QUANTITY_LOWER_LIMIT = 1
	QUANTITY_UPPER_LIMIT = 20

	def __init__(self, Id, env):

		super(Farmer, self).__init__(Id, env)


		self.true_type = math.floor(max(1,random.gauss(Farmer.FARMER_TYPE_MU ,Farmer.FARMER_TYPE_VAR )))
		self.bid = self.true_type
		#self.bid = math.floor(max( self.true_type , random.gauss( self.true_type + 10, 40 )))
		self.qty = math.floor(random.uniform(Farmer.QUANTITY_LOWER_LIMIT,Farmer.QUANTITY_UPPER_LIMIT))
		self.env = env

		self.action = env.process(self.run())

		self.loc_dist = random.uniform(1,50)
		self.qty_traded = 0
		self.payment = 0

	def run(self):

		while True:
			try:
				yield self.env.timeout(1)
				#pass
			except simpy.Interrupt:
				#If  Killed then break out of loop
				if(self.dead):
					break
				# You have to update your Bid
				else:
					self.bid = (self.bid + self.true_type) / 2


			#Perform Book Keeping Functions and update reported type variable

	def get_bid(self):
		return self.bid


class Buyer(Agent):
	"""docstring for Buyer."""

	brk_index = 0 #static variable to store the break even index

	BUYER_TYPE_MU = 100
	BUYER_TYPE_VAR = 10

	QUANTITY_LOWER_LIMIT = 1
	QUANTITY_UPPER_LIMIT = 20


	def __init__(self, Id, env):
		#print(" New Buyer Constructed")
		super(Buyer, self).__init__(Id, env)

		self.env = env
		self.true_type=math.floor(max(1,random.gauss(Buyer.BUYER_TYPE_MU,Buyer.BUYER_TYPE_VAR)))
		self.bid=self.true_type
		#self.bid=math.floor(max(0,min(self.true_type,random.gauss(self.true_type-10,40))))
		self.qty = math.floor(random.uniform(Buyer.QUANTITY_LOWER_LIMIT, Buyer.QUANTITY_UPPER_LIMIT))
		self.action = self.env.process(self.run())
		self.qty_traded = 0

	#Define some action here
	def run(self):

		while True:
			try:
				yield self.env.timeout(1)
				#pass
			except simpy.Interrupt:
				#If  Killed then break out of loop
				if(self.dead):
					print("Buyer Killed")
					break
				# You have to update your Bid
				else:
					self.bid = (self.bid + self.true_type) / 2
