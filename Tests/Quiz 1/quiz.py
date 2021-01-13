def recursive(n):
  if n == 1:
    return 0
  elif n == 2:
    return 3
  else:
    return recursive(n-1)-2*(recursive(n-2))
print(recursive(6))