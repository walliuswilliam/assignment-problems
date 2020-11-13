import math
import sys
sys.path.append('0Assignment 7')
from monte_carlo_coin_flips import probability
from monte_carlo_coin_flips import monte_carlo_probability

def ln(x):
  return math.log(x)

def kl_divergence(p, q):
  answer = 0
  for num in range(len(p)):
    if p[num] and q[num] != 0:
      answer += p[num]*ln(p[num]/q[num])
  return round(answer, 6)
p = [0.2, 0.5, 0, 0.3]
q = [0.1, 0.8, 0.1, 0]

if __name__ == "__main__":
  print("Testing KL Divergence...")
  assert kl_divergence(p,q) == -0.096372, 'failed'
  print('passed')


prob = [probability(num_heads, 8) for num_heads in range(9)]

monte100 = [monte_carlo_probability(num_heads, 8, 100) for num_heads in range(9)]
monte1000 = [monte_carlo_probability(num_heads, 8, 1000) for num_heads in range(9)]
monte10000 = [monte_carlo_probability(num_heads, 8, 10000) for num_heads in range(9)]
if __name__ == "__main__":
  print('Computing KL Divergence for MC Simulations...')
  print('100 samples --> KL Divergence = {}'.format(kl_divergence(monte100, prob)))
  print('1000 samples --> KL Divergence = {}'.format(kl_divergence(monte1000, prob)))
  print('10000 samples --> KL Divergence = {}'.format(kl_divergence(monte10000, prob)))

# As the number of samples increases, the KL divergence approaches 0 because as p, or monte carlo, gets closer to the real probability q, which when divided gets closer to 1, and ln(1) = 0.