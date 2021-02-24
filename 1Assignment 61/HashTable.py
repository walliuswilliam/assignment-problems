class HashTable:
  def __init__(self, num_buckets):
    self.num_buckets = num_buckets
    self.buckets = [[] for num in range(num_buckets)]
    self.alphabet = 'abcdefghijklmnopqrstuvwxyz'


  def hash_function(self, string):
    char_sum = 0
    for char in string:
      char_sum += self.alphabet.index(char)
    return char_sum%self.num_buckets

  def insert(self, key, value):
    bucket_index = self.hash_function(key)
    self.buckets[bucket_index].append((key, value))

  def find(self, key):
    bucket_index = self.hash_function(key)
    for entry in self.buckets[bucket_index]:
      if entry[0] == key:
        return entry[1]



ht = HashTable(num_buckets = 3)
print('testing HashTable...')
assert ht.buckets == [[], [], []]
assert ht.hash_function('cabbage') == 2

ht.insert('cabbage', 5)
assert ht.buckets == [[], [], [('cabbage',5)]]

ht.insert('cab', 20)
assert ht.buckets == [[('cab', 20)], [], [('cabbage',5)]]

ht.insert('c', 17)
assert ht.buckets == [[('cab', 20)], [], [('cabbage',5), ('c',17)]]

ht.insert('ac', 21)
assert ht.buckets == [[('cab', 20)], [], [('cabbage',5), ('c',17), ('ac', 21)]]

assert ht.find('cabbage') == 5
assert ht.find('cab') == 20
assert ht.find('c') == 17
assert ht.find('ac') == 21

print('passed')
