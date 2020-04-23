class EmptyStackError(Exception):
    pass


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.is_empty():
            raise EmptyStackError("stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise EmptyStackError("stack is empty")
        return self.items[-1]

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
