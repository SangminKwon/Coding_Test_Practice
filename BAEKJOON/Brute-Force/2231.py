n = int(input())
p = 0

for i in range(1, n+1):
    temp = i
    for digit in str(i):
        temp += int(digit)

    if temp == n:
        print(i)
        p += 1
        break

if p == 0:
    print(0)
216

