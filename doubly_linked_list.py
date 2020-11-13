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
    last_node.next.prev = last_node

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
    next_node.prev = prev_node
    while node.next != None:
      node.index -= 1
      node = node.next
   
  def insert(self, new_data, index):
    new_node = Node(new_data)
    prev_node = self.get_node(index-1)
    curr_node = self.get_node(index)
    node = prev_node
    curr_node.prev = new_node
    prev_node.next = new_node
    new_node.next = curr_node
    new_node.prev = prev_node
    while node.next != None:
      node.index += 1
      node = node.next


doubly_linked_list = DoublyLinkedList('a')
doubly_linked_list.append('c')
doubly_linked_list.append('d')
doubly_linked_list.append('e')
doubly_linked_list.insert('b',1)
doubly_linked_list.delete(3)


print('testing doubly linked list...')
current_node = doubly_linked_list.get_node(3)
node_values = [current_node.data]
for _ in range(3):
  current_node = current_node.prev
  node_values.append(current_node.data)
assert node_values == ['e', 'c', 'b', 'a'], node_values
print('passed')
