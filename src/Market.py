import simpy
import numpy as np

#Allocate function is assumed to contain the Allocate function
#from Allocate import *
from players import *
from util import *

class Market(object):
	'''
	Constructor for Market.
	Args:
		env - Simpy env
		name - Name of Market. (Can be named on city or area etc.)
		farmer_pop - The farmer population
		buyer_pop - The buyer population
	'''
	#def __init__(self,env,name, farmer_pop, buyer_pop, Logger):
	def __init__(self,env,name, farmer_pop, buyer_pop, logger):
		self.logger = logger
		self.env = env
		self.name = name
		self.farmer_pop=farmer_pop
		self.buyer_pop=buyer_pop
		#self.logger = Logger
		#Keeps the position where new ids are to be assigned from

		self.FARMER_IDX = 0
		self.BUYER_IDX = 0

		#List of all farmer and buyer objects.
		self.farmers = []
		self.buyers = []

		for temp_id in range(self.farmer_pop):
			#temp_bid = #Sample from some distribution
			self.farmers.append(Farmer(temp_id, self.env))

		#Updating Farmer ID which is available
		self.FARMER_IDX+=len(self.farmers)

		for temp_id in range(self.buyer_pop):
			self.buyers.append( Buyer(temp_id, self.env) )

		#Updating Buyer ID which is available
		self.BUYER_IDX+=len(self.buyers)


	# TradingDay is the function which will be called by the simpy simulator. It should carry out all the activities the market does in a trading day.
	def Trading(self):

		while(True):

			#add or remove agents for the day
			UpdateAgents(self.farmers,self.buyers,self)

			# Allocations done by Allocate function imported from Allocate.py script
			#Allocations = RunMechanism(self.farmers, self.buyers, self.logger, self)
			Allocations = RunMechanism(self, self.logger)

			#update bids for all agents (farmers and buyers)
			UpdateBids(self.farmers, self.buyers)

			#Perform the allocations by adjusting the values
			PerformAllocations(self,Allocations)
