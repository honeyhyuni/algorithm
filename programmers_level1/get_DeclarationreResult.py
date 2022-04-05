# https://programmers.co.kr/learn/courses/30/lessons/92334
def solution(id_list, report, k):
    answer = []
    result = {}
    dic = {}
    for i in id_list:
        dic[i] = []
        result[i] = 0
    for i in set(report):  # 중복 신고 불가
        i = i.split()
        dic[i[0]].append(i[1])
        result[i[1]] += 1
    for j in dic.values():
        temp = 0
        for _ in j:
            if result[_] >= k:
                temp += 1
        answer.append(temp)
    return answer


print(
    solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
             2))

