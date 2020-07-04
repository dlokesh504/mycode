from collections import deque

class Node:
    def __init__(self,value):
        self.info = value
        self.lchild=None
        self.rchild=None

class Binarytree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root==None
    def display(self):
        self._display(self.root,0)
        print()
    def _display(self,p,level):
        if p is None:
            return
        self._display(p.rchild,level+1)
        print()
        for i in range(level):
            print("  ",end="")
        print(p.info)
        self._display(p.lchild,level+1)
    def preorder(self):
        self._preorder(self.root)
        print()

    def _preorder(self,p):
        if p is None:
            return
        print(p.info," ",end=" ")
        self._postorder(p.lchild)
        self._preorder(p.rchild)

    def inorder(self):
        self._inorder(self.root)
        print()
    def _inorder(self,p):
        if p is None:
            return
        self._inorder(p.lchild)
        print(p.info," ",end=" ")
        self._inorder(p.rchild)
    def postorder(self):
        self._postorder(self.root)
        print()
    def _postorder(self,p):
        if p is None:
            return
        self._postorder(p.lchild)
        self._postorder(p.rchild)
        print(p.info," ",end=" ")



    def levelorder(self):
        if self.root is None:
            print("Tree is empty")
            return

        dq = deque()
        dq.append(self.root)

        while len(dq)!=0:
            p = dq.popleft()
            print(p.info +" ",end=" ")
            if p.lchild is not None:
                dq.append(p.lchild)
            if p.rchild is not None:
                dq.append(p.rchild)



    def height(self):
        return self._height(self.root)

    def _height(self,p):
        if p is None:
            return  0
        hl = self._height(p.lchild)
        hr = self._height(p.rchild)

        if hl>hr:
            return  1 + hl
        else:
            return 1 + hr

    def create_tree(self):
        self.root=Node("p")
        self.root.lchild=Node("q")
        self.root.rchild=Node("r")
        self.root.lchild.lchild=Node("A")
        self.root.lchild.rchild = Node("B")
        self.root.rchild.lchild = Node("x")



bt = Binarytree()

bt.create_tree()

bt.display()
print()

print("preorder")
bt.preorder()
print("")

print("inorder")
bt.inorder()
print()

print("postorder")
bt.postorder()
print()

print("level order")
bt.levelorder()
print()

print("height of the tree is",bt.height())