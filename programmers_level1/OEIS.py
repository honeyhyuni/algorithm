# https://programmers.co.kr/learn/courses/30/lessons/12977
def solution(nums):
    answer = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                temp = nums[i] + nums[j] + nums[k]
                if temp > 2:
                    for _ in range(2, temp // 2 + 1):
                        if temp % _ == 0:
                            break
                    else:
                        answer += 1

    return answer


print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))
