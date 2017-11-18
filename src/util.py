def UpdateAgents():


#return a matrix of what is allocated to whom
def RunMechanism(farmers, buyers):
  # computes allocation and payment
  seller_pop = len(farmers)
  buyer_pop = len(buyers)
  farmers.sort(key=lambda x: x.bid, reverse=False)
  buyers.sort(key=lambda x: x.bid, reverse=True)
  allocation = [[0 for x in range(seller_pop)] for y in range(buyer_pop)]
  sell = [0 for x in range(seller_pop)]
  buy = [0 for x in range(buyer_pop)]
  for i in range(seller_pop):
      sell[i] = farmers[i].qty
  for i in range(buyer_pop):
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
