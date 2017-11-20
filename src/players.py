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

	def __init__(self, Id, env):

		super(Farmer, self).__init__(Id, env)

		self.true_type = math.floor(max(1,random.gauss(60,40)))
		if(self.true_type < 0):
			print( "WARNING")
		self.bid = math.floor(max( self.true_type , random.gauss( self.true_type + 10,40)))
		if(self.bid < 0):
			print( "WARNING")

		self.qty = math.floor(random.uniform(1,20))
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

	def __init__(self, Id, env):
		#print(" New Buyer Constructed")
		super(Buyer, self).__init__(Id, env)

		self.env = env
		self.true_type=math.floor(max(1,random.gauss(100,40)))
		self.bid=math.floor(max(0,min(self.true_type,random.gauss(self.true_type-10,40))))
		self.qty = math.floor(random.uniform(1,20))
		self.action = self.env.process(self.run())
		self.payment = 0

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
