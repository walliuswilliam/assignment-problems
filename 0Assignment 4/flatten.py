colors = {
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

flat_colors = {
  'animal_bumblebee': ['yellow', 'black'],
  'animal_elephant': ['gray'],
  'animal_fox': ['orange', 'white'],
  'food_apple': ['red', 'green', 'yellow'],
  'food_cheese': ['white', 'orange']
}


def flatten(input_dict):
 flat_dict = {}
 for key in input_dict:
   for nested_key in input_dict[key]:
     flat_dict[key + '_' + nested_key] = input_dict[key][nested_key]
 return flat_dict


print('flattening dictionary')
assert flatten(colors) == flat_colors, "failed"
print('passed')
