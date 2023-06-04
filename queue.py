class Queue:
    def __init__(self):
        self.items=[]
    def __str__(self):
        values =[str(x)for x in self.items]
        return ''.join(values)

    def isEmpty(self):
        if self.items ==[]:
            return True
        else:
            return False
    def enQueue(self,value):
        self.items.append(value)
        return 'the element is inserted in the end of queue'
    def dequeue(self):
        if self.isEmpty():
            return 'there is not any element in the queue'
        else:
            self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return 'there is no element in the queue'
        else:
            return self.items[0]
        
    def delete(self):
        self.items =None


customQueue =Queue()
customQueue.enQueue(1)
customQueue.enQueue(2)
customQueue.enQueue(3)
customQueue.enQueue(4)
print(customQueue)
print(customQueue.dequeue())
print(customQueue)
print(customQueue.delete())
