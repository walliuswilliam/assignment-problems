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
  rand_num = rand.random()
  for num in range(len(cumul_dist)):
    if cumul_dist[num] > rand_num:
      return num


average_draw = [0, 0]
for num in range(1000):
  draw_index = random_draw([0.5, 0.5])
  average_draw[draw_index] += 1
print('draw for [0.5, 0.5]:', average_draw)

average_draw = [0, 0, 0]
for num in range(1000):
  draw_index = random_draw([0.25, 0.25, 0.5])
  average_draw[draw_index] += 1
print('draw for [0.25, 0.25, 0.5]:', average_draw)

average_draw = [0, 0, 0, 0, 0, 0]
for num in range(1000):
  draw_index = random_draw([0.05, 0.2, 0.15, 0.3, 0.1, 0.2])
  average_draw[draw_index] += 1
print('draw for [0.05, 0.2, 0.15, 0.3, 0.1, 0.2]:', average_draw)