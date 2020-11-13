class Queue:
  data = []

  def enqueue(self, var):
    self.data.append(var)

  def dequeue(self):
    self.data.pop(0)

  def peek(self):
    return self.data[0]

q = Queue()

print("testing 'q.data'")
assert q.data == [], 'test failed'
print("passed")


print('testing enqueue')
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
assert q.data == ['a', 'b', 'c'], 'test failed'
print("passed")


print('testing dequeue')
q.dequeue()
q.data == ['b', 'c'], 'test failed'
print("passed")


print('testing peek')
q.peek() == 'b'
print("passed")


print("retesting 'q.data'")
q.data == ['b', 'c']
print("passed")
