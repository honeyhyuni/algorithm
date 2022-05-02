# https://programmers.co.kr/learn/courses/30/lessons/12979
def solution(n, stations, w):
    answer = 0
    arr = [[-1, 0]]
    for i in stations:
        x, y = i-w, i+w
        if i - w < 0:
            x = 0
        if i + w > n:
            y = n
        arr.append([x, y])
    arr.append([n+1, n+1])
    stack = [0]
    for i in range(len(arr)):
        temp = arr[i][0] - stack[-1] -1
        if temp > 0:
            a, b = divmod(temp, w*2+1)
            if b > 0:
                answer += a + 1
            else:
                answer += a
        stack.append(arr[i][1])
    return answer


print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))