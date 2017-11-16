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
		players - list of all the agents. Each agent is an instance of Agent Class.

	'''
	
	def __init__(self,env,name, farmer_pop, buyer_pop):
		self.env = env
		self.name = name

		#List of all farmer and buyer objects.
		self.farmers = []
		self.buyers = []

		# List of true types for Famers and Buyers
		self.farmer_types = []
		self.buyer_types = []

		for temp in range(farmer_pop):

			temp_type = #Sample from some distribution
			temp_bid = #Sample from some distribution
			temp_local_dis = #Sample from some distribution

			self.farmers.append(temp, temp_type, temp_bid, temp_local_dis, self.env)

                for temp in range(buyer_pop):

                        temp_type = #Sample from some distribution
                        temp_bid = #Sample from some distribution
                        temp_local_dis = #Sample from some distribution

                        self.buyers.append(temp, temp_type, temp_bid, temp_local_dis, self.env)

			
			
		

	# TradingDay is the function which will be called by the simpy simulator. It should carry out all the activities the market does in a trading day.
	def TradingDay(self):

		while(True):
			#To control the frequency of trading
			yield self.env.timeout(abs(np.random.normal(1,0.001)))
		
			Seller_bids = {'Farmer_ID' : '[Reported_type, bid]'}
		
			for temp in self.farmers:
				Seller_bids[temp.getID()] = [temp.get_reported_type(), temp.submit_bid()]
		
			Buyer_bids = {'Buyer_ID' : '[Reported_type, bid]'}

			for temp in self.buyers:
				Buyer_bids[temp.getID()] = [temp.get_reported_type(), temp.submit_bid()]

			# Allocations done by Allocate function imported from Allocate.py script
			Allocations = Allocate(Seller_bids, Buyer_bids)
		
			#Perform Allocations
			yield self.env.Process(PerformAllocations(self.farmers, self.buyers, Allocations))


	# Method to perform Allocations in a single pass over the farmers and buyers list
	def PerformAllocations(farmers, buyers, Allocations):
		
