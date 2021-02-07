test_string = '"alpha","beta","gamma","delta"\n1,2,3,4\n5.0,6.0,7.0,8.0'
nested_string_list = [strings.split(',') for strings in test_string.split('\n')]
arr = []

for value_list in nested_string_list:
  new_strings_list = []

  for string in value_list:
    print(string)
    if string[0]=='"' and string[-1]=='"':
      string = string.strip('"')

    elif '.' in string:
      string = float(string)

    else:
      string = int(string)
    new_strings_list.append(string)
  arr.append(new_strings_list)

print(arr)


