


import math
from queue import PriorityQueue


def heuristic_measure(start, goal):
    return math.sqrt(((start[0] - goal[0]) ** 2) + ((start[1] - goal[1]) ** 2))


def generate_path(previous, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = previous[current]
        path.append(current)
    path.reverse()
    return path


def shortest_path(graph, start, goal):
    path_queue = PriorityQueue()
    path_queue.put(start, 0)

    previous = {start: None}
    score = {start: 0}

    while not path_queue.empty():
        current = path_queue.get()
        if current == goal:
            generate_path(previous, start, goal)

        for node in graph.roads[current]:
            update_score = score[current] + heuristic_measure(
                graph.intersections[current],
                graph.intersections[node]
            )

            if node not in score or update_score < score[node]:
                score[node] = update_score
                totalScore = update_score + heuristic_measure(
                    graph.intersections[current], graph.intersections[node])
                path_queue.put(node, totalScore)
                previous[node] = current

    return generate_path(previous, start, goal)


