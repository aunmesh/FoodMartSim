import simpy
import numpy as np


class Agent(object):

	'''Constructor for the super class Agent
		Args:
			id: Name of Agent
			Occupation: Farmers or Consumers
			True_Type: True Type of Agent
			Reported_Type: Reported type of Agent
			Local_Distance: Local Distance of Agent from their market(to be used in the mechanism)
	'''			

	def __init__(self, id, Occupation, True_Type, Reported_Type,local_distance, env):
		self.id = id
		self.Occupation = Occupation
		self.true_type = True_Type  
		self.rep_type = Reported_Type
		self.loc_dist = local_distance
		self.env = env
