class hash:
    def __init__(self,size):
        self.cap=size
        self.lst=[None]*self.cap
        print(self.lst)

    def hash_func(self,ele):
        pos=ele%self.cap
        return pos
    def hash_table(self,ele):
        pos=self.hash_func(ele)
        if self.lst[pos] is not None:
            for i in range(self.cap-1):
                pos=((pos+i) % self.cap)
                if self.lst[pos] is None:
                    self.lst[pos]=ele
                    break
        else:
            self.lst[pos]=ele
    def display(self):
        for i in range(self.cap):
            # if self.lst[i] is not  None:
            print(self.lst[i],end=" ")


size=int(input())
obj=hash(size)
arr=[1,2,3,4,14,67]
for i in arr:
    obj.hash_table(i)
obj.display()

