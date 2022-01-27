# https://www.acmicpc.net/problem/2012
n = int(input())

arr = []
arr2 = []
for i in range(n):
    a = int(input())
    arr.append(a)
    arr2.append(i + 1)

arr.sort()

result = 0

for i in range(n):
    result += abs(arr[i] - arr2[i])

print(result)