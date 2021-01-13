def separate_into_words(input_string):
  separate_words = input_string.split(' ')
  return separate_words

print('separating string into words...')
assert separate_into_words("look the dog ran fast") == ["look", "the", "dog", "ran", "fast"], 'failed'
print('passed')

def reverse_word_order(input_string):
  string = separate_into_words(input_string)
  string.reverse()
  backwards_string = ' '.join([str(word) for word in string]) 
  return backwards_string
print(reverse_word_order("look the dog ran fast"))