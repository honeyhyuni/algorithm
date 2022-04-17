# https://programmers.co.kr/learn/courses/30/lessons/17677
import math


def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    arr1, arr2 = [], []

    for i in range(len(str1)-1):
        if not (65 <= ord(str1[i]) <= 90) or not (65 <= ord(str1[i + 1]) <= 90):
            continue
        arr1.append(str1[i] + str1[i+1])
    for i in range(len(str2)-1):
        if not (65 <= ord(str2[i]) <= 90) or not (65 <= ord(str2[i + 1]) <= 90):
            continue
        arr2.append(str2[i] + str2[i+1])
    gyo = set(arr1) & set(arr2)
    hap = set(arr1) | set(arr2)
    len_gyo, len_hap = 0, 0
    for i in gyo:
        len_gyo += min(arr1.count(i), arr2.count(i))
    for i in hap:
        len_hap += max(arr1.count(i), arr2.count(i))
    if len_hap == 0:
        return 65536
    return math.trunc(len_gyo / len_hap * 65536)
print(solution("France", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))
