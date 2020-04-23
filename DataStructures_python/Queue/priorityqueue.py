
class Node:
    def __init__(self, value, pr):
        self.info = value
        self.pri = pr
        self.link = None


class PriorityQueue:
    def __init__(self):
        self.front = None

    def is_empty(self):
        return self.front == None

    def enqueue(self, data, data_pri):
        temp = Node(data, data_pri)

        if self.is_empty() or data_pri < self.front.pri:
            temp.link = self.front
            self.front = temp
        else:
            p = self.front
            while p.link != None and p.link.pri <= data_pri:
                p = p.link

            temp.link = p.link
            p.link = temp

    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
        x = self.front.info
        self.front = self.front.link
        return x

    def display(self):
        if self.is_empty():
            print("queue is empty")
            return

        print("queue is...")
        p = self.front
        while p is not None:
            print(p.info, "  ", p.pri)
            p = p.link
        print()

    def size(self):
        n = 0
        p = self.front
        while p is not None:
            p = p.link
            n += 1
        return n


if __name__ == "__main__":
    pqu = PriorityQueue()
    while True:
        print("1. Enqueue")
        print("2. dequeue")
        print("3. diplay all queue elements")
        print("4. display size of queue")
        print("5. quit")

        option = int(input("enter the option"))

        if option == 1:
            x = int(input("enter the element to be pushed"))
            pri = int(input("enter the priority of  element to be pushed"))
            pqu.enqueue(x, pri)
        elif option == 2:
            x = pqu.dequeue()
            print("poped element is ", x)

        elif option == 3:
            pqu.display()

        elif option == 4:
            print("size of queue is :", pqu.size())

        elif option == 5:
            break
        else:
            print("wrong oprion")

        print()
        print()
