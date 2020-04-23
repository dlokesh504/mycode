class EmptyQueueError(Exception):
    pass


class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def insert_front(self, value):
        self.items.insert(0, value)

    def inset_rear(self, value):
        self.items.append(value)

    def delete_front(self):
        if self.is_empty():
            raise EmptyQueueError("queue is empty")
        return self.items.pop(0)

    def delete_rear(self):
        if self.is_empty():
            raise EmptyQueueError("queue is empty")
        return self.items.pop()

    def first(self):
        if self.is_empty():
            raise EmptyQueueError("queue is empty")
        return self.items[0]

    def last(self):
        if self.is_empty():
            raise EmptyQueueError("queue is empty")
        return self.items[-1]

    def display(self):
        print(self.items)


if __name__ == "__main__":

    qu = Deque()
    while True:
        print("1.insert at the front")
        print("2. insert at rare")
        print("3. delete from front")
        print("4. delete from the rear")
        print("5. display first element")
        print("6. display last element")
        print("7. display")
        print("8. size")
        print("9.  exit")

        option = int(input("enter the option"))

        if option == 1:
            x = int(input("enter the element "))
            qu.insert_front(x)
        elif option == 2:
            x = int(input("enter the element "))
            qu.inset_rear(x)
        elif option == 3:
            x = qu.delete_front()
            print("poped element is ", x)
        elif option == 4:
            x = qu.delete_rear()
            print("poped element is ", x)
        elif option == 5:
            print("first element is", qu.first())
        elif option == 6:
            print("lastelement is ", qu.last())
        elif option == 7:
            qu.display()
        elif option == 8:
            print("size of que is ", qu.size())
        elif option == 9:
            break
        else:
            print("wrong oprion")

        print()
        print()
