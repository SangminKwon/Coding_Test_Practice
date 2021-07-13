from collections import deque

def dfs(graph, s, visited):
    visited[s] = True
    print(s, end = " ")

    for i in graph[s]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, s, visited):
    queue = deque([s])
    visited[s] = True

    while queue:

        v = queue.popleft()
        print(v, end = ' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



n, m , start = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

for _ in range(m):
    n_1, n_2 = map(int, input().split())
    graph[n_1].append(n_2)
    graph[n_2].append(n_1)

for adj_list in graph:
    if adj_list:
        adj_list.sort()

dfs(graph, start, visited=visited_dfs)
print()

bfs(graph, start, visited=visited_bfs)




