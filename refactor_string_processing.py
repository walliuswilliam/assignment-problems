string = '"alpha","beta","gamma","delta"\n1,2,3,4\n5.0,6.0,7.0,8.0'
string_list = [x.split(',') for x in string.split('\n')]
length_of_string = len(string)
arr = []

for string in string_list:
  newstring = []
  
  if len(string) > 0:
    for char in string:
      if char[0]=='"' and char[-1]=='"':
        char = char.strip('"')

      elif '.' in char:
        char = float(char)

      else:
        char = int(char)
          newstring.append(char)
  arr.append(newstring)

print(arr)