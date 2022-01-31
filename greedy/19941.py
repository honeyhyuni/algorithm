# https://www.acmicpc.net/problem/19941
n, k = map(int, input().split())
arr = list(map(str, input()))

cnt = 0
for i in range(len(arr)):
    if arr[i] == "P":
        for _ in range(i-k, i+k+1):
            if 0 <= _ < n and arr[_] == "H":
                cnt += 1
                arr[_] = 0 # 한번 만난 H 를 방문처리
                break
print(cnt)
