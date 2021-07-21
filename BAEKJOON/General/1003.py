import time

t = int(input())
cases = []
result = {0:[1,0], 1:[0,1]}
fibo_tabul = {0:1, 1:1}


for i in range(t):
    cases.append(int(input()))

start = time.time()
for case in cases:
    if case >= 2:
        for i in range(2, case+1):
            fibo_tabul[i] = fibo_tabul[i-1] + fibo_tabul[i-2]
            result[i] = [result[i-1][0] + result[i-2][0], result[i-1][1] + result[i-2][1]]
    print(result[case][0], result[case][1])
end = time.time()

print(f'런타임 : {end-start:.3f}')