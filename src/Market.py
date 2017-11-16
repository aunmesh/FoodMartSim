import simpy 
import numpy as np

from players import *

class Market(object):
	'''	
	Constructor for Market.
	Args:
		env - Simpy env
		name - Name of Market. (Can be named on city or area etc.)
		players - list of all the agents. Each agent is an instance of Agent Class.

	'''

	def __init__(self,env,name, players):
		self.env = env
		self.name = name
		self.players = players


	# TradingDay is the function which will be called by the simpy simulator. It should carry out all the activities the market does in a trading day.
	def TradingDay(self):
		
