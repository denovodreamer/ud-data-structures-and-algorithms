

######################################################################################################
#   Priority queue for the Huffman tree construction
######################################################################################################


class PriorityQueueNode:
    def __init__(self, node):
        self.node = node
        self.priority = node.frequency
        self.next = None
        self.previous = None



class PriorityQueue:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def insert(self, node):

        new_node = PriorityQueueNode(node)
        
        if self.head is None:
            self.head = new_node
            self.num_elements += 1
            return

        current_node = self.head
        
        while current_node:
            
            if new_node.priority <= current_node.priority:

                if current_node is self.head: # Front of the queue
                    current_node.previous = new_node
                    new_node.next = current_node
                    self.head = new_node
                else: # Wihtin the queue
                    new_node.previous = current_node.previous
                    new_node.next = current_node

                    current_node.previous.next = new_node
                    current_node.previous = new_node

                self.num_elements += 1
                return

            # End of queue
            if current_node.next is None:
                current_node.next = new_node
                new_node.previous = current_node

                self.num_elements += 1
                return
            
            current_node = current_node.next
    

    def pop(self):

        node = self.head

        # If only one node
        if self.size() == 1:
            self.head = None
            self.num_elements -= 1
            return node
            
        node.next.previous = None
        self.head = node.next
        node.next = None

        self.num_elements -= 1
        return node
        
    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0

    def print(self):
        out = []
        node = self.head
        while node:
            out.append(node.priority)
            node = node.next
        return out
    

######################################################################################################
#   Nodes for the tree
######################################################################################################

class CharacterNode:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        
    def __repr__(self):
        return f"CharacterNode({self.character, self.frequency})"
    
    def __str__(self):
        return f"CharacterNode({self.character, self.frequency})"


class InternalNode:
        
    def __init__(self, frequency=None):
        self.frequency = frequency
        self.left = None
        self.right = None
           
    def set_left_child(self,node):
        self.left = node
        
    def set_right_child(self, node):
        self.right = node
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left is not None
    
    def has_right_child(self):
        return self.right is not None
    
    def __repr__(self):
        return f"InternalNode({self.frequency})"
    
    def __str__(self):
        return f"InternalNode({self.frequency})"
    


######################################################################################################
#  Huffman tree
######################################################################################################

from collections import deque


# Queue to print the tree
class Queue():
    def __init__(self):
        self.q = deque()
        
    def enq(self,value):
        self.q.appendleft(value)
        
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
    
    def __len__(self):
        return len(self.q)
    
    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n" 
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"



class Tree:
    def __init__(self):
        self.root = None

    def set_root(self, root):
        self.root = root

    def get_root(self):
        return self.root
    
    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq( (node,level) )
        while(len(q) > 0):
            node, level = q.deq()

            if node == None:
                continue
            visit_order.append((node, level))
            
            if isinstance(node, InternalNode) and node.has_left_child():
                q.enq( (node.get_left_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

            if isinstance(node, InternalNode) and node.has_right_child():
                q.enq( (node.get_right_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node) 
            else:
                s += "\n" + str(node)
                previous_level = level

                
        return s


######################################################################################################
#   Build tree
######################################################################################################

def compute_frequencies(message):
    frequencies = {}
    for letter in message:
        if letter not in frequencies:
            frequencies[letter] = 1
        else:
            frequencies[letter] += 1
    
    frequencies = list(frequencies.items())
    frequencies = sorted(frequencies, key=lambda x: x[1])

    frequencies_table = []
    for character, frequency in frequencies:
        node = CharacterNode(character, frequency)
        frequencies_table.append(node)
        
    return frequencies_table



def build_huffman_tree(frequencies_table):
    node_list = list(frequencies_table)

    # Build initial priority queue
    queue = PriorityQueue()
    for character_node in node_list:
        queue.insert(character_node)

    while queue.size() > 1:
        
        # First two elements of the queue (lowest priority)
        node_1 = queue.pop()
        node_2 = queue.pop()
        
        # Create new internal node
        frequency = node_1.priority + node_2.priority
        new_node = InternalNode(frequency)
    
        # Merge into one internal node
        new_node.set_left_child(node_1.node)
        new_node.set_right_child(node_2.node)
    
        # Insert the new internal node back into the queue
        queue.insert(new_node)


    # The root of the Huffman tree is the only node on the queue
    huffman_tree = Tree()
    root = queue.head.node
    huffman_tree.set_root(root)

    return huffman_tree


######################################################################################################
#   Encoding
######################################################################################################

def traverse(node, base_code, codes):

    if isinstance(node, CharacterNode):
        codes[node.character] = base_code
        return
        
    code = base_code + "0"
    traverse(node.get_left_child(), code, codes)

    code = base_code + "1"
    traverse(node.get_right_child(), code, codes)

    return


def process_encoding(tree):
    
    code = ""
    codes = {}
    traverse(tree.get_root(), code, codes)
    
    return codes


def huffman_encoding(message):
   
    frequencies_table = compute_frequencies(message)

    tree = build_huffman_tree(frequencies_table)

    encoding = process_encoding(tree)

    encoded_message = ""
    for character in message:
        encoded_message = encoded_message + encoding[character]
    
    return encoded_message, tree


######################################################################################################
#   Decoding
######################################################################################################

def traverse_tree(root, encoded_message):

    node = root
    while node:

        if isinstance(node, CharacterNode):
            return node.character, encoded_message
        
        next_bit = encoded_message[0]
        encoded_message = encoded_message[1:]

        if next_bit == "0":
            next_node = node.get_left_child()
        elif next_bit == "1":
            next_node = node.get_right_child()

        node = next_node
    
    return


def huffman_decoding(encoded_message, tree):
    
    decoded_message = ""

    while len(encoded_message) > 0:
        character, encoded_message = traverse_tree(tree.get_root(), encoded_message)
        decoded_message += character
    
    return decoded_message


######################################################################################################
#   Tests
######################################################################################################

def test_encoding():
    message = "AAAAAAABBBCCCCCCCDDEEEEEE"

    encoded_message, _ = huffman_encoding(message)
    assert encoded_message == "1110100100010111000110101101100111111110111100010001011001110000101101"


def test_decoding():
    message = "AAAAAAABBBCCCCCCCDDEEEEEE"
    encoded_message, tree = huffman_encoding(message)
    decoded_message = huffman_decoding(encoded_message, tree)
    assert decoded_message == message

if __name__ == "__name__":
    test_encoding()
    test_decoding()

