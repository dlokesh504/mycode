class EmptyStackError(Exception):
    pass


class StackFullError(Exception):
    pass


class Stack:
    def __init__(self, max=10):
        self.items = [None] * max
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def isfull(self):
        return self.count == len(self.items)

    def size(self):
        return self.count

    def push(self, x):
        if self.isfull():
            raise StackFullError("stack is full , can not pust")

        self.items[self.count] = x
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise EmptyStackError("stack is empty")
        x = self.items[self.count - 1]
        self.items[self.count - 1] = None
        self.count -= 1
        return x

    def peek(self):
        if self.is_empty():
            raise EmptyStackError("stack is empty")
        return self.items[self.count - 1]

    def display(self):
        print(self.items)


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
