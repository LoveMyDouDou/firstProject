#coding=utf-8
#Python的内置数据结构有元组、列表、字典等

#现在有三个物品，分别是"apple","orange","pear"，需要将这三个物品存储起来

#存储方式一:这三个物品每个物品按顺序分别存储到一个柜子中，这些物品可以取出来
["apple","orange","pear"]

#存储方式二:这三个物品每个物品按顺序分别存储到一个柜子中，这些物品不可以取出来，也不可以放新物品，不可挤一个柜子
("apple","orange","pear")

#存储方式三:这三个物品不仅按顺序分别存储到一个柜子中，而且每个柜子还有名称
{"sam":"apple","Jac":"orange","mating":"pear"}


# #栈的实现
#
# class Stack():
#     def __init__(self,size):
#         self.stack=[]
#         self.size=size
#         self.top=-1
#
#     def push(self,content):
#         if self.Full():
#             print "Stack is Full"
#         else:
#             self.stack.append(content)
#             self.top=self.top+1
#
#     def out(self):
#         if self.Empty():
#             print "Stack is Empty"
#         else:
#             self.top-=1
#
#     def Full(self):
#         if self.top==self.size-1:
#             return True
#         else:
#             return False
#
#     def Empty(self):
#         if self.top==-1:
#             print "Stack is Empty"
#
# if __name__=="__main__":
#     q=Stack(7)
#     q.Empty()
#     q.push("hello")
#     q.Empty()


#队列的实现

class Queue():
    def __init__(self,size):
        self.queue=[]
        self.size=size
        self.head=-1
        self.tail=-1

    def Empty(self):
        if self.head==self.tail:
            return True
        else:
            return False

    def Full(self):
        if self.tail-self.head==self.size-1:
            return True
        else:
            return False

    def enQueue(self,content):
        if self.Full():
            print "Queue is Full"
        else:
            self.queue.append(content)
            self.tail+=1

    def outQueue(self):
        if self.Empty():
            print "Queue is Empty!"
        else:
            self.head+=1


if __name__=="__main__":
    q=Queue(6)
    print q.Empty()
    q.enQueue("123")
    print q.Empty()
    q.outQueue()






