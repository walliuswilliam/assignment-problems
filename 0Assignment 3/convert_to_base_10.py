def convert_to_base_10(input):
  total = 0
  count = 0
  binary_list = [int(x) for x in str(input)]
  binary_list = binary_list[::-1]
  for num in binary_list:
    if num == 1:
      total += 2**count
    count += 1
  return total

print('converting binary to base 10')
assert convert_to_base_10(10011) == 19, "conversion failed"
print('passed')