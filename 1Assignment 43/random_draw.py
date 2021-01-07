import random as rand

def cumulative_distribution(input_distribution):
  new_dist = []
  cumul_sum = 0
  for item in input_distribution:
    cumul_sum += item
    new_dist.append(cumul_sum)
  return new_dist

def random_draw(distribution):
  cumul_dist = cumulative_distribution(distribution)
  return cumul_dist

print(random_draw([0.05, 0.2, 0.15, 0.3, 0.1, 0.2]))