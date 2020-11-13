import matplotlib.pyplot as plt

coin_1 = ['TTH', 'HHT', 'HTH', 'TTH', 'HTH',
          'TTH', 'TTH', 'TTH', 'THT', 'TTH',
          'HTH', 'HTH', 'TTT', 'HTH', 'HTH',
          'TTH', 'HTH', 'TTT', 'TTT', 'TTT',
          'HTT', 'THT', 'HHT', 'HTH', 'TTH']
coin_2 = ['HTH', 'HTH', 'HTT', 'THH', 'HHH',
          'THH', 'HHH', 'HHH', 'HTT', 'TTH',
          'TTH', 'HHT', 'TTH', 'HTH', 'HHT',
          'THT', 'THH', 'THT', 'TTH', 'TTT',
          'HHT', 'THH', 'THT', 'THT', 'TTT']
coin_3 = ['HHH', 'THT', 'HHT', 'HHT', 'HTH',
          'HHT', 'HHT', 'HHH', 'TTT', 'THH',
          'HHH', 'HHH', 'TTH', 'THH', 'THH',
          'TTH', 'HTT', 'TTH', 'HTT', 'HHT',
          'TTH', 'HTH', 'THT', 'THT', 'HTH']

def counter(flip_list):
  counter_list = [0, 0, 0, 0]
  for flip_sequence in flip_list:
    heads_counter = 0
    for flip_result in flip_sequence:
      if flip_result == 'H':
        heads_counter += 1
    counter_list[heads_counter] += 1/len(flip_list)
  return counter_list


x = [0, 1, 2, 3]
plt.style.use('bmh')
plt.plot(x, counter(coin_1))
plt.plot(x, counter(coin_2))
plt.plot(x, counter(coin_3))
plt.legend(['Coin 1','Coin 2','Coin 3'])
plt.xlabel('Number of Heads')
plt.ylabel('Experimental Probability')
plt.title('Biased Coins Graph')
plt.savefig('biased-coins.png')

#Based on the graph, I think that the only non-biased coin is coin 2. This is because it gives an equal amount of heads and tails. Coin 1 appears to be more tails heavy, while coin 3 is more head heavy.