# https://www.acmicpc.net/problem/1920
def binary_search(array, target, start, end):   # 이분탐색 기초문제
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
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
    start = 0
    end = n - 1
    print(binary_search(a, b[i], start, end))