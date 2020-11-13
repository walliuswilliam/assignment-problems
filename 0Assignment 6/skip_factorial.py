def skip_factorial_nonrecursive(n):
  factorial = 1
  for num in range(n, 0, -2):
    factorial = factorial*num
  return factorial

print('testing inputs of skip factorial without recursion...')
assert skip_factorial_nonrecursive(6) == 48, 'failed'
print('input 1 passed')
assert skip_factorial_nonrecursive(7) == 105, 'failed'
print('input 2 passed')


def skip_factorial_recursive(n):
  if n <= 1:
    return 1
  else:
    return n*skip_factorial_recursive(n-2)

print('testing inputs of skip factorial with recursion...')
assert skip_factorial_nonrecursive(6) == 48, 'failed'
print('input 1 passed')
assert skip_factorial_nonrecursive(7) == 105, 'failed'
print('input 2 passed')
