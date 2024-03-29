


class GraphNode(object):
    def __init__(self, val):
        self.value = val
        self.children = []

    def add_child(self,new_node):
        self.children.append(new_node)

    def remove_child(self,del_node):
        if del_node in self.children:
            self.children.remove(del_node)

class Graph(object):
    def __init__(self,node_list):
        self.nodes = node_list

    def add_edge(self,node1,node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.add_child(node2)
            node2.add_child(node1)

    def remove_edge(self,node1,node2):
        if(node1 in self.nodes and node2 in self.nodes):
            node1.remove_child(node2)
            node2.remove_child(node1)



# Iterative Solution

def dfs_search(root_node, search_value):
    visited = set()                         # Sets are faster for lookups
    stack = [root_node]                     # Start with a given root node

    while len(stack) > 0:                   # Repeat until the stack is empty

        current_node = stack.pop()          # Pop out a node added recently
        visited.add(current_node)           # Mark it as visited

        if current_node.value == search_value:
            return current_node

        # Check all the neighbours
        for child in current_node.children:

            # If a node hasn't been visited before, and not available in the stack already.
            if (child not in visited) and (child not in stack):
                stack.append(child)


# Recursion Solution

def dfs_recursion(node, search_value, visited):

    if node.value == search_value:
        return node

    visited.add(node)

    for child in node.children:

        if child not in visited:

            node = dfs_recursion(child, search_value, visited)

            if node:
                return node

    return


def dfs_recursion_start(start_node, search_value):

    visited = set()

    return dfs_recursion(start_node, search_value, visited)