# https://www.acmicpc.net/problem/2947
arr = list(map(int, input().split()))

while arr != sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            print(*arr)