def convert_to_numbers(input_string):
  an_array = []
  for char in input_string:
    if char != ' ':
      an_array.append(ord(char) - 9)
    if char == ' ':
      an_array.append(0)
  return an_array
print(convert_to_numbers('a cat'))
