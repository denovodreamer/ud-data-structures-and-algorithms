from math import sqrt

from priority_queue import PriorityQueue


def distance(point_1, point_2):
    return sqrt(((point_1[0] - point_2[0])**2) + ((point_1[1] - point_2[1])**2))


class State:
    """
    Represents a given node and the costs associated with that node.
    The path instance variable is the path of intersections that leads to this state.
    The total cost is the path cost till this state, and the distance of it to the goal.
    """

    def __init__(self, intersection, map_graph, total_cost=0):
        self.intersection = intersection
        self.paths = self.get_paths(map_graph)
        self.coordinates = self.get_coordinates(map_graph)
        self.total_cost = total_cost
        self.path_cost = 0
        self.path = [intersection]

    def get_paths(self, map_graph):
        return map_graph.roads[self.intersection]

    def get_coordinates(self, map_graph):
        return map_graph.intersections[self.intersection]

    def compute_path_cost(self, previous_state):
        self.path = previous_state.path + self.path
        self.path_cost = previous_state.path_cost + distance(previous_state.coordinates, self.coordinates)

    def compute_total_cost(self, goal):
        goal_distance = distance(self.coordinates, goal.coordinates)
        self.total_cost = self.path_cost + goal_distance



def shortest_path(map_graph, start_intersection, goal_intersection):

    start = State(start_intersection, map_graph)
    goal = State(goal_intersection, map_graph)

    frontier = set()
    explored = set()

    frontier.add(start_intersection)

    queue = PriorityQueue()
    queue.insert(start)

    best_path = None

    while not queue.is_empty():

#         frontier_sorted = sorted(frontier.values(), key=lambda x: x.total_cost)
#         state = frontier_sorted.pop(0)
#         frontier = {s.intersection:s for s in frontier_sorted}

        head = queue.pop()
        state = head.state
        if state.intersection in frontier:
            frontier.remove(state.intersection)

        # Goal test
        if state.intersection == goal_intersection:
            if best_path is None or state.total_cost < best_path.total_cost:
                best_path = state

        elif state.intersection not in explored:

            explored.add(state.intersection)

            # Get new paths
            new_intersections = state.get_paths(map_graph)

            # Explore new paths
            for intersection in new_intersections:
                new_state = State(intersection, map_graph)

                # Compute cost
                new_state.compute_path_cost(state)
                new_state.compute_total_cost(goal)

                current = queue.get(intersection)

                if current is None:
                    queue.insert(new_state)

                elif new_state.total_cost < current.state.total_cost:
                    current.state = new_state

    return best_path.path

