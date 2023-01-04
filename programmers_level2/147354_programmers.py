# https://school.programmers.co.kr/learn/courses/30/lessons/147354
def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    for i in range(row_begin - 1, row_end):
        x = 0
        for j in data[i]:
            x += j % (i + 1)
        answer ^= x
    return answer


print(solution([[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8, 3]], 2, 2, 3))
