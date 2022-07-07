# https://www.acmicpc.net/problem/5639
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def postorder(start, end):
    if start > end:
        return
    root = tree[start]
    idx = start + 1
    while idx <= end:
        if tree[idx] > root:
            break
        idx += 1

    # 왼쪽 서브트리
    postorder(start+1, idx-1)
    # 오른쪽 서브트리
    postorder(idx, end)
    print(root)


tree = []
while True:
    try:
        tree.append(int(input()))
    except:
        break
postorder(0, len(tree)-1)