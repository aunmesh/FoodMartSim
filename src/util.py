'''Access the list farmers and buyers. Iterate through the list, send
agents(which have become useless) to be terminated. Also perform remove from the list.
We will need to dump their stats.
'''
def UpdateAgents():





#method to remove agent before trading starts
# used for every agent which is to be removed
def Remove_agent(agent):
	agent.action.interrupt()
	agent.dead = True


#return a matrix of what is allocated to whom
def RunMechanism():
  # computes allocation and payment
  # sellers should be sorted in ascending order of bids and buyers in descending order
  farmers.sort(key=lambda x: x.bid, reverse=False)
  buyers.sort(key=lambda x: x.bid, reverse=True)

  allocation = [[0 for x in range(seller_pop)] for y in range(buyer_pop)] # 2D matrix to store quantity traded between each farmer and buyer
  for i in range(seller_pop): # duplicating the supply and demand
      sell[i] = farmers[i].qty
  for i in range(buyer_pop):
      buy[i] = buyers[i].qty
  s = 0
  b = 0
  while(s < seller_pop - 1 and b < buyer_pop - 1):  # note that the last seller and last buyer never trades in this mechanism
      q = min(sell[s], buy[b])  # 'q' denotes the quantity to be traded between seller 's' and buyer 'b'
      sell[s] -= q
      buy[b] -= q
      if(not buy[b]): # decides whether to increment seller index or buyer index or both depending upon if any supply or demand is left to trade
          ds = 1
          db = 0
      elif(not sell[s]):
          ds = 0
          db = 1
      else:
          ds = 1
          db = 1
      if(farmers[s + ds].bid > buyers[b + db].bid): # check if 's' and 'b' are break indices
          break
      else:
          allocation[s][b] = q
          s += ds
          b += db

  for i in range(seller_pop): # assigns total trade done for each farmer and buyer
      for j in range(buyer_pop):
          farmers[i].qty_traded += allocation[i][j]
          buyers[j].qty_traded += allocation[i][j]

  for i in range(seller_pop): # finds break index
      if(not farmers[i].qty_traded):
          Farmer.brk_index = i
          break

  for i in range(buyer_pop):
      if(not buyers[i].qty_traded):
          Buyer.brk_index = i
          break

  # computes payment
  for i in range(Farmer.brk_index):
      farmers[i].payment = farmers[Farmer.brk_index].bid

  for i in range(Buyer.brk_index):
      buyers[i].payment = buyers[Buyer.brk_index].bid

  # sorting them back to initial positions to avoid inconsistency
  farmers.sort(key=lambda x: x.id, reverse=False)
  buyers.sort(key=lambda x: x.id, reverse=False)

  return allocation


#each agent updates bids according to last days sales
def UpdateBids():


def CheckDSIC():
