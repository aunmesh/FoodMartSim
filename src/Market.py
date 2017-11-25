import simpy
import numpy as np
from Mechanisms import *

#Allocate function is assumed to contain the Allocate function
#from Allocate import *
from players import *
from util import *
from csvLogger import logger

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
	def __init__(self,env,name, farmer_pop, buyer_pop,logger):

		self.env = env
		self.name = name
		self.farmer_pop=farmer_pop
		self.buyer_pop=buyer_pop
		#self.logger = Logger
		#Keeps the position where new ids are to be assigned from

		self.FARMER_IDX = 0
		self.BUYER_IDX = 0
		self.logger = logger

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

		#farmer and buyer break indices
		self.farmerBI = 0
		self.buyerBI = 0

		self.profit_per_trade = 0
		#profit of market from trade
		self.profit_trade = 0
		#profit of market by trying to balance mechanism
		self.profit_mech = 0

		self.total_trade_buyer = 0
		self.total_trade_farmer = 0


		#total quantity traded by marginal (break_index) farmer
		self.marg_farmer_qty_traded = 0
		#total quantity traded by marginal (break_index) buyer
		self.marg_buyer_qty_traded = 0

		#Qty of trade by market to farmers and buyers
		self.qty_from_farmers = [0 for x in range(farmer_pop)]
		self.qty_to_buyers = [0 for x in range(buyer_pop)]


	# TradingDay is the function which will be called by the simpy simulator. It should carry out all the activities the market does in a trading day.
	def Trading(self):

		while(True):
			yield self.env.timeout(0.1)

			#add or remove agents for the day
			UpdateAgents(self.farmers,self.buyers,self)\

			self.farmer_pop= len(self.farmers)
			self.buyer_pop= len(self.buyers)

			del self.qty_from_farmers
			del self.qty_to_buyers

			self.qty_from_farmers = [0 for x in range(self.farmer_pop)]
			self.qty_to_buyers = [0 for x in range(self.buyer_pop)]

			# Allocations done by Allocate function imported from Allocate.py script
			Allocations = runMechanism(self, self.logger)
			
			eff = calculate_efficiency(self, self.logger)

			#update bids for all agents (farmers and buyers)
			UpdateBids(self)

			#Perform the allocations by adjusting the values
			PerformAllocations(self,Allocations)
