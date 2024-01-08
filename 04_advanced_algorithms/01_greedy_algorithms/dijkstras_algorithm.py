


from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = set()                   # A set cannot contain duplicate nodes
        self.neighbours = defaultdict(list)  # Defaultdict is a child class of Dictionary that provides a default value for a key that does not exists.
        self.distances = {}                  # Dictionary. An example record as ('A', 'B'): 6 shows the distance between 'A' to 'B' is 6 units

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.neighbours[from_node].append(to_node)
        self.neighbours[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance    # lets make the graph undirected / bidirectional

    def print_graph(self):
        print("Set of Nodes are: ", self.nodes)
        print("Neighbours are: ", self.neighbours)
        print("Distances are: ", self.distances)




import sys

def dijkstra(graph, source):
    '''
    Find the shortest path from the source node to every other node in the given graph
    '''

    result = {}
    result[source] = 0

    for node in graph.nodes:
        if (node != source):
            result[node] = sys.maxsize

    unvisited = set(graph.nodes)

    path = {}

    '''THE GREEDY APPROACH'''
    # As long as unvisited is non-empty
    while unvisited:
        min_node = None

        # 1. Find the unvisited node having smallest known distance from the source node.
        for node in unvisited:
            if node in result:

                if min_node is None:
                    min_node = node
                elif result[node] < result[min_node]:
                    min_node = node

        if min_node is None:
            break

        # known distance of min_node
        current_distance = result[min_node]

        # 2. For the current node, find all the unvisited neighbours.
        # For this, you have calculate the distance of each unvisited neighbour.
        for neighbour in graph.neighbours[min_node]:
            if neighbour in unvisited:
                distance = current_distance + graph.distances[(min_node, neighbour)]

                # 3. If the calculated distance of the unvisited neighbour is less than the already known distance in result dictionary,
                # update the shortest distance in the result dictionary.
                if ((neighbour not in result) or (distance < result[neighbour])):
                    result[neighbour] = distance

                    # 4. If there is an update in the result dictionary,
                    # you need to update the path dictionary as well for the same key.
                    path[neighbour] = min_node

        # 5. Remove the current node from the unvisited set.
        unvisited.remove(min_node)

    return result



if __name__ == "__main__":

    """
    Set of Nodes are:  {'D', 'E', 'A', 'B', 'C'}
    Neighbours are:  defaultdict(
        <class 'list'>,
        {
            'A': ['B', 'D'],
            'B': ['A', 'D', 'E', 'C'],
            'D': ['A', 'B', 'E'],
            'E': ['B', 'C', 'D'],
            'C': ['B', 'E']
            }
    )
    Distances are:
        {
            ('A', 'B'): 3, ('B', 'A'): 3,
            ('A', 'D'): 2, ('D', 'A'): 2,
            ('B', 'D'): 4, ('D', 'B'): 4,
            ('B', 'E'): 6, ('E', 'B'): 6,
            ('B', 'C'): 1, ('C', 'B'): 1,
            ('C', 'E'): 2, ('E', 'C'): 2,
            ('E', 'D'): 1, ('D', 'E'): 1
        }
    """

    graph = Graph()
    for node in ['A', 'B', 'C', 'D', 'E', 'F']:
        graph.add_node(node)

    graph.add_edge('A','B',5)
    graph.add_edge('A','C',4)
    graph.add_edge('A','D',2)
    graph.add_edge('B','C',2)
    graph.add_edge('B','F',2)
    graph.add_edge('C','D',1)
    graph.add_edge('C','E',1)
    graph.add_edge('C','F',3)
    graph.add_edge('E','F',2)


    result = dijkstra(graph, "A")

    # result = {'B': 'A', 'C': 'D', 'D': 'A', 'F': 'C', 'E': 'C'}
    print(result)

