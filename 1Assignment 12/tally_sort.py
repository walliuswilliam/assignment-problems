def minimum(list_input):
  min_num = list_input[0]
  for num in list_input:
    if num < min_num:
      min_num = num
  return min_num

def maximum(list_input):
  max_num = list_input[0]
  for num in list_input:
    if num > max_num:
      max_num = num
  return max_num

def tally_sort(num_list):
  sorted_list = []
  small_num = minimum(num_list)
  tally_list = [0 for num in range(maximum(num_list)+1)]

  for i in range(len(num_list)):
    num_list[i] -= small_num

  for num in num_list:
    tally_list[num] += 1

  for tally in range(len(tally_list)):
    for num in range(tally_list[tally]):
      sorted_list.append(tally+small_num)
      
  return sorted_list

print('testing tally sort...')
assert tally_sort([2, 5, 2, 3, 8, 6, 3]) == [2, 2, 3, 3, 5, 6, 8]
print('passed')