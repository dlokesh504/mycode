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
        elif x<p.info:
            p.lchild = self._insert(p.lchild,x)
        elif x>p.info:
            p.rchild = self._insert(p.rchild,x)
        else:
            print(x,"already present in the tree")
        return p

    def insert1(self,x):
        p = self.root
        par = None
        while p is not None:
            par = p
            if x<p.info:
                p=p.lchild
            elif x>p.info:
                p=p.rchild
            else:
                print(x," already present in the tree")
                return
        temp = Node(x)

        if par== None:
            self.root = temp
        elif x<par.info:
            par.lchild=temp
        else:
            par.rchild = temp




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

    def _delete(self,p,x):
        if p is None:
            print(x," not found")
            return p

        if x < p.info:
            p.lchild = self._delete(p.lchild,x)
        elif x>p.info:
            p.rchild = self._delete(p.rchild,x)
        else:
            #key to be deleted is found
            if p.lchild is not None and p.rchild is not None: # 2 children
                s=p.rchild
                while s.lchild is not  None:
                    s=s.lchild
                p.info = s.info
                p.rchild = self._delete(p.rchild,s.info)
            else:#1 child or no child
                if p.lchild is not None:
                    ch = p.lchild
                else:
                    ch = p.rchild
                p = ch
        return p




    def delete1(self):
        p = self.root
        par = None

        while p is not None:
            if x==p.info:
                break
            par = p
            if x < p.info:
                p = p.lchild
            else:
                p=p.rchild
        if p == None:
            print(x,"not found")
            return

        #case c : 2 cildren
        #Find inorder successor and its parent

        if p.lchild is not None and p.rchild is not None:
            ps = p
            s  =p.rchild
            while s.lchild is not None:
                ps =s
                s= s.lchild
            p.info = s.info
            p = s
            par = p

        # case B and case A : 1 or no child

        if p.lchild is not None:
            ch = p.lchild
        else:
            ch = p.rchild

        if par == None:
            self.root = ch
        elif p == par.lchild:
            par.lchild = ch
        else:
            par.rchild = ch





    def min1(self):
        if self.is_empty():
            raise TreeEmptyError("Tree is empty")
        p = self.root
        while p.lchild is not None:
            p=p.lchild
        return p.info


    def max1(self):
        if self.is_empty():
            raise TreeEmptyError("Tree is empty")
        p = self.root
        while p.rchild is not None:
            p = p.rchild
        return p.info

    def min2(self):
        if self.is_empty():
            raise TreeEmptyError("Tree is empty")
        return self._min(self.root)

    def _min(self,p):
        if p.lchild is None:
            return p
        return self._min(p.lchild)
    def max2(self):
        if self.is_empty():
            raise TreeEmptyError("Tree is empty")
        return self._max(self.root).info

    def _max(self,p):
        if p.rchild is None:
            return p
        return self._max(p.rchild)

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
