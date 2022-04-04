# https://programmers.co.kr/learn/courses/30/lessons/67256
def solution(numbers, hand):
    dic = {0: [3, 1], "*": [3, 0], "#": [3, 2]}
    x, y = 0, 0
    answer = ""
    for i in range(1, 10):
        dic[i] = [x, y]
        y += 1
        if y == 3:
            x += 1
            y = 0
    left, right = "*", "#"
    for i in numbers:
        if i in [1, 4, 7]:
            answer += "L"
            left = i
        elif i in [3, 6, 9]:
            answer += "R"
            right = i
        else:
            le = abs(dic[left][0] - dic[i][0]) + abs(dic[left][1] - dic[i][1])
            ri = abs(dic[right][0] - dic[i][0]) + abs(dic[right][1] - dic[i][1])
            if le > ri:
                answer += "R"
                right = i
            elif le == ri:
                if hand == "right":
                    right = i
                    answer += "R"
                else:
                    left = i
                    answer += "L"
            else:
                answer += "L"
                left = i

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))
