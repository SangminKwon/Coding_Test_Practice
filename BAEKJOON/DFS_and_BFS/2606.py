def dfs(graph, s, visited):
    visited[s] = True

    for neighbor in graph[s]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)
    


n_com = int(input())
n_pair = int(input())
graph = [list() for _ in range(n_com+1)]
visited = [False] * (n_com + 1)

for i in range(n_pair):
    node_1, node_2 = map(int, input().split())
    graph[node_1].append(node_2)
    graph[node_2].append(node_1)


dfs(graph, 1, visited)
print(visited.count(True)-1)