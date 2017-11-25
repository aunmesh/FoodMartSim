#Holds Implementations of Mechanisms
from players import *
import random
import math
from util import *

def runMechanism(market, logger):
    # computes allocation and payment
    farmer_pop = len(market.farmers)
    buyer_pop = len(market.buyers)
    #market.farmers.sort(key=lambda x: x.bid, reverse=False)
    #market.buyers.sort(key=lambda x: x.bid, reverse=True)

    allocation = [[0 for x in range(buyer_pop)] for y in range(farmer_pop)]
    sell = [0 for x in range(farmer_pop)]
    buy = [0 for x in range(buyer_pop)]
    ##  totaltrade = 0

    for i in range(farmer_pop):
      sell[i] = market.farmers[i].qty

    for i in range(buyer_pop):
      buy[i] = market.buyers[i].qty

    s = 0
    b = 0

    while(s < farmer_pop and b < buyer_pop and market.farmers[s].bid <= market.buyers[b].bid):
      q = min(sell[s], buy[b])
      sell[s] -= q
      buy[b] -= q
      allocation[s][b] = q
    ##      totaltrade += q
      if(not buy[b]):
          b += 1
      if(not sell[s]):
          s += 1

    for i in range(farmer_pop):
      for j in range(buyer_pop):
          market.farmers[i].qty_traded += allocation[i][j]
          market.buyers[j].qty_traded += allocation[i][j]

    for i in range(farmer_pop):
      if(market.farmers[i].qty_traded):
          market.farmerBI = i
      else:
          break

    for j in range(buyer_pop):
      if(market.buyers[j].qty_traded):
          market.buyerBI = j
      else:
          break

    market.marg_farmer_qty_traded = market.farmers[market.farmerBI].qty_traded - 1
    market.marg_buyer_qty_traded = market.buyers[market.buyerBI].qty_traded - 1
    market.farmers[market.farmerBI].qty_traded = 0
    market.buyers[market.buyerBI].qty_traded = 0

    allocation[market.farmerBI][market.buyerBI] = 0

    for i in range(market.farmer_pop):
      #market.farmers[i].qty_traded -= allocation[i][market.buyerBI]
      market.qty_from_farmers[i] = allocation[i][market.buyerBI]
      allocation[i][market.buyerBI] = 0

    #print('DEBUG')
    #print(buyer_pop)

    for j in range(buyer_pop):
      #market.buyers[j].qty_traded -= allocation[market.farmerBI][j]
      market.qty_to_buyers[j]
      allocation[market.farmerBI][j]
      market.qty_to_buyers[j] = allocation[market.farmerBI][j]
      allocation[market.farmerBI][j] = 0

    for i in range(farmer_pop):
      market.farmers[i].payment = market.farmers[i].qty_traded * market.farmers[market.farmerBI].bid
      market.total_trade_farmer += market.farmers[i].qty_traded

    for j in range(buyer_pop):
      market.buyers[j].payment = market.buyers[j].qty_traded * market.buyers[market.buyerBI].bid
      market.total_trade_buyer += market.buyers[j].qty_traded

    if(market.total_trade_farmer > market.total_trade_buyer):
      market.profit_mech = (market.total_trade_buyer - market.total_trade_farmer)* market.farmers[market.farmerBI].bid

    else:
      market.profit_mech = (market.total_trade_buyer - market.total_trade_farmer)* market.buyers[market.buyerBI].bid

    market.profit_per_trade = market.buyers[market.buyerBI].bid - market.farmers[market.farmerBI].bid
    market.profit_trade = min(market.total_trade_farmer, market.total_trade_buyer)*market.profit_per_trade

    if(not market.profit_trade):
        market.profit_per_trade = 0

    #logger.log([ market.profit_per_trade , Buyer.BUYER_TYPE_MU - Farmer.FARMER_TYPE_MU ])

    #print('\n')
    #print("Market profit per trade: {2:d}, Total market trade profit: {0:d}, Misc profit: {1:d}".format(market.profit_trade, market.profit_mech, market.profit_per_trade))

    #print('\n')
    #print("Quantity of goods in hand of market: {0:d}".format(market.total_trade_farmer - market.total_trade_buyer))

    #print('\n')

    print("Mechanism Finished")
    return allocation



#return a matrix of what is allocated to whom
# ouput is (farmer_pop x buyer_pop) matrix where each element is quantity traded between them
'''
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
'''


'''
def RunMechanism2(market, logger):
	farmer_pop = len(market.farmers)
	buyer_pop = len(market.buyers)
	market.farmers.sort(key=lambda x: x.bid, reverse=False)
	market.buyers.sort(key=lambda x: x.bid, reverse=True)
	allocation = [[0 for x in range(buyer_pop)] for y in range(farmer_pop)]
	sell = [0 for x in range(farmer_pop)]
	buy = [0 for x in range(buyer_pop)]
	totaltrade = 0
	for i in range(farmer_pop):
		sell[i] = market.farmers[i].qty
	for i in range(buyer_pop):
		buy[i] = market.buyers[i].qty
	s = 0
	b = 0
	while(s < farmer_pop and b < buyer_pop and market.farmers[s].bid <= market.buyers[b].bid):
		q = min(sell[s], buy[b])
		sell[s] -= q
		buy[b] -= q
		allocation[s][b] = q
		totaltrade += q
		if(not buy[b]):
		  b += 1
		if(not sell[s]):
		  s += 1

	for i in range(farmer_pop):
		for j in range(buyer_pop):
			market.farmers[i].qty_traded += allocation[i][j]
			market.buyers[j].qty_traded += allocation[i][j]

	for i in range(farmer_pop):
		if(market.farmers[i].qty_traded):
			Farmer.brk_index = i

	for i in range(buyer_pop):
		if(market.buyers[i].qty_traded):
			Buyer.brk_index = i

	market.farmers[Farmer.brk_index].qty_traded = 0
	market.buyers[Buyer.brk_index].qty_traded = 0

	allocation[Farmer.brk_index][Buyer.brk_index] = 0

	for i in range(farmer_pop):
		marketF[i] = allocation[i][Buyer.brk_index]
		allocation[i][Buyer.brk_index] = 0

	for j in range(buyer_pop):
		marketC[j] = allocation[Farmer.brk_index][j]
		allocation[Farmer.brk_index][j] = 0

	for i in range(Farmer.brk_index):
		market.farmers[i].payment = market.farmers[Farmer.brk_index].bid

	for j in range(Buyer.brk_index):
		market.buyers[j].payment = market.buyers[Buyer.brk_index].bid

	marketprofit = totaltrade*(market.buyers[Buyer.brk_index].bid - market.farmers[Farmer.brk_index].bid)

	logger.log([totaltrade, marketprofit])

	#print(end="\n)
	#print(marketprofit, end=' ')
	#print(end='\n')
	return allocation
'''
