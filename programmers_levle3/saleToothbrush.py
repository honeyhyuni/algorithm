# https://programmers.co.kr/learn/courses/30/lessons/77486
def solution(enroll, referral, seller, amount):
    dic = {}
    money = {}
    for i, j in zip(enroll, referral):
        dic[i] = j
        money[i] = 0
    for i, j in zip(seller, amount):
        child = i
        parent = dic[i]
        temp = j * 100
        money[child] += temp
        while True:
            s = temp // 10
            money[child] -= s
            if dic[child] == "-" or temp == 0:
                break
            money[parent] += s
            child = parent
            parent = dic[child]
            temp = s
    return list(money.values())


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))