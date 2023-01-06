# https://school.programmers.co.kr/learn/courses/30/lessons/150370
def solution(today, terms, privacies):
    answer = []
    dic = {}
    for i in terms:
        i = i.split()
        dic[i[0]] = int(i[-1])
    today = list(map(int, today.split(".")))
    c = 1
    for i in privacies:
        p_month = dic[i[-1]]
        now = list(map(int, i[:-2].split(".")))
        now[-1] -= 1
        if now[-1] == 0:
            now[-1] = 28
            now[1] -= 1
        now[1] += p_month
        v, m = divmod(now[1]-1, 12)
        if v:
            now[0] += v
            now[1] = m + 1
        if today > now:
            answer.append(c)
        c += 1
    return answer


print(solution("2022.05.19", ["A 6", "B 12", "C 3"],
               ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
