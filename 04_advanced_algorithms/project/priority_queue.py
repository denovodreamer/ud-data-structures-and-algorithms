


class PriorityQueueNode:
    def __init__(self, state):
        self.state = state
        self.priority = state.total_cost
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

    def get(self, intersection):

        node = self.head

        while node:
            state = node.state
            if state.intersection == intersection:
                return node

            node = node.next
        return

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