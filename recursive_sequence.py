def first_n_terms(n):
  list_results = []
  for number in range(1, n):
    if number == 1:
      initial = 5
      list_results.append(5)
    list_results.append(3*initial - 4)
    initial = 3*initial - 4
  return list_results

print('calculating first "10" terms...')
assert first_n_terms(10) == [
  5, 11, 29, 83, 245, 731, 2189, 6563, 19685, 59051], "calculation failed"
print('passed')


def nth_term(n):
  if n == 1:
    return 5
  answer = 3*nth_term(n-1) - 4
  return answer

print("calculating the '10th' term")
assert nth_term(10) == 59051, "failed calculation"
print("passed")
