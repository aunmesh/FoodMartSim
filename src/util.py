from players import *
import numpy as np
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

	for temp in buyers:
		if temp.qty == 0: # buyer has nothing to buy
			Remove_agent(temp)
			buyers.remove(temp)

	flen2=len(farmers)
	blen2=len(buyers)

	Add_agent(market, [ flen1-flen2 , blen1-blen2 ])



#Method to add agent before trading starts for the day
#used when new farmers or buyers are added into the sim
# Nums is list of (no of farmers to be added, no of buyers to be added)
def Add_agent(market,Nums):
	temp_farmer = Nums[0]
	temp_buyer = Nums[1]

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

	for i in range(len(Allocations[0])):
		for j in range(len(Allocations)):
			#decrease farmer quantity by the allocated value
			# decrease buyer quantity by the allocated value
			market.farmers[i].qty = market.farmers[i].qty - Allocations[j][i]
			market.buyers[j].qty = market.buyers[j].qty - Allocations[j][i]

	print(" Allocation Finished")


#return a matrix of what is allocated to whom
# ouput is (farmer_pop x buyer_pop) matrix where each element is quantity traded between them
#def RunMechanism(farmers, buyers,logger,market):

def RunMechanism(market,logger):

	# computes allocation and payment

	farmer_pop = len(market.farmers)
	buyer_pop = len(market.buyers)

	market.farmers.sort(key=lambda x: x.bid, reverse=False)
	market.buyers.sort(key=lambda x: x.bid, reverse=True)

	allocation = [[0 for x in range(farmer_pop)] for y in range(buyer_pop)]
	# 2D matrix to store quantity traded between each farmer and buyer

	sell = [0 for x in range(farmer_pop)]
	buy = [0 for x in range(buyer_pop)]

	for i in range(farmer_pop): # duplicating the supply and demand
	  market.farmers[i].qty_traded=0
	  sell[i] = market.farmers[i].qty

	for i in range(buyer_pop):
	  market.buyers[i].qty_traded=0
	  buy[i] = market.buyers[i].qty

	s = 0
	b = 0

	NET_TRADE = 0
	while(s < farmer_pop - 1 and b < buyer_pop - 1):

		q = min(sell[s], buy[b])
		sell[s] -= q
		buy[b] -= q
		if(buy[b]):
		  ds = 1
		  db = 0
		elif(sell[s]):
		  ds = 0
		  db = 1
		else:
		  ds = 1
		  db = 1
		if(market.farmers[s + ds].bid > market.buyers[b + db].bid):
		  break
		else:
		  NET_TRADE+=q

		  allocation[b][s] = q
		  s += ds
		  b += db

	for i in range(farmer_pop):
		for j in range(buyer_pop):
			#CAUTION  FARMERS ARE IN THE COLUMN DIMENSION OF THE MATRIX  SEE allocation near LINE 79
			market.farmers[i].qty_traded += allocation[j][i]
			market.buyers[j].qty_traded += allocation[j][i]

	for i in range(farmer_pop):
		if(not market.farmers[i].qty_traded):
			Farmer.brk_index = i
			#Farmer.brk_index = i
			break

	for i in range(buyer_pop):
		if(not market.buyers[i].qty_traded):
			Buyer.brk_index = i
			#Buyer.brk_index = i
			break

	NET_PAYMENT = 0


	for i in range(Farmer.brk_index):
		market.farmers[i].payment = market.farmers[Farmer.brk_index].bid
		print(market.farmers[i].payment)
		NET_PAYMENT-=market.farmers[i].payment  * market.farmers[i].qty_traded


	#print("BRK_EVEN INDEX BUYER " + str(buyers[0].brk_index))

	for i in range(Buyer.brk_index):
		market.buyers[i].payment = market.buyers[Buyer.brk_index].bid
		print(market.buyers[i].payment)
		NET_PAYMENT+=market.buyers[i].payment * market.buyers[i].qty_traded
		#buyers[i].payment = buyers[Buyer.brk_index].bid

	print(" Ended")

	logger.log([NET_PAYMENT, NET_TRADE, farmer_pop, buyer_pop])

	Alloc = np.asarray(allocation)


	return allocation


#each agent updates bids according to last days sales
# if he hasnt sold his stuff then move bid closer to the true_type
# better to be less greedy and sell off stuff than to not sell
# this is because farmer doesnt know what dsic means.
# the farmer will eventually learn that his utility is more when his bid is close to true_type
'''
def UpdateBids(farmers,buyers):
	for temp in farmers:
		if temp.qty!=0:
			temp.bid=(temp.bid+temp.true_type) / 2
	for temp in buyers:
		if temp.qty!=0:
			temp.bid=(temp.bid+temp.true_type) / 2
'''

def UpdateBids(farmers,buyers):
	for temp in farmers:
		temp.action.interrupt()

	for temp in buyers:
		temp.action.interrupt()


#def CheckDSIC():
