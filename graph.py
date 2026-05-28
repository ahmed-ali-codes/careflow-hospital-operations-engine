class HospitalGraph:
    """
    Implements a weighted, undirected graph using an adjacency list.
    No built-in graph libraries used as per the requiremnets.
    """
    def __init__(self):
         # Initialize the adjacency list to store departments and corridors
        self.adj_list = {}

    def add_department(self, name):
        # Add a new department node if it doesn't exist already
        if name not in self.adj_list:
            self.adj_list[name] = []

    def add_corridor(self, u, v, w):
        # Ensure undirected symmetry: u-v and v-u have same weight.
        if u in self.adj_list and v in self.adj_list:
            self.adj_list[u].append((v, w))
            self.adj_list[v].append((u, w))
        else:
            print("Error: Missing department.")

    def bfs_levels(self, start):
        """BFS grouping reachable departments by hops (Level 0, 1...)."""
        if start not in self.adj_list: 
            return "Error: Start not found."
        
        visited = {start}       # Set to track visited departments
        queue = [(start, 0)]    # Queue stores (department, level)
        result = {}             # Dictionary to store departments by BFS levels
        
        idx = 0
        while idx < len(queue):
            node, level = queue[idx]    # Current department and its BFS level
            idx += 1
            
            if level not in result: result[level] = []     # Initialize list for this level
            result[level].append(node)
            
            for neighbor, _ in self.adj_list[node]:     # Explore neighbors
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, level + 1))     # Next level
        return result

    def detect_cycle_dfs(self):
        """DFS to detect cycles and report involved nodes."""
       
        visited = set()     # Track visited departments
        def dfs(v, parent, path):
            visited.add(v)
            path.append(v)      # Keep track of current DFS path
            for neighbor, _ in self.adj_list[v]:
                if neighbor == parent: 
                    continue # Skip edge leading back to parent
                if neighbor in path:
                    # Cycle detected, return the part of path forming cycle
                    idx = path.index(neighbor)
                    return True, path[idx:]
                if neighbor not in visited:
                    res, cycle = dfs(neighbor, v, path)
                    if res: return True, cycle
            path.pop()    # Backtrack in DFS
            return False, []

        # Check each disconnected component of the graph
        for node in self.adj_list:
            if node not in visited:
                found, nodes = dfs(node, None, [])
                if found: return True, nodes
        return False, []

    def dijkstra(self, start, end):

        """Shortest path implementation based on Dijkstra's Algorithm (Wikipedia contributors, 2025).
      
        Refernece: 
         Wikipedia contributors. (2025). Dijkstra's algorithm. Retrieved March 26, 2026, from https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm 
        """
        
        if start not in self.adj_list or end not in self.adj_list: 
            return None, 0      # Return if start or end department does not exist
        
        # Initialize distances to infinity and previous node pointers
        distances = {n: float('inf') for n in self.adj_list}
        prev = {n: None for n in self.adj_list}
        distances[start] = 0
        unvisited = list(self.adj_list.keys())   # All departments are initially unvisited

        while unvisited:
            # Manual min-finding to avoid built-in min()
            curr = unvisited[0]
            for node in unvisited:
                if distances[node] < distances[curr]: 
                    curr = node
            
            if distances[curr] == float('inf') or curr == end: 
                break       # No path exists or destination reached
            unvisited.remove(curr)

             # Relaxation step: update distances to neighbors
            for neighbor, weight in self.adj_list[curr]:
                alt = distances[curr] + weight
                if alt < distances[neighbor]:
                    distances[neighbor] = alt
                    prev[neighbor] = curr

         # Reconstruct path from start to end
        path, step = [], end
        while step:
            path.insert(0, step)
            step = prev[step]
        # Return None if end is unreachable
        return (path, distances[end]) if distances[end] != float('inf') else (None, 0)