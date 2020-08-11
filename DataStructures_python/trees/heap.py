class HeapEmptyError(Exception):
    pass

class Heap:
    def __init__(self,maxsize=10):
        self.a = [None]*maxsize
        self.n=0
        self.a[0]=99999

    def insert(self,value):
        self.n+=1
        self.a[self.n]=value
        self.restore_up(self.n)


    def restore_up(self,i):
        k=self.a[i]
        iparent = i//2


        while self.a[iparent] <k:
            self.a[i]=self.a[iparent]
            i = iparent
            iparent = i//2
        self.a[i] = k


