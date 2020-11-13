def update_bounds(bounds):
  new_bounds = []
  midpoint = (bounds[1]+bounds[0])/2
  if midpoint**2 > 2:
    new_bounds.append(bounds[0])
    new_bounds.append(midpoint)
  else:
    new_bounds.append(midpoint)
    new_bounds.append(bounds[1])
  return new_bounds

print('refining bounds for sqrt(2)...')
assert update_bounds([1, 2]) == [1, 1.5], 'failed'
print('passed')

print('refining bounds for sqrt(2)...')
assert update_bounds([1, 1.5]) == [1.25, 1.5]
print('passed')


def estimate_root(precision):
  bounds = update_bounds([1, 2])
  while abs(bounds[1] - bounds[0]) > precision:
    bounds = update_bounds(bounds)
  approx = (bounds[1]+bounds[0])/2
  return approx

print("approximating sqrt(2)...")
assert estimate_root(0.1) == 1.40625, 'failed'
print('passed')
