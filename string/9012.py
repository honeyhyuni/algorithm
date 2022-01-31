n = int(input())
for _ in range(n):
    arr = list(input())
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == "(":
            cnt += 1
        elif arr[i] == ")":
            cnt -= 1
        if cnt < 0:
            print("NO")
            break
    if cnt > 0:
        print("NO")
    elif cnt == 0:
        print("YES")
