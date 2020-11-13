def even_odd_tuples(input_list):
  return [(num, 'odd') if num % 2 == 1 else (num, 'even') for num in input_list]

print('testing if input is even or odd...')
assert even_odd_tuples([1, 2, 3, 5, 8, 11]) == [
  (1, 'odd'), (2, 'even'), (3, 'odd'), (5, 'odd'), (8, 'even'), (11, 'odd')], 'failed'
print('passed')


def even_odd_dict(input_list):
  return {num: 'odd' if num % 2 == 1 else 'even' for num in input_list}

print('testing if input is even or odd...')
assert even_odd_dict([1, 2, 3, 5, 8, 11]) == {
    1: 'odd',
    2: 'even',
    3: 'odd',
    5: 'odd',
    8: 'even',
    11: 'odd'
}, 'failed'
print('passed')
