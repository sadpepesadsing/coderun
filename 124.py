class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None


def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root


def leaves(node, answer):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        answer.append(node.key)
    leaves(node.left, answer)
    leaves(node.right, answer)


def main():
    answer = []
    nums = list(map(int, input().split()))
    root = None
    
    for i in nums:
        if i == 0:
            break
        root = insert(root, i)
    leaves(root, answer)

    for num in answer:
        print(num)



if __name__ == '__main__':
    main()
