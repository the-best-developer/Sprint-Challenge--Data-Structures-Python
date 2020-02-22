class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    # TO BE COMPLETED

    prev_node = None
    next_node = None
    current = self.head
    
    # Loops through our linked list and changes our pointers to reverse
    while current != None:
      
      # Store next node in variable
      next_node = current.next_node
      
      # Next node is swapped with the prevous, and also set to None at the beginning to indicate end of list
      current.next_node = prev_node
      
      # Set our previous node to the current for next loop
      prev_node = current

      # Our next node in the list is where we will start in the next iteration
      current = next_node
    
    # At the end of the list, swap head with matching node at other end of the list
    self.head = prev_node
