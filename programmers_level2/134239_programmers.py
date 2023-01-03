# https://school.programmers.co.kr/learn/courses/30/lessons/134239
def solution(k, ranges):
    data = [0.0]
    c = 0
    while k > 1:
        c += 1
        b_k = k
        if k % 2 == 0:
            k //= 2
        else:
            k = (k * 3) + 1
        data.append(data[c-1] + (b_k + k) / 2)
    len_ = len(data) - 1
    answer = []
    for i, j in ranges:
        j += len_
        if j < i:
            answer.append(-1.0)
        else:
            answer.append(data[j] - data[i])
    return answer


print(solution(5, [[0, 0], [0, -1], [2, -3], [3, -3]]))
