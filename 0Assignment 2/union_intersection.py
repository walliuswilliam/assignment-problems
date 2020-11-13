def intersection(list1, list2):
 intersection_set = set.intersection(set(list1), set(list2))
 return(intersection_set)

print("testing intersections between [1,2,'a','b'] and [2,3,'a']")
assert intersection(
  {1, 2, 'a', 'b'}, {2, 3, 'a'}) == {2, 'a'}, 'intersection failed'
print('passed')


def union(list1, list2):
 union_set = set.union(set(list1), set(list2))
 return(union_set)

print("testing union between [1,2,'a','b'] and [2,3,'a']")
print(union([1, 2, 'a', 'b'], [2, 3, 'a']))
assert union(
  {1, 2, 'a', 'b'}, {2, 3, 'a'}) == {1, 2, 3, 'a', 'b'}, 'union test failed'
print('passed')
