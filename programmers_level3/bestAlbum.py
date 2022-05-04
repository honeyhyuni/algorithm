# https://programmers.co.kr/learn/courses/30/lessons/42579
def solution(genres, plays):
    answer = []
    dic = {}
    total_dic = {}
    cnt = 0
    for i, j in zip(genres, plays):
        if i not in dic:
            dic[i] = [[j, cnt]]
            total_dic[i] = j
        else:
            dic[i].append([j, cnt])
            total_dic[i] += j
        cnt += 1
    print(dic)
    for key in dic.keys():
        dic[key].sort(key=lambda x: (-x[0], x[1]))
    for i, j in sorted(total_dic.items(), key=lambda x: x[1], reverse=True):
        c = 0
        for _ in dic[i]:
            if c == 2:
                break
            answer.append(_[1])
            c += 1

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
