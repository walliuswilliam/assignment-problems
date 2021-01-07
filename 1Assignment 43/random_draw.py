import random as rand

def random_draw(distribution):
  cumul_dist = []
  for item in range(len(distribution)):
    if item = 0:
      cumul_dist.append(distribution[item])  
    else:
      cumul_dist.append(distribution[item]+distribution[item-1])
  return cumul_dist

