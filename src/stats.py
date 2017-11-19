def calculate_efficiency(farmers, buyers):
  welfare = 0
  maxwelfare = 0
  farmer_pop = len(farmers)
  buyer_pop = len(buyers)
  for i in range(farmer_pop):
    welfare -= farmers[i].qty_traded * farmers[i].true_type
  for i in range(buyer_pop):
    welfare += buyers[i].qty_traded * buyers[i].true_type
  maxwelfare = welfare
  maxwelfare += (farmers[Farmer.brk_index].qty - farmers[Farmer.brk_index].qty_traded)
  maxwelfare += (buyers[Buyer.brk_index].qty - buyers[Buyer.brk_index].qty_traded)
  efficiency = welfare/maxwelfare
  return efficiency
