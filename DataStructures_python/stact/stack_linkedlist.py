class EmptyStackError(Exception):
    pass


class Node:
    def __init__(self, value):
        self.info = value
        self.link = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top == None

    def size(self):
        if self.is_empty():
            return 0
        count = 0
        p = self.top
        while p is not None:
            count += 1
            p = p.link
        return count

    def push(self, data):
        temp = Node(data)
        temp.link = self.top
        self.top = temp

    def pop(self):
        if self.is_empty():
            raise EmptyStackError("stack is empty")
        popped = self.top.info
        self.top = self.top.link
        return popped

    def peek(self):
        if self.is_empty():
            raise EmptyStackError("stack is empty")
        return self.top.info

    def display(self):
        if self.is_empty():
            print("stack is empty")

            return

        print("stack is :")
        p = self.top
        while p is not None:
            print(p.info, " ")
            p = p.link


if __name__ == "__main__":
    st = Stack()
    while True:
        print("1. push")
        print("2. pop")
        print("3. peek")
        print("4. size")
        print("5. display")
        print("6. quit")

        option = int(input("enter the option"))

        if option == 1:
            x = int(input("enter the element to be pushed"))
            st.push(x)
        elif option == 2:
            x = st.pop()
            print("poped element is ", x)

        elif option == 3:
            print("element at the top is : ", st.peek())

        elif option == 4:
            print("size of stack is :", st.size())
        elif option == 5:
            st.display()

        elif option == 6:
            break
        else:
            print("wrong oprion")

        print()
        print()
