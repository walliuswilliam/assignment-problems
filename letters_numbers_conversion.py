def convert_to_numbers(input_string):
  an_array = []
  for char in input_string:
    if char != ' ':
      an_array.append(ord(char) - 96) #found method from Remy, he explained how to do it
    if char == ' ':
      an_array.append(0)
  return an_array

assert convert_to_numbers('a cat') == [1, 0, 3, 1, 20], "test failed"
print('PASSED')

