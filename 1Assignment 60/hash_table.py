array = [[], [], [], [], []]

def hash_function(string):
    char_sum = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in string:
      char_sum += alphabet.index(char)
    return char_sum%5

def insert(array, key, value):
    bucket_index = hash_function(key)
    array[bucket_index].append((key, value))

def find(array, key):
    bucket_index = hash_function(key)
    for entry in array[bucket_index]:
      if entry[0] == key:
        return entry[1]


print(array)
array = [[], [], [], [], []]

insert(array, 'a', [0,1])
insert(array, 'b', 'abcd')
insert(array, 'c', 3.14)
print(array)
# [[('a',[0,1])], [('b','abcd')], [('c',3.14)], [], []]

insert(array, 'd', 0)
insert(array, 'e', 0)
insert(array, 'f', 0)
print(array)
# [[('a',[0,1]), ('f',0)], [('b','abcd')], [('c',3.14)], [('d',0)], [('e',0)]]

print('testing hash_table...')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i, char in enumerate(alphabet):
    key = 'someletters'+char
    value = [i, i**2, i**3]
    insert(array, key, value)

for i, char in enumerate(alphabet):
    key = 'someletters'+char
    output_value = find(array, key)
    desired_value = [i, i**2, i**3]
    assert output_value == desired_value
print('passed')
