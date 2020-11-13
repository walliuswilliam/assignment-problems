def identity_matrix_elements(n):
  return [[int(x == y) for x in range(n)] for y in range(n)]

print('creating identity matrix...')
assert identity_matrix_elements(4) == [[1, 0, 0, 0], [0, 1, 0, 0
], [0, 0, 1, 0], [0, 0, 0, 1]]
print('passed')


def counting_across_rows_matrix_elements(m,n):
  return [[(x+1)+n*y for x in range(n)] for y in range(m)]

print('creating counting matrix...')
assert counting_across_rows_matrix_elements(3,4) == [[1, 2, 3, 4], [5, 6, 7, 8
],[9, 10, 11, 12]], 'failed'
print('passed')