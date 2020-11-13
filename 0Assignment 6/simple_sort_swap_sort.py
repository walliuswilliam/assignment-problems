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

print("sorting list...")
assert simple_sort([5,8,2,2,4,3,0,2,-5,3.14,2]) == [
  -5,0,2,2,2,2,3,3.14,4,5,8]
print('passed')


def swap_sort(x):
  for nums in range(len(x)):
    for num in range(len(x) - 1):
      if x[num] > x[num + 1]:
        x[num], x[num + 1] = x[num + 1], x[num]
  return x

print('sorting list by swapping...')
assert swap_sort([5,8,2,2,4,3,0,2,-5,3.14,2]) == [
  -5,0,2,2,2,2,3,3.14,4,5,8]
print('passed')
