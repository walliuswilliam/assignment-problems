def get_children(parent, input_list):
  output_list = []
  for pair in input_list:
    if pair[0] == parent:
      output_list.append(pair[1])
  return output_list


def get_parents(child, input_list):
  output_list = []
  for pair in input_list:
    if pair[1] == child:
      output_list.append(pair[0])
  return output_list

def get_roots(input_list):
  output_list = []
  for pair in input_list:
    if get_parents(pair[0], input_list) == []:
      output_list.append(pair[0])
  return output_list


edges = [('a','c'), ('e','g'), ('e','i'), ('e','a'), ('d','b'), ('a','d'), ('d','f'), ('f','h'), ('d','j'), ('d','k')]

print('testing "tree"...')
assert get_children('e', edges) == ['g', 'i', 'a'],  get_children('e', edges)
assert get_children('c', edges) == []
assert get_children('f', edges) == ['h']
assert get_parents('e', edges) == []
assert get_parents('c', edges) == ['a']
assert get_parents('f', edges) == ['d']
assert get_roots(edges) == ['e'], get_roots(edges)
print('passed')