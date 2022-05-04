# https://programmers.co.kr/learn/courses/30/lessons/12971
def solution(sticker):
    n = len(sticker)
    if n < 4:
        return max(sticker)
    dp = [0] * n
    # 맨 첫 스티커를 뗏을경우
    dp[0] = sticker[0]
    dp[1] = sticker[0]
    for i in range(2, n-1):
        dp[i] = max(dp[i-2] + sticker[i], dp[i-1])
    answer = dp[n-2]
    # 맨 첫 스티커를 떼지 않았을 경우
    dp[0] = 0
    dp[1] = sticker[1]
    for i in range(2, n):
        dp[i] = max(dp[i-2] + sticker[i], dp[i-1])
    return max(answer, dp[n-1])


print(solution([14, 6, 5, 11, 3, 9, 2, 10]	))
print(solution([1, 3, 2, 5, 4]))