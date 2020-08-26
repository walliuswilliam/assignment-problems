def count_characters(input_string):
  lowstring = input_string.lower()
  dict = {}
  for char in lowstring:
    dictkey = dict.keys()
    if char in dictkey:
      dict[char] += 1
    else:
      dict[char] = 1
  return dict

print("counting characters in 'A cat!!!'")
assert count_characters("A cat!!!") == {
  'a': 2, 'c': 1, 't': 1, ' ': 1, '!': 3}, "counting failed"
print('passed')
