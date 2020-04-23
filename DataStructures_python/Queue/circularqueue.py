class EmptyQueueError(Exception):
    pass


class Queue:
    def __init__(self, size=10):
        self.items = [None] * size
        self.front = 0
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def enqueue(self, value):
        i = (self.front + self.count) % len(self.items)
        self.items[i] = value
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("queue is empty")
        x = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % len(self.items)
        self.count -= 1
        return x

    def peek(self):
        if self.is_empty():
            raise EmptyQueueError("queue is empty")
        return self.items[self.front]

    def display(self):
        print(self.items)


if __name__ == "__main__":

    qu = Queue()
    while True:
        print("1. Enqueue")
        print("2. dequeue")
        print("3. peek")
        print("4. size")
        print("5. display")
        print("6. quit")

        option = int(input("enter the option"))

        if option == 1:
            x = int(input("enter the element to be pushed"))
            qu.enqueue(x)
        elif option == 2:
            x = qu.dequeue()
            print("poped element is ", x)

        elif option == 3:
            print("element at the top is : ", qu.peek())

        elif option == 4:
            print("size of stack is :", qu.size())
        elif option == 5:
            qu.display()

        elif option == 6:
            break
        else:
            print("wrong oprion")

        print()
        print()
