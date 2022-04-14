answer = 0
c = 0


def solution(word):
    result = []

    def back(cnt):
        global answer, c
        if len(result) == 6:
            return
        answer += 1
        if "".join(result) == word:
            c = answer - 1
        arr = ["A", "E", "I", "O", "U"]
        for _ in arr:
            result.append(_)
            back(cnt + 1)
            result.pop()
        return c

    return back(0)
