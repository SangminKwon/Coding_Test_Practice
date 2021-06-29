n = int(input())
students = []
ranking = [0 for _ in range(n)]


for _ in range(n):
    students.append(list(map(int, input().split())))


for i in range(n):
    copy = students[:]
    copy.remove(copy[i])
    count = 0
    for element in copy:
        w, t = students[i]
        w_c = element[0]
        t_c = element[1]

        if w < w_c and t < t_c:
            count += 1
    ranking[i] = count + 1

for rank in ranking:
    print(rank, end=" ")
