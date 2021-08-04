# 가능한 8*8 케이스를 모두 뽑아내고
# 각 케이스에서 칠해야 하는 정사각형 개수를 구해서
# 그중 최솟값을 얻는다
# 정답이 정해져있다. (맨 왼쪽 위칸이 흰색인 경우와 검은색인 경우)


def counting(test_in):

    result_1, result_2 = 0, 0


    # B로 시작
    for i, line in enumerate(test_in):
        if i % 2 == 0:
            for j, e in enumerate('BWBWBWBW'):
                if line[j] != e:
                    result_1 += 1
        else:
            for k, e in enumerate('WBWBWBWB'):
                if line[k] != e:
                    result_1 += 1
    # W로 시작
    for i, line in enumerate(test_in):
        if i % 2 == 0:
            for j, e in enumerate('WBWBWBWB'):
                if line[j] != e:
                    result_2 += 1
        else:
            for k, e in enumerate('BWBWBWBW'):
                if line[k] != e:
                    result_2 += 1

    return min(result_1, result_2)




n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(input())


cases = []
for i in range(n-7):
    for j in range(m-7):
        case = []
        for k in range(8):
            case.append(board[i:i+8][k][j:j+8])
        cases.append(case)

min_val = 9999
for case in cases:
    temp = counting(case)
    min_val = min(min_val, temp)


print(min_val)