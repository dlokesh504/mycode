class A:
    def myfun(self):
        print("in class A")
class B(A):
    def mufunb(self):
        print("in classB")
b=B()
b.myfun()
b.mufunb()