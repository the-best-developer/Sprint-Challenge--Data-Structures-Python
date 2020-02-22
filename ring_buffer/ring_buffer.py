from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):

        # If we have room, go ahead and add our item
        if self.capacity > self.storage.length:
            # Add item
            self.storage.add_to_tail(item)
            # Update our current node location to the oldest
            self.current = self.storage.tail

        # If our list is full, we are overwriting our current values with newer ones
        if self.capacity == self.storage.length:
            # If we are at the tail, start over at the head
            if self.current == self.storage.tail:
                self.current.value = item
                self.current = self.storage.head
            
            elif self.current != None:
                # Set item and set current to next node in our list to overwrite
                self.current.value = item
                self.current = self.current.next
            
            


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        
        # Start at the head and loop through our list
        current = self.storage.head
        # Loop till we hit a None value (end of list)
        while current:
            list_buffer_contents.append(current.value)
            current = current.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
