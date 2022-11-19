class node:
    def __init__(self,num):
        self.num = num
        self.left = None
        self.right = None
        self.leave = []
        self.ch = []
        self.par = []
        self.sib = []

    def insert(self,num):
        if num > self.num:
            if self.right == None:
                self.right = node(num)
            else:
                self.right.insert(num)
        elif num < self.num:
            if self.left == None:
                self.left = node(num)
            else:
                self.left.insert(num)

    def delete(self,root,num):

        if root is None:
            return root

        if num < root.num:
            root.left = node.delete(self, root.left, num)
            return root

        elif (num > root.num):
            root.right = node.delete(self, root.right, num)
            return root

        if root.left is None and root.right is None:
            return None

        if root.left is None:
            return root.right

        elif root.right is None:
            return root.left

    def height(self,root):
        if root == None:
            return 0
        left = node.height(self,root.left)
        right = node.height(self,root.right)
        return max(left,right) + 1

    def parent(self,root):
        if root == None:
            return 0
        if root.left != None or root.right != None:
            self.par.append(root.num)
        node.parent(self,root.left)
        node.parent(self,root.right)
        return self.par

    def child(self,root):
        if root == None:
            return 0
        if root.left == None and root.right != None:
            self.ch.append(root.right.num)
        elif root.left != None and root.right == None:
            self.ch.append(root.left.num)
        elif root.left != None and root.right != None:
            self.ch.append(root.left.num)
            self.ch.append(root.right.num)
        node.child(self,root.left)
        node.child(self,root.right)
        return self.ch

    def leaves(self,root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            self.leave.append(root.num)
        node.leaves(self,root.left)
        node.leaves(self,root.right)
        return self.leave

    def sibling(self,root):
        if root == None:
            return 0
        if root.left != None and root.right != None:
            self.sib.append((root.left.num,root.right.num))
        node.leaves(self,root.left)
        node.leaves(self,root.right)
        return self.sib

    def show(self,root,space=0,LEVEL_SPACE=7):
        if (root == None):
            return
        space += LEVEL_SPACE
        node.show(self, root.right, space)
        for i in range(LEVEL_SPACE, space):
            print(end=" ")
        print("|" + str(root.num) + "|<")
        node.show(self, root.left, space)


root = node(50)
root.insert(25)
root.insert(75)
root.insert(30)
root.insert(60)
root.insert(40)
print("maximum height is: ",root.height(root))
print("parent is: ",root.parent(root))
print("Child is: ",root.child(root))
print("Leaves is: ",root.leaves(root))
print("Sibling is: ",root.sibling(root))

print("------Binary tree------")
root.show(root)
print("---------Delete--------")
root.delete(root,30)
root.delete(root,75)
root.delete(root,40)
root.show(root)
print("-----------------------")

