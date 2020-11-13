colors = {
  'animal_bumblebee': ['yellow', 'black'],
  'animal_elephant': ['gray'],
  'animal_fox': ['orange', 'white'],
  'food_apple': ['red', 'green', 'yellow'],
  'food_cheese': ['white', 'orange']
}

nested_colors = {
  'animal': {
    'bumblebee': ['yellow', 'black'],
    'elephant': ['gray'],
    'fox': ['orange', 'white']
  },
  'food': {
    'apple': ['red', 'green', 'yellow'],
    'cheese': ['white', 'orange']
  }
}

def make_nested(input_dict):
  result = {}
  for key in input_dict:
    var = key.split('_')
    if var[0] not in result:
      result[var[0]] = {}
    result[var[0]][var[1]] = input_dict[key]
  return result

print('nesting dictionaries...')
assert make_nested(colors) == nested_colors, "failed"
print('passed')
