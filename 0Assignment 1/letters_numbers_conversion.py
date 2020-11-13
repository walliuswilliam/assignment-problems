def convert_to_numbers(input_string):
  array = []
  for char in input_string:
    if char != ' ':
      array.append(ord(char) - 96)
    if char == ' ':
      array.append(0)
  return array

print('converting "batman" to numbers...')
assert convert_to_numbers('batman') == [2, 1, 20, 13, 1, 14], "test failed"
print('PASSED')


def convert_to_letters(input_list):
  a_string = ""
  for int_ in input_list:
    if int_ != 0:
      a_string += chr(int_ + 96)
    if int_ == 0:
      a_string += (" ")
  return a_string

print('converting [1, 0, 3, 1, 20] to letters...')
assert convert_to_letters([1, 0, 3, 1, 20]) == 'a cat', "test failed"
print('PASSED')
