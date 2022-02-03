# https://www.acmicpc.net/problem/16471
n = int(input())

arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr.sort()
arr2.sort()

end = (n + 1) / 2

cnt = 0
i, k = 0, 0

while True:
    if arr[i] < arr2[k]:
        i += 1
        k += 1
        cnt += 1
    else:
        k += 1
    if k == n:
        break

if cnt >= end:
    print("YES")
else:
    print("NO")
