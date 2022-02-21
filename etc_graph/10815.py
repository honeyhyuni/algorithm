# https://www.acmicpc.net/problem/10815
def binary_search(a, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == target:
            return 1
        elif a[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0


n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()


for i in range(len(b)):
    print(binary_search(a, b[i], 0, n-1), end=' ')