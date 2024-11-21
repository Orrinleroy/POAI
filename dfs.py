class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

    def dfs_recursive(self, node, visited):
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in self.graph.get(node, []):
                self.dfs_recursive(neighbor, visited)

    def dfs_iterative(self, start_node):
        visited = set()
        stack = [start_node]

        while stack:
            node = stack.pop()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                for neighbor in reversed(self.graph.get(node, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)

print("DFS (Recursive):")
g.dfs_recursive(0, set())

print("\nDFS (Iterative):")
g.dfs_iterative(0)
