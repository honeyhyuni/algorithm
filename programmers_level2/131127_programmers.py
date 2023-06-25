# https://school.programmers.co.kr/learn/courses/30/lessons/131127
from collections import defaultdict


def check(want_dict, check_dict):
    for i, j in check_dict.items():
        if j == 0:
            continue
        if i in want_dict:
            if not j == want_dict[i]:
                return False
        else:
            return False

    return True


def solution(want, number, discount):
    answer = 0
    want_dict = defaultdict(int)
    for i, j in zip(want, number):
        want_dict[i] = j

    check_dict = defaultdict(int)

    for i in range(10):
        check_dict[discount[i]] += 1

    left, right = 0, 10
    while right <= len(discount):
        if check(want_dict, check_dict):
            answer += 1
        if len(discount) == right:
            break
        check_dict[discount[left]] -= 1
        check_dict[discount[right]] += 1
        left += 1
        right += 1
    return answer


print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1],
               ["chicken", "apple", "apple", "banana", "rice", "apple",
                "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
