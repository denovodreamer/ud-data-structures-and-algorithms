
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    """Implements a stack using linked lists."""
    
    def __init__(self):
        self.head = None
        self.num_elements = 0
        
    def push(self, value):
        new_node = Node(value)
        # if stack is empty
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head # place the new node at the head (top) of the linked list
            self.head = new_node

        self.num_elements += 1
        
    def pop(self):
        if self.is_empty():
            return
        
        value = self.head.value # copy data to a local variable
        self.head = self.head.next # move head pointer to point to next node (top is removed by doing so)
        self.num_elements -= 1
        return value
    
    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0



def to_list(stack):
    """Gets the data from the nodes into a list."""
    elements = []
    i = 0
    current = stack.head
    while current:
        elements.append(current.value)
        current = current.next
        i += 1
        if i > stack.num_elements:
            print("Iteration larger than number of elements.")
            break
    return elements