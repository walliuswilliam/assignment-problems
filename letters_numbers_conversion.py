def convert_to_numbers(input_string):
  an_array = []
for char in input_string:
  if char != ' ':
    an_array.append(ord(char) - 64)
