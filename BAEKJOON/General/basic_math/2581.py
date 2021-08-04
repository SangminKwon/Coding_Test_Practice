# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

# 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

# 에라토스테네스의 체 사용
import math

m = int(input())
n = int(input())

prime_n = [k for k in range(2, n+1)]
pivot = int(math.sqrt(n))
# print(f'기본값 {pivot}')

if pivot == 1:
    prime_n.insert(0,0)


k = 2
while k <= pivot:
    if k not in prime_n: 
        k += 1
        continue

    for i, pn in enumerate(prime_n):
        if pn % k == 0 and pn != 0 and pn != k:
            prime_n[i] = 0
    k += 1


prime_n = list(set(prime_n))
prime_n.sort()

if prime_n[-1] < m:
    print(-1)
else:
    for p, pn in enumerate(prime_n):
        if pn < m:
            prime_n[p] = 0
        else:
            prime_n = list(set(prime_n))
            prime_n.sort()
            print(sum(prime_n), prime_n[1], sep='\n')
            break


