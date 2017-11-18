import simpy
import numpy as np

#Allocate function is assumed to contain the Allocate function
from Allocate import *
from players import *

class Market(object):
	'''
	Constructor for Market.
	Args:
		env - Simpy env
		name - Name of Market. (Can be named on city or area etc.)
		farmer_pop - The farmer population
		buyer_pop - The buyer population
	'''
	def __init__(self,env,name, farmer_pop, buyer_pop):

		self.env = env
		self.name = name
		self.farmer_pop=farmer_pop
		self.buyer_pop=buyer_pop

		#Keeps the position where new ids are to be assigned from

		self.FARMER_IDX = 0
		self.BUYER_IDX = 0

		#List of all farmer and buyer objects.
		self.farmers = []
		self.buyers = []


		for temp_id in range(farmer_pop):
			#temp_bid = #Sample from some distribution
			self.farmers.append(Farmer(temp_id, self.env))

		#Updating Farmer ID which is available
		self.FARMER_IDX+=len(farmer_pop)

		for temp in range(buyer_pop):
            #temp_bid = #Sample from some distribution
            self.buyers.append(Buyer(temp_id, self.env))

		#Updating Buyer ID which is available
		self.BUYER_IDX+=len(buyer_pop)


	# TradingDay is the function which will be called by the simpy simulator. It should carry out all the activities the market does in a trading day.
	def Trading(self):

		while(True):
			#To control the frequency of trading
			#yield self.env.timeout(abs(np.random.normal(1,0.001)))

			#add or remove agents for the day
			UpdateAgents(farmers,buyers)

			'''
			Seller_bids = {'Farmer_ID' : 'bid'}

			for temp in self.farmers:
				Seller_bids[temp.getID()] = temp.get_bid()

			Buyer_bids = {'Buyer_ID' : 'bid'}

			for temp in self.buyers:
				Buyer_bids[temp.getID()] = tmep.get_bid()
			'''
			# Allocations done by Allocate function imported from Allocate.py script
			Allocations = Allocate(farmers,buyers)

			#update bids for all agents (farmers and buyers)
			UpdateBids(farmers,buyers)
			

			#Perform Allocations
			yield self.env.Process(PerformAllocations(self,Allocations))
