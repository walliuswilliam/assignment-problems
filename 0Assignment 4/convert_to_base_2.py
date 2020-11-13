import math


def convert_to_base_2(input_b10):
  bits = math.floor(math.log(input_b10, 2)) + 1
  binary = ""
  var = input_b10
  for bit in range(bits, 0, -1):
    if var - 2**(bit - 1) >= 0:
      binary += '1'
      var -= 2**(bit - 1)
    else:
      binary += '0'
  return int(binary)

print('converting base 10 to base 2...')
assert convert_to_base_2(19) == 10011
print('passed')
