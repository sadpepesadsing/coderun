import sys

class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None


def insert(root, key):
    if root == None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root


def height(node):
    if node == None:
        return 0
    left = height(node.left)
    right = height(node.right)
    return max(left, right) + 1


def main():
    nums = list(map(int, input().split()))
    root = None
    for i in nums:
        if i == 0:
            break
        root = insert(root, i)
    print(height(root))



if __name__ == '__main__':
    main()
