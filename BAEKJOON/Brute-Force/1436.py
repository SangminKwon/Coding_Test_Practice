# 종말의 숫자 666을 체킹하기
# N번쨰로 작은 종말의 숫자 찾기

n = int(input())
i = 0
k = 666

while True:
    if '666' in str(k):
        i += 1
        if i == n:
            break
    k += 1
print(k)
        