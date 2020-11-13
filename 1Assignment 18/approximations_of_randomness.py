import sys
sys.path.append('1Assignment 11')
from kl_divergence_for_monte_carlo_simulations import kl_divergence
sys.path.append('0Assignment 7')
from monte_carlo_coin_flips import probability

flips = {
    'Justin S': 'HTTH HHTT TTHH TTTH HHTH TTHT HHHH THHT THTT HTHH TTTT HTHT TTHH THTH HTTH HHTH HHHT TTTH HTTH HTHT',
    'Nathan R': 'HTTH HHTH HTTT HTHH HTTH HHHH TTHH TTHT THTT HTHT HHTH TTTT THHT HTTH HTHH THHH HTTH THTT HHHT HTHH',
    'Justin H': 'HHHT HHTH HHTT THHT HTTT HTTT HHHT HTTT TTTT HTHT THHH TTHT TTHH HTHT TTTT HHHH THHH THTH HHHH THHT',
    'Nathan A': 'HTTH HHHH THHH TTTH HTTT THTT HTHT THHT HTTH TTTT HHHH TTHH HHTH TTTH HHHH THTT HTHT TTTT HHTT HHTT',
    'Cayden': 'HTHT HHTT HTTH THTH THHT TTHH HHHH TTTH HHHT HTTT TTHT HHTH HTHH THTT HHHH THTT HTTT HTHH TTTT HTTH',
    'Maia': 'HTHH THTH HTTH TTTT TTHT HHHH HHTT THHH TTHH HHTH THHT HHHH THTT HHTH HTHT TTHH TTHH HHHH TTTT HHHT',
    'Spencer': 'HHHT HTTH HTTT HTHH THTT TTHT TTTT HTTH HHTH TTHT TTHH HTHT THHT TTHT THTT THTH HTTH THHT TTTH HHHH',
    'Charlie': 'HHHH HHHT HHTT HTTT TTTT TTTH TTHH THHH THTH HTHT HHTH HTHH TTHT THTT THTH TTHT HTHT THHT HTTH THTH',
    'Anton': 'HHTH THTH TTTT HTTH THTT TTTH THHH TTHH THHT HHHH TTHT HTTT THTH HHHT HHTH HHHH TTTH HTHT TTTT HHTT',
    'William': 'THTT HHHT HTTH THHT THTH HHHT TTTH HHTH THTH HTHT HHHT TTHT HHHT THTT HHTT TTHH HHTH TTTT THTH TTHT'
}

def simple_sort(num_list):
  sorted_list = []
  for i in range(len(num_list)):
    min_num = num_list[0]
    for num in num_list:
      if num < min_num:
        min_num = num
    sorted_list.append(min_num)
    num_list.remove(min_num)
  return sorted_list

true_distribution = []
for heads in range(5):
  true_distribution.append(probability(heads, 4))


def count_heads(flip_sequence):
  num_heads = 0
  for outcome in flip_sequence:
    if outcome == 'H':
      num_heads += 1
  return num_heads

def calculate_distribution(sample):
  flip_list = [0, 0, 0, 0, 0]
  flip_split = sample.split(' ')
  for sample in flip_split:
    for num in range(5):
      if num == count_heads(sample):
        flip_list[num] += 1/len(flip_split)
  return flip_list


divergence_dict = {}
for key in flips:
  divergence_dict[key] = kl_divergence(calculate_distribution(flips[key]), true_distribution)
# div_list = simple_sort(divergence_list)

[print(key, value) for (key, value) in sorted(divergence_dict.items(), key=lambda x: x[1])]

#Charlie had the best approximation, as the divergence was the lowest