class TreeEmptyError(Exception):
    pass

class Node:
    def __init__(self):
        self.info = None
        self.lchild = None
        self.rchild = None

class BinartSearchTree:
    def __init__(self):
        self.root = None
    def is_empty(self):
        return self.root == None
    def insert(self,x):
        self.root = self._insert(self.root,x)
    def _insert(self,p,x):
        if p is None:
            p=Node(x)

    def insert1(self,x):
        pass

    def search(self,x):
        return self._search(self.root,x) is not None
    def _search(self,p,x):
        if p in None:
            return None
        if x<p.info:
            return  self._search(p.lchild,x)
        if x>p.info:
            return self._search(p.rchild,x)
        return  p


    def search1(self,x):
        p = self.root
        while p is not None:
            if x<p.info:
                p=p.lchild
            elif x>p.info:
                p=p.rchild
            else:
                return True
        return False





    def delete(self,x):
        self.root = self._delete(self.root,x)
    def _delete(selfself,p,x):
        pass

    def delete1(self):
        pass


    def min1(self):
        pass

    def max1(self):
        pass

    def min2(self):
        pass

    def _min(self,p):
        pass
    def max2(self):
        pass

    def map(self):
        pass

    def diplay(self):
        pass

    def _display(self):
        pass

    def preorder(self):
        self._preorder(self.root)
        print()
    def _preorder(self,p):
        pass

    def inorder(self):
        self._inorder(self.root)
        print()
    def _inorder(self,p):
        pass

    def postorder(self):
        self._postorder(self.root)
        print()
    def _postorder(self,p):
        pass
    def height(self):
        return self._height(self.root)

    def _height(self,p):
        pass



bst = BinartSearchTree()

while True:
    print("1.Display Tree")
    print("2.Search (Iterative)")
    print("3.search (Recursive) ")
    print("4. Insert a new node (Iterative)")
    print("5.Insert a new node (Recursive)")
    print("6. Delete a node (Iterative)")
    print("7. Delete a node (Recursive)")
    print("8. Find Minimum key (Iterative)")
    print("9. Find Minimum key (Recursive)")
    print("10. Find Maximum key (Iterative)")
    print("11. Find Maximum key (Recursive) ")
    print("12.Preorder Traversal")
    print("13. Inorder Traversal")
    print("14. Postorder Traversal")
    print("15. Height of tree")
    print("16. Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        bst.display()
    elif choice == 2:
        x = int(input("Enter the key to be searched :"))
        if bst.searchl(x):
            print("key found")
        else:
            print("Key not found")

    elif choice == 3:
        x = int(input("Enter the key to be searched :"))
        if bst.search(x):
            print("key found")
        else:
            print("key not found")
    elif choice == 4:
        x = int(input("Enter the key to be inserted : "))
        bst.insert()

    elif choice == 5:
        x = int(input("Enter the key to be inserted : "))
        bst.insert(x)
    elif choice == 6:
        x = int(input("Enter the element to be deleted :"))
        bst.delete1(x)
    elif choice == 7:
        x = int(input("Enter the element to be dele"))
        bst.delete(x)
    elif choice == 8:
        print("Minimum key is", bst.min1())
    elif choice == 9:
        print("Minimum key is ",bst.min2())
    elif choice == 10:
        print("Maximum key is",bst.max1() )
    elif choice == 11:
        print("Maximum key is ", bst.max2())
    elif choice == 12:
        bst.preorder()
    elif choice == 13:
        bst.inorder()
    elif choice == 14:
        bst.postorder()
    elif choice == 15:
        print("Height of tree is", bst.height())

    elif choice == 16:
        break

    else:
        print("Wrong choice")

    print()
