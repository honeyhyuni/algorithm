# https://www.acmicpc.net/problem/4673
dp = [-1] * 10001
i = 1
while i < 10001:
    num = 0
    if i < 10:
        num = i * 2
    else:
        num += i
        i = str(i)
        for _ in range(len(i)):
            num += int(i[_])
    i = int(i)
    if num < 10001:
        dp[num] = 0
    if dp[i] == -1:
        print(i)
    i += 1
