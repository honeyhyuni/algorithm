def solution(clothes):
    answer = 1
    dic = {}
    for i in clothes:
        if i[1] not in dic:
            dic[i[1]] = [i[0]]
        else:
            dic[i[1]].append(i[0])
    for v in dic.values():
        answer *= len(v) + 1
    return answer - 1


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))