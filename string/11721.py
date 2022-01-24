# https://www.acmicpc.net/problem/11721
arr = input()
cnt = 0
for i in range(len(arr)):
    print(arr[i], end='')
    cnt += 1
    if cnt % 10 == 0:
        print()
