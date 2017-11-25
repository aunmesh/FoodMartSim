from players import *
'''Access the list farmers and buyers. Iterate through the list, send
agents(which have become useless) to be terminated. Also perform remove from the list.
We will need to dump their stats.

The total number of agents is kept same for each trading day.
We replenish the number of agents before allocation
'''
def UpdateAgents(farmers,buyers,market):
	flen1 = len(farmers)
	blen1= len(buyers)

	for temp in farmers: #farmer has nothing to sell
		if temp.qty == 0:
			Remove_agent(temp)
			farmers.remove(temp)

	flen2=len(farmers)
	blen2=len(buyers)

	for temp in buyers:
		if temp.qty == 0: # buyer has nothing to buy
			Remove_agent(temp)
			buyers.remove(temp)

	Add_agent(market, [ flen1-flen2 , blen1-blen2 ])



#Method to add agent before trading starts for the day
#used when new farmers or buyers are added into the sim
# Nums is list of (no of farmers to be added, no of buyers to be added)
def Add_agent(market,Nums):
	temp_farmer = Nums[0]
	temp_buyer = Nums[0]

	for temp in range(temp_farmer):
		market.farmers.append(Farmer(market.FARMER_IDX + temp , market.env))

	#Updating available ID
	market.FARMER_IDX+=temp_farmer

	for temp in range(temp_buyer):
		market.buyers.append(Buyer(market.BUYER_IDX + temp , market.env))

	#Updating available ID
	market.BUYER_IDX+=temp_buyer



#method to remove agent before trading starts
# used for every agent which is to be removed
def Remove_agent(agent):
	agent.action.interrupt()
	agent.dead = True

# Method to perform Allocations in a single pass over the farmers and buyers list
#Check whether the allocation is peformed at the correct seller/buyer id

def PerformAllocations(market,Allocations):
	for col in range(len(Allocations[0])):
		for row in range(len(Allocations)):
			#decrease farmer quantity by the allocated value
			# decrease buyer quantity by the allocated value
			market.farmers[row].qty = market.farmers[row].qty - Allocations[row][col]
			market.buyers[col].qty = market.buyers[col].qty - Allocations[row][col]
	print(" Allocation Finished")



#each agent updates bids according to last days sales
# if he hasnt sold his stuff then move bid closer to the true_type
# better to be less greedy and sell off stuff than to not sell
# this is because farmer doesnt know what dsic means.
# the farmer will eventually learn that his utility is more when his bid is close to true_type

def UpdateBids(self):
	for temp in self.farmers:
		temp.action.interrupt()

	for temp in self.buyers:
		temp.action.interrupt()




def calculate_efficiency(market, logger):
  welfare = 0
  maxwelfare = 0
  farmer_pop = len(market.farmers)
  buyer_pop = len(market.buyers)
  for i in range(farmer_pop):
    welfare -= (market.farmers[i].qty_traded - market.qty_from_farmers[i]) * market.farmers[i].true_type
  for i in range(buyer_pop):
    welfare += (market.buyers[i].qty_traded - market.qty_to_buyers[i])* market.buyers[i].true_type
  maxwelfare = welfare
  maxwelfare += market.marg_farmer_qty_traded* market.farmers[market.farmerBI].true_type
  maxwelfare += market.marg_buyer_qty_traded* market.buyers[market.buyerBI].true_type
  #print("Welfare {0:d} Max welfare {1:f}".format(welfare, maxwelfare), end='\n')
  efficiency = welfare/maxwelfare
  logger.log([efficiency])
  return efficiency



'''
def UpdateBids(farmers,buyers):
	for temp in farmers:
		if temp.qty!=0:
			temp.bid=(temp.bid+temp.true_type) / 2
	for temp in buyers:
		if temp.qty!=0:
			temp.bid=(temp.bid+temp.true_type) / 2
'''


#def CheckDSIC():
