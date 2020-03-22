class A:
    def __init__(self):
        print("in init of A")
class B:
    def __init__(self):
        print("in init of B")
class C(B,A):
    def __init__(self):
        #super().__init__()
        print("in init of C")
        print(int.__add__(5,6))


c=C()