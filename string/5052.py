# https://www.acmicpc.net/problem/5052
T = int(input())
for t in range(T):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(str(input()))
    arr.sort()
    for i in range(len(arr)-1):
        if len(arr[i]) > len(arr[i+1]):
            continue
        if arr[i] == arr[i+1][:len(arr[i])]:
            print("NO")
            break
    else:
        print("YES")