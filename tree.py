class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data)

# 广度优先遍历
def breadth_travel(root):
    """利用队列实现树的层次遍历"""
    if root == None:
        return
    queue = []
    queue.append(root)
    while queue:
        node = queue.pop(0)
        print(node.data)
        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)


root = Node(10)
root.left = Node(34)
root.right = Node(89)
root.left.left = Node(45)
root.left.right = Node(50)


print("前序遍历")
preorder(root)
print("中序遍历")
inorder(root)
print("后序遍历")
postorder(root)
print("广度遍历")
breadth_travel(root)