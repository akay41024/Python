# Purpose: To create a linked list and display it
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def append(self, data):
#         newnode = Node(data)
#         if self.head is None:
#             self.head = newnode
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = newnode
#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" ")
#             current = current.next
#         # print("None")

# lst = LinkedList()
# n = int(input("Enter the number of nodes: "))
# for i in range(n):
#     data = int(input("Enter the data item: "))
#     lst.append(data)
# print("The linked list: ", end=" ")
# lst.display()

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def push(self, data):
#         newnode = Node(data)
#         newnode.next = self.head
#         self.head = newnode
#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" ")
#             current = current.next


# lst = LinkedList()
# n = int(input("Enter the number of nodes: "))

# for i in range(n):
#     data = int(input(f"Enter the data {i+1} item: "))
#     lst.push(data)
# print("The linked list: ", end=" ")
# lst.display()





#Single linked list insert at position before
class Node:
    def _init_(self):
        self.data=None
        self.next=None
head=None
def append(d):#15
    global head
    newnode=Node()
    temp=head
    newnode.data=d
    newnode.next=None
    if head ==None:
        head=newnode
    else:
        while temp.next !=None:
            temp=temp.next
        temp.next=newnode
def insert(pos,ele):
    global head
    temp=head
    ptr=head
    c=0
    while ptr!=None:
        ptr=ptr.next
        c+=1
    if pos>c and pos<=0:
        print("Invalid Input")
    else:
        curr=Node()
        curr.data=ele
        curr.next=None
        i=1
        while(i<pos-1):
            temp=temp.next
            i+=1
        curr.next=temp.next
        temp.next=curr
def display():
    global head
    temp=head
    while temp!=None:
        print(temp.data,end=" ")
        temp=temp.next
if __name__=='__main__':
    d=None
    while True:
        d=int(input())
        if d>0:
            append(d)#15
        else:
            break
print("Displaying linked list:")
display()
print("Enter the position:")
pos=int(input())
print("Enter the element:")
ele=int(input())
insert(pos,ele)
print("Displaying linked list after insertion:")
display()


