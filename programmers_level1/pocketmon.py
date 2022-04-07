# https://programmers.co.kr/learn/courses/30/lessons/1845
def solution(nums):
    len_ = len(nums)
    if len(set(nums)) > len_ // 2:
        return len_ // 2
    else:
        return len(set(nums))


print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))
