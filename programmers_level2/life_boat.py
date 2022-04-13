from collections import deque


def solution(people, limit):
    answer = 0
    q = deque(sorted(people))
    while len(q) > 1:
        if q[0] + q[-1] <= limit:
            q.popleft()
            q.pop()
            answer += 1
        elif q[0] + q[-1] > limit:
            q.pop()
            answer += 1

    return answer + len(q)


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
