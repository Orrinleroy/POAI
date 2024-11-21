from heapq import heappop, heappush

def a_star(graph, start, goal, heuristic):
    open_set = []
    heappush(open_set, (0, start))

    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic[start]

    came_from = {}

    while open_set:
        _, current = heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  

        for neighbor, cost in graph[current]:
            tentative_g_score = g_score[current] + cost

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic[neighbor]
                heappush(open_set, (f_score[neighbor], neighbor))

    return None  

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('E', 1)],
    'D': [('F', 2)],
    'E': [('F', 2)],
    'F': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 2,
    'F': 0
}

start = 'A'
goal = 'F'

path = a_star(graph, start, goal, heuristic)
print("Shortest path:", path)
