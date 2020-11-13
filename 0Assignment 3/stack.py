class Stack:
  data = []

  def push(self, var):
    self.data.append(var)

  def pop(self):
    self.data.pop()

  def peek(self):
    return self.data[len(self.data) - 1]

s = Stack()

print('running the first test')
assert s.data == [], 'test failed'
print("passed")


print('testing push')
s.push('a')
s.push('b')
s.push('c')
assert s.data == ['a', 'b', 'c'], 'test failed'
print("passed")


print('testing pop')
s.pop()
s.data == ['a', 'b'], 'test failed'
print("passed")


print('testing peek')
s.peek() == 'b'
print("passed")


print('running the fifth test')
s.data == ['a', 'b']
print("passed")
