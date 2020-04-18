class Node(object):
    def __init__(self, value):
        self.info = value
        self.link = None


class HeaderLinkedList(object):
    def __init__(self):
        self.head = Node(0)

    def display_list(self):
        if self.head.link == None:
            print("list is empty")
            return

        p = self.head.link
        print("list is ....")
        while p is not None:
            print(p.info, " ", end="")
            p = p.link
        print()

    def create_list(self):
        n = int(input("enter the number of nodes :  "))
        for i in range(n):
            data = int(input("enter the elements to be inserted : "))
            self.insert_at_end(data)

    def insert_at_end(self, data):
        temp = Node(data)
        p = self.head
        while p.link is not None:
            p = p.link
        p.link = temp

    def insert_before(self, data, x):
        p = self.head
        while p.link is not None:
            if p.link.info == x:
                break
            p = p.link
        if p.link is None:
            print(x, " not present in the list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def insert_at_position(self, data, x):
        p = self.head
        i = 1
        while i <= x - 1 and p is not None:
            p = p.link
            i += 1

        if p is None:
            print("you can only upto ", (i - 1), "position")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def delete_node(self, data):
        p = self.head
        while p.link is not None:
            if p.link.info == data:
                break
            p = p.link
        if p.link == None:
            print(data, "not found")
        else:
            p.link = p.link.link

    def reverse_llist(self):
        prev = None
        p = self.head.link
        while p is not None:
            next = p.link
            p.link = prev
            prev = p
            p = next

        self.head.link = prev


list = HeaderLinkedList()
list.create_list()
while True:
    print("1. display list")
    print("2. insert a node at end of the list")
    print("3. insert a node before a specified node")
    print("4. insert a node at given position")
    print("5. delete a node")
    print("6. reverse the list")
    print("7. quit")

    option = int(input("enter  your choice.."))
    if option == 1:
        list.display_list()
    elif option == 2:
        data = int(input("enter the element to be inserted : "))
        list.insert_at_end(data)
    elif option == 3:
        data = int(input("enter the element to be inserted : "))
        x = int(input("enter the element before which to insert : "))
        list.insert_before(data, x)
    elif option == 4:
        data = int(input("enter the element to be inserted : "))
        x = int(input("enter the element at which to insert : "))
        list.insert_at_position(data, x)

    elif option == 5:
        x = int(input("enter the element before which to insert : "))
        list.delete_node(data)

    elif option == 6:
        list.reverse_llist()
    elif option == 7:
        break
    elif option >= 8:
        print("wrong input")

    print()
