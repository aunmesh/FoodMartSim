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
	for i in range(len(Allocations[0])):
		for j in range(len(Allocations)):
			#decrease farmer quantity by the allocated value
			# decrease buyer quantity by the allocated value
			market.farmers[i].qty = market.farmers[i].qty - Allocations[j][i]
			market.buyers[j].qty = market.buyers[j].qty - Allocations[j][i]
	print(" Allocation Finished")


#return a matrix of what is allocated to whom
# ouput is (farmer_pop x buyer_pop) matrix where each element is quantity traded between them
def RunMechanism(farmers, buyers):
	# computes allocation and payment
	farmer_pop = len(farmers)
	buyer_pop = len(buyers)
	farmers.sort(key=lambda x: x.bid, reverse=False)
	buyers.sort(key=lambda x: x.bid, reverse=True)

	allocation = [[0 for x in range(farmer_pop)] for y in range(buyer_pop)]
	# 2D matrix to store quantity traded between each farmer and buyer
	sell = [0 for x in range(farmer_pop)]
	buy = [0 for x in range(buyer_pop)]
	for i in range(farmer_pop): # duplicating the supply and demand
	  farmers[i].qty_traded=0
	  sell[i] = farmers[i].qty
	for i in range(buyer_pop):
	  buyers[i].qty_traded=0
	  buy[i] = buyers[i].qty
	s = 0
	b = 0
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
		if(farmers[s + ds].bid > buyers[b + db].bid):
		  break
		else:
		  allocation[s][b] = q
		  s += ds
		  b += db

	for i in range(farmer_pop):
		#print("Here " + str(buyer_pop))
		for j in range(buyer_pop):
			#CAUTION  FARMERS ARE IN THE COLUMN DIMENSION OF THE MATRIX  SEE allocation near LINE 79
			farmers[i].qty_traded += allocation[j][i]
			buyers[j].qty_traded += allocation[j][i]

	for i in range(farmer_pop):
		if(not farmers[i].qty_traded):
			farmers[i].brk_index = i
			#Farmer.brk_index = i
			break

	for i in range(buyer_pop):
		if(not buyers[i].qty_traded):
			buyers[i].brk_index = i
			#Buyer.brk_index = i
			break

	for i in range(farmers[0].brk_index):
		farmers[i].payment = farmers[farmer[i].brk_index].bid
		#farmers[i].payment = farmers[Farmer.brk_index].bid

	for i in range(buyers[0].brk_index):
		buyers[i].payment = buyers[buyers[i].brk_index].bid
		#buyers[i].payment = buyers[Buyer.brk_index].bid

	print(" Mechanism Finished")

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
