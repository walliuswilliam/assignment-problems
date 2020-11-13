def unlist_nonrecursive(x):
  final_list = x
  while type(final_list) == list and len(final_list) == 1:
    final_list = final_list[0]
  return final_list

print('testing unlist nonrecursive...')
assert unlist_nonrecursive([[[[1], [2,3], 4]]]) == [[1], [2,3], 4]
print('passed')
assert unlist_nonrecursive([[[[1]]]]) == 1
print('passed')


def unlist_recursive(x):
  if type(x) != list or len(x) != 1:
    return x
  else:
    return unlist_recursive(x[0])

print('testing unlist recursive...')
assert unlist_recursive([[[[1], [2,3], 4]]]) == [[1], [2,3], 4]
print('passed')
assert unlist_recursive([[[[1]]]]) == 1
print('passed')
