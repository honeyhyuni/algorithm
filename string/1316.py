# https://www.acmicpc.net/problem/1316
n = int(input())
for _ in range(n):
    arr = input()
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]: # 연속된 문자중 다른 문자가 나왔을경우
            if arr[i] in arr[i+1:]: # 그뒤 문자열에 확인 여부
                n -= 1
                break

print(n)