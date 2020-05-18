from node import NodeSinglyLinked

class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit
        
  def has_space(self):
    return self.limit > self.size

  def is_empty(self):
    return self.size == 0
 
  def push(self, value):
    if (self.has_space()):
      item = NodeSinglyLinked(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      # Increment stack size by 1 here:
      self.size += 1
    else:
      print("stack overflow")

  def pop(self):
    if self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("stack underflow")
  
  def peek(self):
    if self.is_empty():
	    return self.top_item.get_value()
    else:
      print("empty stack")

  
