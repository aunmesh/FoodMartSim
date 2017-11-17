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
		self.farmer_pop=farmer_pop
		self.buyer_pop=buyer_pop

		#List of all farmer and buyer objects.
		self.farmers = []
		self.buyers = []


		for temp_id in range(farmer_pop):
			#temp_bid = #Sample from some distribution
			self.farmers.append(Farmer(temp_id, self.env))

        for temp in range(buyer_pop):
            #temp_bid = #Sample from some distribution
            self.buyers.append(Buyer(temp_id, self.env))


	#method to add agent before trading starts for the day
	# used when new farmers or buyers are added into the sim
	def Add_agent(Occupation):
		if Occupation==0: #farmer
			self.farmers.append(Farmer(farmer_pop, self.env))
			seller_pop+=1
		elif Occupation==1:
			self.buyers.append(Buyer(buyer_pop,self.env))
			buyer_pop+=1




	#method to remove agent before trading starts
	# used for every agent which is to be removed
	def Remove_agent():




	# Method to perform Allocations in a single pass over the farmers and buyers list
	def PerformAllocations(farmers, buyers, Allocations):


	# TradingDay is the function which will be called by the simpy simulator. It should carry out all the activities the market does in a trading day.
	def Trading(self):

		while(True):
			#To control the frequency of trading
			#yield self.env.timeout(abs(np.random.normal(1,0.001)))

			#add or remove agents for the day
			UpdateAgents()

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
			UpdateBids()


			#Perform Allocations
			yield self.env.Process(PerformAllocations(self.farmers, self.buyers, Allocations))
