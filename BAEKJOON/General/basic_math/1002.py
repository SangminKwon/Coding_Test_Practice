import math

t = int(input())
cases = []
results = []

for i in range(t):
    cases.append(list(map(int, input().split())))

for case in cases:
    x_1 , y_1, r_1, x_2, y_2, r_2 = case[0], case[1], case[2], case[3], case[4], case[5]
    d = math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)

    if d > 0 :
        if d > r_1 + r_2 or d < abs(r_1 - r_2):
            results.append(0)
        elif d == r_1 + r_2 or d == abs(r_1 - r_2):
            results.append(1)
        elif abs(r_1 - r_2) < d and d < r_1 + r_2:
            results.append(2)
    else:
        if abs(r_1-r_2):
            results.append(0)
        else:
            results.append(-1)

for result in results:
    print(result)

