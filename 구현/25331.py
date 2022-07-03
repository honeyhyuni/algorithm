# https://www.acmicpc.net/problem/25331
import copy
import sys

input = sys.stdin.readline
arr = [list(map(int, input().split())) for i in range(7)]

k = int(input())


def play_game(temp_arr):
    while True:
        result = []
        # 시계방향으로 90도 회전한후 확인(가로,세로 둘다 체크하기 위해)
        result += update(temp_arr, 0) + update(list(map(list, zip(*temp_arr[::-1]))), 1)
        if not result:
            break
        else:
            while result:
                x, y = result.pop()
                temp_arr[x][y] = 0
        temp_arr = new_arr(temp_arr)
    return check(temp_arr)


# 가로, 세로 확인하여 x 그룹 찾고 인덱스 저장배열 return
def update(temp_arr, bo):
    pop_in = []
    for i in range(7):
        idx, c = 0, 0
        for j in range(7):
            if temp_arr[i][j] != 0:
                c += 1
            else:
                if c != 0:
                    for t in range(idx, j + 1):
                        if temp_arr[i][t] == c:
                            if not bo:
                                pop_in.append((i, t))
                            else:
                                pop_in.append((6-t, i))
                    idx, c = j+1, 0
        if c != 0:
            for t in range(idx, 7):
                if temp_arr[i][t] == c:
                    if not bo:
                        pop_in.append((i, t))
                    else:
                        pop_in.append((6 - t, i))
    return pop_in


# 배열에 남은 숫자 체크
def check(temp_arr):
    cnt = 0
    for i in range(7):
        for j in range(7):
            if temp_arr[i][j] != 0:
                cnt += 1
    return cnt


# 숫자 밑으로 이동
def new_arr(temp_arr):
    for i in range(7):
        temp = []
        for j in range(6, -1, -1):
            if temp_arr[j][i] != 0:
                temp.append((temp_arr[j][i]))
        for j in range(6, -1, -1):
            if temp:
                x = temp.pop(0)
                temp_arr[j][i] = x
            else:
                temp_arr[j][i] = 0
    return temp_arr


min_v = sys.maxsize
for i in range(7):
    for j in range(6, -1, -1):
        if arr[j][i] == 0:
            arr[j][i] = k
            min_v = min(min_v, play_game(copy.deepcopy(arr)))
            arr[j][i] = 0
            break
print(min_v)
