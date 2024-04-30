# n=int(input())
# li=list(map(int,input().split()))
# k=[]
# for i in range(len(li)):
#     c=0
#     for j in range(i,len(li)):
#         if li[i]>li[j]:
#             c+=1
#     k.append(c)
# print(k)

class node():
    def __init__(self,data):
        self.data=data
        self.next=None
class link():
    def __init__(self):
        self.head=None
        self.temp=None
    def create(self,data):
        Node=node(data)
        if self.head==None:
            self.head=Node
            self.temp=self.head
        else:
            self.temp.next=Node
            self.temp=self.temp.next
    def new(self):
        prev=self.head
        while prev!=None:
            curr=prev.next
            c=0
            while curr!=None:
                if prev.data > curr.data:
                    c+=1
                prev=prev.next
            obj.create(c)
            prev=prev.next
        obj.display()
    def display(self):
        self.temp=self.head
        while self.temp!=None:
            print(self.temp.data,end=" ")
            self.temp=self.temp.next


obj1=link()
n=int(input())
for i in range(n):
    obj1.create(int(input()))
obj1.display()
obj=link()
obj1.new()