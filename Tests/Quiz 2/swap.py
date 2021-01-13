def swap_sort(num_list):
  num_swaps = 0
  for i in range(len(num_list)-1):
    x = num_list[i]
    y = num_list[i+1]
    if x > y:
      num_list[i] = y
      num_list[i+1] = x
      num_swaps += 1
  if num_swaps != 0:
    return swap_sort(num_list)
  else:
    return num_list


print(swap_sort([5,8,2,2,4,3,0,2,-5,3.14,2]))