class EmptyQueueError(Exception):
    pass


class Node:
    def __init__(self, value):
        self.info = value
        self.link = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size_queue = 0

    def is_empty(self):
        return self.front == None

    def size(self):
        return self.size_queue

    def enqueue(self, value):
        temp = Node(value)
        if self.front == None:
            self.front = temp
        else:
            self.rear.link = temp
        self.rear = temp
        self.size_queue += 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("queue is empty")

        x = self.front.info
        self.front = self.front.link
        self.size_queue -= 1
        return x

    def peek(self):
        if self.is_empty:
            raise EmptyQueueError("queue is empty")

        print(self.front.info)

    def display(self):
        if self.is_empty():
            raise EmptyQueueError("queue is empty")

        print("queue is :")

        p = self.front
        while p is not None:
            print(p.info)
            p = p.link

        print()


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
