# https://www.acmicpc.net/problem/1758
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

sum_v = 0
arr.sort(reverse=True) # 최댓값을 받기위해 배열 역순정렬
for i in range(n):
    result = arr[i] - (i+1 - 1)
    if result < 0:
        result = 0
    sum_v += result
print(sum_v)