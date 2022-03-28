import sys

input = sys.stdin.readline
n = int(input())
dic = {}
for i in range(n):
    a = list(map(str, input().split()))
    dic[a[0]] = a[1:]


def preorder(root):  # 전위
    if root != ".":
        print(root, end='')
        preorder(dic[root][0])
        preorder(dic[root][1])


def inorder(root):  # 중위
    if root != ".":
        inorder(dic[root][0])
        print(root, end='')
        inorder(dic[root][1])


def postorder(root):  # 후위
    if root != ".":
        postorder(dic[root][0])
        postorder(dic[root][1])
        print(root, end='')


preorder("A")
print()
inorder("A")
print()
postorder("A")
