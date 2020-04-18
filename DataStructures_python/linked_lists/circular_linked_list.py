class Node(object):
    def __init__(self, value):
        self.info = value
        self.link = None


class CircularLinkedList(object):
    def __init__(self):
        self.last = None

    def display_list(self):
        if self.last == None:
            print("List is empty")
            return
        p = self.last.link

        while True:
            print(p.info, "", end="")
            p = p.link
            if p == self.last.link:
                break
        print()

    def insert_beginning(self, data):
        temp = Node(data)
        temp.link = self.last.link
        self.last.link = temp

    def insert_in_empty_list(self, data):
        temp = Node(data)
        self.last = temp
        self.last.link = self.last

    def insert_at_end(self, data):
        temp = Node(data)
        temp.link = self.last.link
        self.last.link = temp
        self.last = temp

    def create_list(self):
        n = int(input("enter the number of nodes"))
        if n == 0:
            return
        data = int(input("enter the element to insert"))
        self.insert_in_empty_list(data)

        for i in range(n - 1):
            data = int(input("enter the element to insert"))
            self.insert_at_end(data)

    def insert_after(self, data, x):
        p = self.last.link
        while True:
            if p.info == x:
                break
            p = p.link
            if p == self.last.link:
                break
        if p == self.last.link and p.info != x:
            print(x, " not present in the list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp
            if p == self.last:
                self.last = temp


list = CircularLinkedList()
list.create_list()

while True:
    print("1. Display list")
    print("2. insert in empty list")
    print("3. insert a node in the beginning of the list")
    print("4. insert a node at end of the list")
    print("5. insert a node after a specified node")
    print("6. delete first node")
    print("7.delete last node ")
    print("8. delete any node")
    print("9. Quit")

    option = int(input("enter your choice..."))

    if option == 1:
        list.display_list()
    elif option == 2:
        data = int(input("enter element to insert"))
        list.insert_in_empty_list(data)
    elif option == 3:
        data = int(input("enter element to insert"))
        list.insert_beginning(data)
    elif option == 4:
        data = int(input("enter element to insert"))
        list.insert_at_end(data)
    elif option == 5:
        data = int(input("enter element to insert"))
        x = int(input("enter elemet after which to insert"))
        list.insert_after(data, x)
    elif option == 6:
        pass
    elif option == 7:
        pass
    elif option == 8:
        pass
    elif option == 9:
        break
    else:
        print("wrong option")
