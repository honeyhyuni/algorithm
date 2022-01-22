# https://www.acmicpc.net/problem/1292
a, b = map(int, input().split())

arr = []

i = 1
j = 1
while True: # 순열
    for _ in range(1, i+1):
        arr.append(j)
    i += 1
    j = i
    if i == 1001:
        break
# hap = 0
# for k in range(a-1, b):
#     hap += arr[k]
# print(hap)
print(sum(arr[a-1:b]))