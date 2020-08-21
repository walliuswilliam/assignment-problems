def is_symmetric(input_string):
  if input_string == input_string[::-1]:
    symmetry_check = True
  else:
    symmetry_check = False
  return symmetry_check

print(is_symmetric("racecar"))
print(is_symmetric("batman"))
