# https://www.acmicpc.net/problem/24465
arr = [20, 19, 21, 20, 21, 22, 23, 23, 23, 23, 23, 22] # 별자리
visited = [0] * len(arr)

for i in range(7):
    month, day = map(int, input().split())
    month -= 1
    if arr[month] > day:
        visited[month - 1] += 1
    else:
        visited[month] += 1
n = int(input())
result = []
for i in range(n):
    month_, day = map(int, input().split())
    month = month_ - 1
    if arr[month] > day:
        month -= 1
    if visited[month] > 0:  # 이미 별자리 멤버가 있다면 스킵
        continue
    else:
        result.append([month_, day])
result.sort(key=lambda x: (x[0], x[1]))
if result:
    for i in result:
        print(" ".join(map(str, i)))
else:
    print("ALL FAILED")
