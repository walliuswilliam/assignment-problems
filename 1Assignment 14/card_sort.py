def insert_element_into_sorted_list(element, sorted_list):
  for element_compare in range(len(sorted_list)):
    if element < sorted_list[element_compare]:
      sorted_list.insert(element_compare, element)
      return sorted_list
  sorted_list.append(element)
  return sorted_list

def card_sort(num_list):
  sorted_list = [num_list[0]]
  for element in range(1, len(num_list)):
    sorted_list = insert_element_into_sorted_list(num_list[element], sorted_list)
  return sorted_list

print('testing card sort...')
assert card_sort([12, 11, 13, 5, 6]) == [5, 6, 11, 12, 13]
assert card_sort([5, 7, 3, 5, 1, 3, -1, 1, -3, -1, -3, -1]) == [
  -3, -3, -1, -1, -1, 1, 1, 3, 3, 5, 5, 7]
print('passed')