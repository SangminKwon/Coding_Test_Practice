# 주어진 N개 중에서 소수가 몇 개인지 찾아서 출력

n = int(input())
nums = list(map(int, input().split()))

result = 0
for num in nums:
    check = 1
    if num >= 3:
        for i in range(2, num):
            if num % i == 0:
                check -= 1
                break
    else:
        if num == 1:
            check -= 1
    if check:
        result += 1

print(result)