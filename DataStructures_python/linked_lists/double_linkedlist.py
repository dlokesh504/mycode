class Node(object):
    def __init__(self, value):
        self.info = value
        self.prev = None
        self.next = None


class DoubleLinkedList(object):
    def __init__(self):
        self.start = None

    def createlist(self):
        pass

    def display(self):
        if self.start is None:
            print("list is empty")
            return
        else:
            print("list is")
            p = self.start
            while p is not None:
                print(p.info, " ", end=" ")
                p = p.next
            print()

    def insert_in_beginning(self, data):
        temp = Node(data)
        temp.next = self.start
        self.start.prev = temp
        self.start = temp

    def insert_in_empty_list(self, data):
        temp = Node(data)
        self.start = temp

    def inser_at_end(self, data):
        temp = Node(data)
        p = self.start
        while p.next is not None:
            p = p.next
        p.next = temp
        temp.prev = p

    def create_list(self):
        n = int(input("enter number of nodes : "))
        if n == 0:
            return
        data = int(input(" enter the first element to br inserted"))
        self.insert_in_empty_list(data)
        for i in range(n - 1):
            data = int(input(" enter the next element to br inserted"))
            self.inser_at_end(data)

    def insert_after(self, data, x):
        temp = Node(data)
        p = self.start
        while p is not None:
            if p.info == x:
                break
            p = p.next
        if p is None:
            print(x, "is not present in list")
        else:
            temp.prev = p
            temp.next = p.next
            if p.next is not None:
                p.next.next.prev  # should not be done when p refers to laste node
            p.next = temp

    def insert_before(self, data, x):
        if self.start is None:
            print("list is empty")
            return

        if self.start.info == x:
            temp = Node(data)
            temp.next = self.start
            self.start.prev = temp
            self.start = temp
        p = self.start
        while p is not None:
            if p.info == x:
                break
            p = p.next
        if p is None:
            print(x, "not present in the list")
        else:
            temp = Node(data)
            temp.prev = p.prev
            temp.next = p
            p.prev.next = temp
            p.prev = temp

    def delete_first_node(self):
        if self.start is None:
            return
        if self.start.next is None:
            self.start = None
            return
        self.start = self.start.next
        self.start.prev = None

    def delete_last_node(self):
        if self.start is None:
            return
        if self.start.next is None:
            self.start = None
            return

        p = self.start
        while p.next != None:
            p = p.next
        p.prev.next = None

    def delete_node(self, x):
        if self.start is None:
            return
        if self.start.next is None:
            if self.start.info == x:
                self.start = None
            else:
                print(x, "not found")

        if self.start.info == x:
            self.start = self.start.next
            self.start.prev = None
            return

        p = self.start
        while p.next is not None:
            if p.info == x:
                break
            p = p.next

        if p.next is not None:
            p.prev.next = p.next
            p.next.prev = p.prev
        else:
            if p.info == x:
                p.prev.next = None
            else:
                print(x, "is not found")


list = DoubleLinkedList()
list.create_list()

while True:
    print("1.display list")
    print("2.insert in emplty list")
    print("3.insert a node at beggining of the list")
    print("4.insert a node at end of the list")
    print("5.insert a node after a specified node")
    print("6. insert a node before a specified node")
    print("7. Delete first done")
    print("8. Delte last node")
    print("9. Delete any node")
    print("10. reverse the list")
    print("11. Quit")

    option = int(input("plase enter option"))
    if option == 1:
        list.display()
    elif option == 2:
        data = int(input("enter the element to insert"))
        list.insert_in_empty_list(data)
    elif option == 3:
        data = int(input("enter the element to insert"))
        list.insert_in_beginning(data)

    elif option == 4:
        data = int(input("enter the element to insert"))
        list.inser_at_end(data)
    elif option == 5:
        data = int(input("enter the element to insert"))
        x = int(input("enter node position"))
        list.insert_after(data, x)
    elif option == 6:
        data = int(input("enter the element to insert"))
        x = int(input("enter node position"))
        list.insert_before(data, x)
    elif option == 7:
        list.delete_first_node()
    elif option == 8:
        list.delete_last_node()
    elif option == 9:
        data = int(input("enter the element to delete"))
        list.delete_node(data)
    elif option == 10:
        pass
    elif option == 11:
        break
    else:
        print("wrong option")
