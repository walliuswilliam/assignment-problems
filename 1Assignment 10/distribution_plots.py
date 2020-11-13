import sys
sys.path.append('Assignment 7')
from monte_carlo_coin_flips import probability
from monte_carlo_coin_flips import monte_carlo_probability
import matplotlib.pyplot as plt

plt.style.use('bmh')
plt.plot([x for x in range(0, 9)], [probability(x, 8) for x in range(0, 9)], linewidth=2.5)
plt.plot([x for x in range(0, 9)], [monte_carlo_probability(x, 8) for x in range(0, 9)], linewidth=0.75)
plt.plot([x for x in range(0, 9)], [monte_carlo_probability(x, 8) for x in range(0, 9)], linewidth=0.75)
plt.plot([x for x in range(0, 9)], [monte_carlo_probability(x, 8) for x in range(0, 9)], linewidth=0.75)
plt.plot([x for x in range(0, 9)], [monte_carlo_probability(x, 8) for x in range(0, 9)], linewidth=0.75)
plt.plot([x for x in range(0, 9)], [monte_carlo_probability(x, 8) for x in range(0, 9)], linewidth=0.75)
plt.legend(['True','MC 1','MC 2','MC 3','MC 4','MC 5'])
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.title('True Distribution vs Monte Carlo Simulations for 4 Coin Flips')
plt.savefig('plot.png')
