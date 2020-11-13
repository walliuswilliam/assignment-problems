def is_symmetric(input_string):
  if input_string == input_string[::-1]:
    symmetry_check = True
  else:
    symmetry_check = False
  return symmetry_check

print("testing symmetry on 'racecar'")
assert is_symmetric("racecar") is True, '"racecar" failed'
print("Racecar has PASSED")

print("testing symmetry on 'batman'")
assert is_symmetric("batman") is False, '"batman" failed'
print("Batman has PASSED")
