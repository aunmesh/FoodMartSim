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

	Add_agent(flen1-flen2,blen1-blen2)



#Method to add agent before trading starts for the day
#used when new farmers or buyers are added into the sim
# Nums is list of (no of farmers to be added, no of buyers to be added)
def Add_agent(Nums):
	temp_farmer = Nums[0]
	temp_buyer = Nums[0]

	for temp in range(temp_farmer):
		self.farmers.append(Farmer(FARMER_IDX + temp , self.env))

	#Updating available ID
	self.FARMER_IDX+=temp_farmer

	for temp in range(temp_buyer):
		self.buyers.append(Buyer(BUYER_IDX + temp , self.env))

	#Updating available ID
	self.BUYER_IDX+=temp_buyer



#method to remove agent before trading starts
# used for every agent which is to be removed
def Remove_agent(agent):
	agent.action.interrupt()
	agent.dead = True

# Method to perform Allocations in a single pass over the farmers and buyers list
def PerformAllocations(market,Allocations):
	for i in range(seller_pop):
		for j in range(buyer_pop):
			#decrease farmer quantity by the allocated value
			# decrease buyer quantity by the allocated value
			farmers[i].qty = farmers[i].qty - allocation[i][j]
			buyers[j].qty = buyers[j].qty - allocation[i][j]




#return a matrix of what is allocated to whom
<<<<<<< HEAD
# ouput is (farmer_pop x buyer_pop) matrix where each element is quantity traded between them
def RunMechanism():
=======
def RunMechanism(farmers, buyers):
>>>>>>> d2e196dbc1c6dff20263dd17f81571f79da2141d
  # computes allocation and payment
  seller_pop = len(farmers)
  buyer_pop = len(buyers)
  farmers.sort(key=lambda x: x.bid, reverse=False)
  buyers.sort(key=lambda x: x.bid, reverse=True)
<<<<<<< HEAD

  allocation = [[0 for x in range(seller_pop)] for y in range(buyer_pop)] # 2D matrix to store quantity traded between each farmer and buyer
  for i in range(seller_pop): # duplicating the supply and demand
      farmers[i].qty_traded=0
=======
>>>>>>> d2e196dbc1c6dff20263dd17f81571f79da2141d
      sell[i] = farmers[i].qty
  for i in range(buyer_pop):
	  buyers[i].qty_traded=0
      buy[i] = buyers[i].qty
  s = 0
  b = 0
  while(s < seller_pop - 1 and b < buyer_pop - 1):
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
  for i in range(seller_pop):
      for j in range(buyer_pop):
          farmers[i].qty_traded += allocation[i][j]
          buyers[j].qty_traded += allocation[i][j]

  for i in range(seller_pop):
      if(not farmers[i].qty_traded):
          Farmer.brk_index = i
          break

  for i in range(buyer_pop):
      if(not buyers[i].qty_traded):
          Buyer.brk_index = i
          break

  for i in range(Farmer.brk_index):
      farmers[i].payment = farmers[Farmer.brk_index].bid

  for i in range(Buyer.brk_index):
      buyers[i].payment = buyers[Buyer.brk_index].bid
  return allocation


#each agent updates bids according to last days sales
def UpdateBids():


def CheckDSIC():
