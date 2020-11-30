import sys
sys.path.append('1Assignment 21')
from merge_sort import merge

def merge_sort(input_list):
  if len(input_list) > 1:
    length = len(input_list)
    middle = length//2
    left_half = input_list[:middle]
    right_half = input_list[middle:]
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left, right)
  else:
    return input_list

print('testing merge sort 2...')
assert merge_sort([4,8,7,7,4,2,3,1]) == [1,2,3,4,4,7,7,8], merge_sort([4,8,7,7,4,2,3,1])
print('passed')