def cartesian_product(arrays):
  points = [[]]
  for an_array in arrays:
    new_list = []
    for point in range(len(points)):
      first_point = points[point]
      for var in range(len(an_array)):
        new_list.append(first_point + [an_array[var]])
    points = list(new_list)
  return points


if __name__ == "__main__":
  print('testing cartesian_product...')
  assert cartesian_product([['a'], [1,2,3], ['Y','Z']]) == [
    ['a',1,'Y'], ['a',1,'Z'], ['a',2,'Y'], ['a',2,'Z'], ['a',3,'Y'], ['a',3,'Z']], cartesian_product([['a'], [1,2,3], ['Y','Z']])
  print('passed')
