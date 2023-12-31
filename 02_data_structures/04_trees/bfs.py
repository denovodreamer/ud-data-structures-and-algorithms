

class QueueNode:
    
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0
        
    def enqueue(self, value):
        new_node = QueueNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node    # add data to the next attribute of the tail (i.e. the end of the queue)
            self.tail = self.tail.next   # shift the tail (i.e., the back of the queue)
        self.num_elements += 1
            
    def dequeue(self):
        if self.is_empty():
            return None
        value = self.head.value          # copy the value to a local variable
        self.head = self.head.next       # shift the head (i.e., the front of the queue)
        self.num_elements -= 1
        return value
    
    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0
        
    def to_list(self):
        elements = []
        
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
            
        return elements

    # def __repr__(self):
    #     if len(self.q) > 0:
    #         s = "<enqueue here>\n_________________\n" 
    #         s += "\n_________________\n".join([str(item) for item in self.q])
    #         s += "\n_________________\n<dequeue here>"
    #         return s
    #     else:
    #         return "<queue is empty>"


# from collections import deque
# class Queue():
#     def __init__(self):
#         self.q = deque()
        
#     def enq(self,value):
#         self.q.appendleft(value)
        
#     def deq(self):
#         if len(self.q) > 0:
#             return self.q.pop()
#         else:
#             return None
    
#     def __len__(self):
#         return len(self.q)
    
#     def __repr__(self):
#         if len(self.q) > 0:
#             s = "<enqueue here>\n_________________\n" 
#             s += "\n_________________\n".join([str(item) for item in self.q])
#             s += "\n_________________\n<dequeue here>"
#             return s
#         else:
#             return "<queue is empty>"



class Node:
        
    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None
        
    def set_value(self,value):
        self.value = value
        
    def get_value(self):
        return self.value
        
    def set_left_child(self,left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"
    
    
       


class Tree():
    def __init__(self, value=None):
        self.root = Node(value)
        
    def get_root(self):
        return self.root
    
    # def __repr__(self):
    #     level = 0
    #     q = Queue()
    #     visit_order = list()
    #     node = self.get_root()
    #     q.enq( (node,level) )
    #     while(len(q) > 0):
    #         node, level = q.deq()
    #         if node == None:
    #             visit_order.append( ("<empty>", level))
    #             continue
    #         visit_order.append( (node, level) )
    #         if node.has_left_child():
    #             q.enq( (node.get_left_child(), level +1 ))
    #         else:
    #             q.enq( (None, level +1) )
                
    #         if node.has_right_child():
    #             q.enq( (node.get_right_child(), level +1 ))
    #         else:
    #             q.enq( (None, level +1) )
                
    #     s = "Tree\n"
    #     previous_level = -1
    #     for i in range(len(visit_order)):
    #         node, level = visit_order[i]
    #         if level == previous_level:
    #             s += " | " + str(node) 
    #         else:
    #             s += "\n" + str(node)
    #             previous_level = level

    #     return s



def bfs(tree: Tree):
    q = Queue()
    visit_order = list()

    node = tree.get_root()

    q.enqueue(node)
    while(len(q) > 0):
        node: Node = q.dequeue()
        visit_order.append(node)
        if node.has_left_child():
            q.enqueue(node.get_left_child())
        if node.has_right_child():
            q.enqueue(node.get_right_child())

    return visit_order