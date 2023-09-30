#1.Breadth First Traversal for a Graph
from collections import defaultdict, deque
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def add_edge(self, u, v):
        self.graph[u].append(v)
    def bfs(self, start):
        visited = [False] * (max(self.graph) + 1)
        queue = deque()
        queue.append(start)
        visited[start] = True
        while queue:
            node = queue.popleft()
            print(node, end=" ")
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
start_node = 2
print("BFS traversal starting from node", start_node)
g.bfs(start_node)
#2.Depth First Traversal for a Graph
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def add_edge(self, u, v):
        self.graph[u].append(v)
    def dfs_util(self, node, visited):
        visited[node] = True
        print(node, end=" ")
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)
    def dfs(self, start):
        visited = [False] * (max(self.graph) + 1)
        self.dfs_util(start, visited)
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
start_node = 2
print("DFS traversal starting from node", start_node)
g.dfs(start_node)
#3.Count the number of nodes at given level in a tree using BFS
from collections import defaultdict, deque
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def add_edge(self, u, v):
        self.graph[u].append(v)
    def count_nodes_at_level(self, start, level):
        queue = deque([(start, 0)])
        count = 0
        while queue:
            node, current_level = queue.popleft()
            if current_level == level:
                count += 1
            if current_level > level:
                break  
            for neighbor in self.graph[node]:
                queue.append((neighbor, current_level + 1))
        return count
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)
g.add_edge(3, 7)
start_node = 1
level_to_count = int(input("Enter the level:"))
count = g.count_nodes_at_level(start_node, level_to_count)
print(f"Number of nodes at level {level_to_count}: {count}")
#4.Count number of trees in a forest
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Assuming an undirected graph
    def dfs(self, node, visited):
        visited[node] = True
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)
    def count_trees(self):
        visited = [False] * (max(self.graph) + 1)
        tree_count = 0
        for node in self.graph:
            if not visited[node]:
                self.dfs(node, visited)
                tree_count += 1
        return tree_count
g = Graph()
g.add_edge(1, 2)
g.add_edge(3, 4)
g.add_edge(5, 6)
g.add_edge(7, 8)
g.add_edge(9, 10)
g.add_edge(11, 12)
forest = g.count_trees()
print("Number of trees in the forest:", forest)
#5.Detect Cycle in a Directed Graph
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def add_edge(self, u, v):
        self.graph[u].append(v)
    def has_cycle(self):
        def dfs(node, visited, stack, parent, cycle_edges):
            visited[node] = True
            stack[node] = True
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    if dfs(neighbor, visited, stack, node, cycle_edges):
                        cycle_edges.append((node, neighbor))
                        return True
                elif stack[neighbor] and neighbor != parent:
                    cycle_edges.append((node, neighbor))
                    return True
            stack[node] = False
            return False
        num_nodes = len(self.graph)
        visited = [False] * num_nodes
        stack = [False] * num_nodes
        cycle_edges = []
        for node in range(num_nodes):
            if not visited[node]:
                if dfs(node, visited, stack, -1, cycle_edges):
                    return True, cycle_edges
        return False, []
g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
has_cycle, cycle_edges = g.has_cycle()
if has_cycle:
    print("The graph contains a cycle.")
    print("Edges in the cycle:")
    for edge in cycle_edges:
        print(edge[0], "->", edge[1])
else:
    print("The graph does not contain a cycle.")
    