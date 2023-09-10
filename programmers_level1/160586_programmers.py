import sys


def solution(keymap, targets):
    answer = []
    alphabet = [sys.maxsize] * 26

    for key in keymap:
        for k in range(len(key)):
            alpha = ord(key[k])-65
            alphabet[alpha] = min(alphabet[alpha], k+1)

    for target in targets:
        cnt = 0
        for t in range(len(target)):
            tar = ord(target[t])-65
            cnt += alphabet[tar]
        if cnt < sys.maxsize:
            answer.append(cnt)
        else:
            answer.append(-1)
    return answer


print(solution(["ABACD", "BCEFD"], ["ABCD","AABB"]))
print(solution(["AA"], ["B"]))
print(solution(["AGZ", "BSSS"], ["ASA","BGZ"]))
print(solution(["A", "AB", "B"], ["B"]))
print(solution(["ABCE"], ["ABDE"]))