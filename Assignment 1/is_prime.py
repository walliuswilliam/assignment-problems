import math


def is_prime(n):
  prime_check = True
  for m in range(2, math.floor(n/2)):
    if n % m == 0:
      prime_check = False
  return prime_check

print("testing if '59' is prime...")
assert is_prime(59) is True, 'is_prime(59) is False'
print('PASSED')

print("testing if '51' is prime...")
assert is_prime(51) is False, 'is_prime(59) is True'
print('PASSED')
