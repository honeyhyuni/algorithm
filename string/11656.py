# https://www.acmicpc.net/problem/11656
S = input()
result = []
for i in range(len(S)):
    result.append(S[i:])
print("\n".join(sorted(result)))