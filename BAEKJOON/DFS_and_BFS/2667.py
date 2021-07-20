n = int(input())
graph = []
count = 0
apa_list = []

for _ in range(n):
    graph.append(list(map(int, list(input()))))



def dfs_apa(x, y):
    global count
    if x < 0 or y < 0 or x > n-1 or y > n-1:
        return 0

    if graph[x][y]:
        graph[x][y] = 0
        count += 1

        dfs_apa(x-1, y)
        dfs_apa(x+1, y)
        dfs_apa(x, y-1)
        dfs_apa(x, y+1)
       
        return count
    else:
        return 0


for i in range(n):
    for j in range(n):
        result = dfs_apa(i, j)
        if result > 0:
            apa_list.append(result)
            count = 0

print(len(apa_list))
apa_list.sort()
for apa in apa_list:
    print(apa)

