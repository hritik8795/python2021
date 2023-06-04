#we want to create a stack class 
class stack():
    def __init__(self):
        self.list =[]
#initiating the length of the stack
    def __len__(self):
        return len(self.list)
    def push(self,item):
        return self.list.append(item)
    def pop(self):
        if len(self.list)==0:
            return None
class QueueViaStack():
    def __init__(self):
        self.instack =stack()
        self.outstack =stack()
        
    def enqueue(self,item):
        self.instack.push(item)
    
    def dequeue(self):
        #till the instack have element it will pop and same element is pushed inside the outstack
        while len(self.instack):
            self.outstack.push(self.instack.pop())
#now by the above out stack is fulfilled so start poping from the outstack til the length o the out stack 
        result =self.outstack.pop()
        while len(self.outstack):
            self.instack.push(self.outstack.pop())
            return result
customQueue =QueueViaStack()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)
print(customQueue.dequeue())