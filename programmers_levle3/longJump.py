# https://programmers.co.kr/learn/courses/30/lessons/12914
def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    dp = [0] * n
    dp[0], dp[1] = 1, 2
    for i in range(2, n):
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567
    return dp[-1]


print(solution(4))
print(solution(3))