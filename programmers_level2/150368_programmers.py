# https://school.programmers.co.kr/learn/courses/30/lessons/150368
from itertools import product


def solution(users, emoticons):
    sale = [10, 20, 30, 40]
    answer = []
    for pro in list(product(sale, repeat=len(emoticons))):
        temp = [0, 0]
        for i, j in users:
            emo = 0
            for a, b in zip(pro, emoticons):
                if i <= a:
                    emo += b - (b * a // 100)
            if emo >= j:
                temp[0] += 1
            else:
                temp[1] += emo
        answer.append(temp)

    return sorted(answer, key=lambda x:(-x[0], -x[1]))[0]


print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
