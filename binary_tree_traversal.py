class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self, root_data):
        self.root = Node(root_data)

    def traverse(self, traverse_type):
        if traverse_type == 'preorder':
            return self.preorder(self.root)
        elif traverse_type == 'postorder':
            return self.postorder(self.root)
        elif traverse_type == 'inorder':
            return self.inorder(self.root)
        elif traverse_type == 'levelorder':
            return self.levelorder(self.root)
        else:
            return "invalid traverse type"

    def preorder(self, root):
        if root == None:
            return
        print(f"{root.data}-",end = '')
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):
        if root == None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(f"{root.data}-",end = '')

    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        print(f"{root.data}-",end = '')
        self.inorder(root.right)

    def levelorder(self, root):
        if root == None:
            return
        
        queue = Queue()
        queue.enqueue(root)
        traversal = ""

        while len(queue.items) > 0:
            traversal += str(queue.peek())
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)

            if node.right:
                queue.enqueue(node.right)

        return traversal

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

tree.traverse('preorder')
print()
tree.traverse('inorder')
print()
tree.traverse('postorder')
print()
print(tree.traverse('levelorder'))
