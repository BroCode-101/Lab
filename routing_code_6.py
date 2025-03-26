import sys  

# Number of vertices in the graph  
V = 6  

def min_distance(dist, visited):
    """Find the vertex with the minimum distance value from the set of vertices not yet processed."""
    min_val = sys.maxsize
    min_index = -1

    for v in range(V):
        if not visited[v] and dist[v] < min_val:
            min_val = dist[v]
            min_index = v

    return min_index

def dijkstra(graph, src):
    """Implements Dijkstra's algorithm for shortest path calculation."""
    dist = [sys.maxsize] * V  # Distance from source to each vertex
    visited = [False] * V  # To track visited vertices

    dist[src] = 0  # Distance of source vertex from itself is always 0

    for _ in range(V - 1):
        u = min_distance(dist, visited)  # Get the vertex with the smallest distance
        visited[u] = True  # Mark the vertex as processed

        # Update distance values of adjacent vertices
        for v in range(V):
            if graph[u][v] and not visited[v] and dist[u] != sys.maxsize and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]

    print_solution(dist)

def print_solution(dist):
    """Prints the shortest distances from source."""
    print("Vertex\tDistance from Source")
    for i in range(V):
        print(f"{i}\t{dist[i]}")

# Graph representation as adjacency matrix
graph = [
    [0, 10, 0, 0, 0, 11],
    [10, 0, 18, 0, 0, 0],
    [0, 18, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 0],
    [0, 0, 0, 9, 0, 4],
    [11, 0, 0, 0, 4, 0]
]

# Source vertex
source = 0  

# Run Dijkstra’s Algorithm
dijkstra(graph, source)