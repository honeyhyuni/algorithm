# https://school.programmers.co.kr/learn/courses/30/lessons/178870
def solution(sequence, k):
    answer = []
    left, right = 0, -1
    total = 0
    while right < len(sequence):
        if total < k:
            right += 1
            if right >= len(sequence):
                break
            total += sequence[right]
        else:
            if total == k:
                answer.append([left, right, right - left])
            total -= sequence[left]
            left += 1
    return sorted(answer, key=lambda x: (x[2], x[0]))[0][:2]


print(solution([1, 2, 3, 4, 5], 7))
print(solution([1, 1, 1, 2, 3, 4, 5], 5))
print(solution([2, 2, 2, 2, 2], 6))
