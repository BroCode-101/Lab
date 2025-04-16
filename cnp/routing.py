import sys

def dijkstra(graph, src):
    V = len(graph) 
    dist = [sys.maxsize] * V
    dist[src] = 0
    visited = [False] * V

    for _ in range(V):
        u = min((v for v in range(V) if not visited[v]), key=lambda v: dist[v], default=-1)
        visited[u] = True

        for v in range(V):
            if graph[u][v] and not visited[v]:
                dist[v] = min(dist[v], dist[u] + graph[u][v])

    print("Vertex\tDistance from Source")
    for i in range(V):
        print(f"{i}\t{dist[i]}")


graph = [
    [0, 10, 0, 0, 0, 11],
    [10, 0, 18, 0, 0, 0],
    [0, 18, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 0],
    [0, 0, 0, 9, 0, 4],
    [11, 0, 0, 0, 4, 0]
]

dijkstra(graph, 0)
