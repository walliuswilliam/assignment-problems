def factorial(n):
  if n <= 1:
    return 1
  else:
    return n*factorial(n-1)

def probability(num_heads, num_flips):
  outcomes = 2**num_flips
  prob = factorial(num_flips)/(factorial(num_flips-num_heads)*factorial(num_heads))
  return prob/outcomes

if __name__ == "__main__":
  print('asserting probability...')
  assert probability(5,8) == 0.21875, 'failed'
  print('passed')

from random import random
def random_flips():
  flip = round(random())
  return "HT"[flip]


def monte_carlo_probability(num_heads, num_flips, samples):
  flips = []
  one_heads_counter = 0
  for num in range(samples):
    flip = [random_flips() for i in range(num_flips)]
    flips.append(flip)
  for flip in flips:
    heads_in_flip = 0
    for outcome in flip:
      if outcome == "H":
        heads_in_flip += 1
    if heads_in_flip == num_heads:
      one_heads_counter += 1
  return one_heads_counter/samples

if __name__ == "__main__":
  print('testing monte carlo probability...')
  for num in range(5):
    print(monte_carlo_probability(5, 8, 1000))
