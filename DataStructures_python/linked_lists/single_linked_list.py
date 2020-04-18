class Node:
    def __init__(self, value):
        self.info = value
        self.link = None


class SingleLinkedList:
    def __init__(self):
        self.start = None

    def displaylist(self):
        if self.start is None:
            print("list is empty")
            return
        else:
            print("list is")
            p = self.start
            while p is not None:
                print(p.info, " ", end=" ")
                p = p.link
            print()

    def countnodes(self):
        p = self.start
        n = 0
        while p is not None:
            n = n + 1
            p = p.link
        print("number of nodes in the list :", n)

    def search_node(self, x):
        p = self.start
        pos = 1
        while p is not None:
            if p.info == x:
                print(x, "is at position ", pos)
                return True
            pos = pos + 1
            p = p.link
        else:
            print(x, "is not found in the list")
            return False

    def inset_in_beginning(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp

    def insert_at_end(self, data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return
        p = self.start
        while p.link is not None:
            p = p.link
        p.link = temp

    def createlist(self):
        n = int(input("enter the number nodes to insert"))
        if n == 0:
            return True
        for _ in range(n):
            data = int(input("enter the element to inert"))
            self.insert_at_end(data)

    def insert_after(self, data, x):
        p = self.start
        while p is not None:
            if p.info == x:
                break
            p = p.link
        if p is None:
            print(x, "not present i  the list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def insert_before(self, data, x):
        # if list is empty
        if self.start is None:
            print("list is empty")
            return
        # x is in first node,new node is to be inserted before first node
        if x == self.start.info:
            temp = Node(data)
            temp.link = self.start
            self.start = temp
            return
        # find referrecne to predecessor of node constainig x
        p = self.start
        while p.link is not None:
            if p.link.info == x:
                break
            p = p.link
        if p.link is None:
            print(x, "not in list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def insert_at_position(self, data, x):
        if x == 1:
            temp = Node(data)
            temp.link = self.start
            self.start = temp
            return

        p = self.start
        i = 1
        while i < x - 1 and p is not None:
            p = p.link
            i = i + 1
        if p is None:
            print("yes can insert only upto position")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def delete_first_node(self):
        if self.start is None:
            return
        self.start = self.start.link

    def delete_last_node(self):
        if self.start is None:
            return
        if self.start.link is None:
            self.start = None
            return
        p = self.start
        while p.link.link is not None:
            p = p.link
        p.link = None

    def delete_node(self, x):
        if self.start is None:
            print("list os empty")
            return
        if self.start.info == x:
            self.start = self.start.link
            return
        p = self.start
        while p.link is not None:
            if p.link.info == x:
                break
            p = p.link
        if p.link is None:
            print("element ", x, "not in list")
        else:
            p.link = p.link.link

    def reverse_list(self):
        prev = None
        p = self.start
        while p is not None:
            next = p.link
            p.link = prev
            prev = p
            p = next
        self.start = prev

    def bubble_sort_exdata(self):
        end = None
        while end != self.start.link:
            # print("end print", end)
            # print("print link", self.start.link)

            p = self.start
            while p.link != end:
                q = p.link
                if p.info > q.info:
                    p.info, q.info = q.info, p.info
                p = p.link
            end = p
        # print(end)

    def bubble_sort_exlink(self):
        pass

    def has_cycle(self):
        pass


list = SingleLinkedList()
list.createlist()

while True:
    print("1. display list")
    print("2. count the number of nodes")
    print("3. search for element")
    print("4. insert in empty list or /inser at beginnig of the list")
    print("5. insert a node at end of the list")
    print("6. insert a node after aspecified node")
    print("7. insert a node before a specified node")
    print("8. insert a node at given position")
    print("9. delete first node")
    print("10. delete last node")
    print("11. delete any node")
    print("12. reverse the list")
    print("13. bubble sort by exchanging data")
    print("14. bubble sort by exchanging links")
    print("15. merge sort")
    print("16. insert cycle")
    print("17. delete cycle")
    print("18. remove cycle")
    print("19 quit")

    option = int(input("enetr your choice : "))

    if option == 1:
        list.displaylist()
        print()
    elif option == 2:
        list.countnodes()
    elif option == 3:
        x = int(input("enter the valu to search"))
        list.search_node(x)
    elif option == 4:
        data = int(input("enter element to insert at beginig"))
        list.inset_in_beginning(data)
    elif option == 5:
        data = int(input("enter element to insert at beginig"))
        list.insert_at_end(data)
    elif option == 6:
        x, data = map(
            int,
            input(
                "enter element after which lement has to insert space data to be iserted"
            ).split(),
        )
        list.insert_after(data, x)
    elif option == 7:
        x, data = map(int, input("enter element  space data").split())
        list.insert_before(data, x)
    elif option == 8:
        x, data = map(int, input("enter position space data").split())
        list.insert_at_position(data, x)
    elif option == 9:
        list.delete_first_node()
    elif option == 10:
        list.delete_last_node()
    elif option == 11:
        data = int(input("enter element to delete"))
        list.delete_node(data)
    elif option == 12:
        list.reverse_list()
    elif option == 13:
        list.bubble_sort_exdata()
    elif option == 14:
        list.bubble_sort_exlink()
    elif option == 15:
        pass
    elif option == 16:
        pass
    elif option == 17:
        pass
    elif option == 18:
        pass
    elif option == 19:
        break
    else:
        print("wrong option")
    print()
    print()
