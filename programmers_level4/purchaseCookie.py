# https://programmers.co.kr/learn/courses/30/lessons/49995
def solution(cookie):
    answer = 0
    n = len(cookie)
    for i in range(n - 1):
        # i 를 기준으로 좌우를 나눈다
        cookie_left, left_idx = cookie[i], i
        cookie_right, right_idx = cookie[i + 1], i + 1
        while True:
            if cookie_left == cookie_right:
                answer = max(answer, cookie_left)
            # 왼쪽 쿠키의 합이 오른쪽 쿠키의 합보다 작거나 같고 인덱스를 더 줄일수 있는 경우
            if left_idx > 0 and cookie_left <= cookie_right:
                left_idx -= 1
                cookie_left += cookie[left_idx]
            # 오른쪽 쿠키의 합이 왼쪽 쿠키의 합보다 작거나 같고 인덱스를 더 늘릴수 있는 경우
            elif right_idx < n - 1 and cookie_right <= cookie_left:
                right_idx += 1
                cookie_right += cookie[right_idx]
            else:
                break
    return answer


print(solution([1, 1, 2, 3]))
print(solution([1, 2, 4, 5]))
