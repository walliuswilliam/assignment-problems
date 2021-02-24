def find_midpoint_index(input_list):
    length = len(input_list)
    middle = length//2
    return middle

def bisection_search(value, input_list):
  sub_list = input_list
  low_index = 0
  high_index = len(input_list)-1
  while 1==1:
    midpoint_index = high_index-low_index//2
    if value > sub_list[midpoint_index]:
      low_index += (low_index + midpoint_index + 1)
    elif value < sub_list[midpoint_index]:
      high_index -= (high_index - midpoint_index + 1)
    else:
      return midpoint_index


print('testing bisection_search...')
assert bisection_search(14, [2, 3, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16]) == 9, bisection_search(14, [2, 3, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16])
print('passed')
