# https://www.acmicpc.net/problem/12015
# LIS 알고리즘
n = int(input())
arr = list(map(int, input().split()))
lis = [0]
for a in arr:
    if lis[-1] < a:
        lis.append(a)
    else:
        left = 0
        right = len(lis)
        while left < right:
            mid = (left + right) // 2
            if lis[mid] < a:
                left = mid + 1
            else:
                right = mid
        lis[right] = a
print(len(lis) - 1)
