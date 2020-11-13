def count_compression(string):
  temp_list = []
  tuple_list = []
  for num in range(len(string)):
    if string[num] == string[num-1] and num != 0:
      temp_list[-1][1] += 1
    else:
      temp_list.append([string[num], 1])
  for lists in temp_list:
    tuple_list.append(tuple(lists))
  return tuple_list
print('testing count compression...')
assert count_compression('aaabbcaaaa') == [('a',3), ('b',2), ('c',1), ('a',4)]
assert count_compression('22344444') == [('2',2), ('3',1), ('4',5)]
print('passed')

def count_decompression(compressed_string):
  decompressed = ''
  for tuple_list in compressed_string:
    for num in range(tuple_list[1]):
      decompressed += tuple_list[0]
  return decompressed

print('testing count decompression...')
assert count_decompression([('a',3), ('b',2), ('c',1), ('a',4)]) == 'aaabbcaaaa'
assert count_decompression([('2',2), ('3',1), ('4',5)]) == '22344444'
print('passed')
