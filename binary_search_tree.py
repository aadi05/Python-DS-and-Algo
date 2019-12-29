class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
    
class BST:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def insert(self,key):
        self.__insertNode(self.root,key)
        self.size += 1

    def __insertNode(self,root,key):
        if root == None:
            self.root = Node(key)
            return
        if key > root.data:
            #move right
            if root.right == None:
                root.right = Node(key)
                return
            else:
                self.__insertNode(root.right,key)
        else:
            #move left
            if root.left == None:
                root.left = Node(key)
                return
            else:
                self.__insertNode(root.left,key)

    def remove(self,key):
        self.__removeNode(self.root,key)
        self.size -= 1

    def __removeNode(self,root,key):
        if root == None:
            return None
        if root.data == key:
            if root.left == None and root.right == None:
                root = None
            elif root.left == None:
                temp = root.right
                root = None
                return temp
            elif root.right == None:
                temp = root.left
                root = None
                return temp
            else:
                temp = self.inorderSuccessor(root.right)
                root.data = temp.data
                root.right = self.__removeNode(root.right,temp.data)
        elif key > root.data:
            #move right
            root.right = self.__removeNode(root.right,key)
        else:
            #move left
            root.left = self.__removeNode(root.left,key)
        return root

    def inorderSuccessor(self,root):
        curr = root
        while curr.left != None:
            curr = curr.left
        return curr

    def contains(self,key):
        return self.__containsNode(self.root,key)

    def __containsNode(self,root,key):
        if root == None:
            return False
        if root.data == key:
            return True
        if key > root.data:
            #move right
            return self.__containsNode(root.right,key)
        else:
            #move left
            return self.__containsNode(root.left,key)

    def inorderTraversal(self,root):
        if root:
            self.inorderTraversal(root.left)
            print(root.data)
            self.inorderTraversal(root.right)

bst = BST()
arr = [14, 35, 30, 7, 30, 12, 29, 29, 43, 47, 27, 10, 4, 41, 20]

for item in arr:
    bst.insert(item)

bst.inorderTraversal(bst.root)
print()
bst.remove(4)

print(bst.contains(4))
print(bst.size)
print()
bst.inorderTraversal(bst.root)
