# https://www.acmicpc.net/problem/1436
n = int(input())
cnt = 0
T_six = 666

while True:
    if '666' in str(T_six):
        cnt += 1
    if cnt == n:
        print(T_six)
        break
    T_six += 1

