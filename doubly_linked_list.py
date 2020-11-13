class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None
    self.index = 0

class DoublyLinkedList:
  def __init__(self, head):
    self.head = Node(head)
  
  def print_data(self):
    head_data = self.head
    print(head_data.data)
    while head_data.next is not None:
      print(head_data.next.data)
      head_data = head_data.next

  def append(self, num):
    last_node = self.head
    node_index = 0
    while last_node.next is not None:
      last_node = last_node.next
      node_index += 1
    node_index += 1
    last_node.next = Node(num)
    last_node.next.index = node_index

  def length(self):
    node_head = self.head
    count = 0
    while node_head is not None:
      count += 1
      node_head = node_head.next
    return count

    
  def push(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node

    current_node = self.head
    current_index = 0
    while current_node is not None:
      current_node.index = current_index
      current_index += 1
      current_node = current_node.next


  def get_node(self, index):
    node_head = self.head
    for num in range(index):
      node_head = node_head.next
    return node_head
  
  def delete(self, index):
    prev_node = self.get_node(index-1)
    next_node = self.get_node(index+1)
    node = prev_node
    prev_node.next = next_node
    while node.next != None:
      node.index -= 1
      node = node.next
   
  def insert(self, new_data, index):
    new_node = Node(new_data)
    prev_node = self.get_node(index-1)
    curr_node = self.get_node(index)
    node = prev_node
    prev_node.next = new_node
    new_node.next = curr_node
    while node.next != None:
      node.index += 1
      node = node.next


print('checking class Node...')
A = Node(4)
assert A.data == 4
assert A.next == None
B = Node(8)
A.next = B
assert A.next.data == 8
print('passed')

print('checking class Linked List...')
linked_list = LinkedList(4)
assert linked_list.head.data == 4
linked_list.append(8)
assert linked_list.head.next.data == 8
linked_list.append(9)
print('printing list data:')
linked_list.print_data()
assert linked_list.length() == 3
print('passed')


linked_list = LinkedList('b')
linked_list.append('e')
linked_list.append('f')
linked_list.push('a')

print("checking method 'length'...")
assert linked_list.length() == 4
print('passed')

print("checking attribute 'index'...")
assert linked_list.head.index == 0
print('passed')
assert linked_list.head.next.index == 1
print('passed')
assert linked_list.head.next.next.index == 2
print('passed')
assert linked_list.head.next.next.next.index == 3
print('passed')

print("checking method 'get node'...")
assert linked_list.get_node(0).data == 'a', linked_list.get_node(0).data
print('passed')
assert linked_list.get_node(1).data == 'b', linked_list.get_node(1).data
print('passed')
assert linked_list.get_node(2).data == 'e'
print('passed')
assert linked_list.get_node(3).data == 'f'
print('passed')

print('')
print('')
linked_list = LinkedList('a')
linked_list.append('b')
linked_list.append('c')
linked_list.append('d')
linked_list.append('e')
print("checking method 'length'...")
assert linked_list.length() == 5
print('passed')

linked_list.print_data()

print("checking method 'get node'...")
assert linked_list.get_node(2).data == 'c'
print('passed')
linked_list.delete(2)

print("checking method 'length'...")
assert linked_list.length() == 4
print('passed')

print("checking method 'get node'...")
linked_list.get_node(2).data == 'd'
print('passed')

linked_list.print_data()

print("checking method 'insert'...")
linked_list.insert('f', 2)
assert linked_list.length() == 5, linked_list.length
assert linked_list.get_node(2).data == 'f'
linked_list.print_data()
print('passed')