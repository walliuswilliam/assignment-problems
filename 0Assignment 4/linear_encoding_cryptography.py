letters = " abcdefghijklmnopqrstuvwxyz"


#part a
def encode(string, a, b):
  message = []
  for letter in string:
    message.append(a * letters.index(letter) + b)
  return message

print('encoding "a cat"...')
assert encode('a cat', 2, 3) == [5, 3, 9, 5, 43], 'assertion failed'
print('passed')


#part b
def decode(numbers, a, b):
  decoded = ""
  for num in numbers:
    if (num - b)/a < 0 or (num - b)/a > 26 or int((num - b)/a) != (num - b)/a:
      return False
    else:
      decoded += letters[int((num - b)/a)]
  return decoded

print('decoding [5, 3, 9, 5, 43]')
assert decode([5, 3, 9, 5, 43], 2, 3) == 'a cat', "assertion failed"
print('passed')

print('testing wrong input (negative number)...')
assert decode([1, 3, 9, 5, 43], 2, 3) is False, 'assertion failed'
print('passed')

print('testing wrong input (decimal)...')
assert decode([5, 3, 9, 5, 44], 2, 3) is False, 'assertion failed'
print('passed')

#part c
code = [377, 717, 71, 513, 105, 921, 581, 547, 547, 105, 377, 717, 241,
 71, 105, 547, 71, 377, 547, 717, 751, 683, 785, 513, 241, 547, 751]

for a in range(1, 101):
  for b in range(0, 101):
    if decode(code, a, b) is not False:
      print(decode(code, a, b))
