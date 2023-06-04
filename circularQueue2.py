class Queue:
    def __init__ (self,maxsize):
        self.items =maxsize *[None]
        self.maxsize =maxsize
        self.start =-1
        self.top =-1
    def __str__(self):
        values=[str(x) for x in self.items]
        return ''.join(values)
    def isFull(self):
        if self.top +1 ==self.start:
            return True
        else:
            return False
    def isEmpty(self):
        if self.top ==-1:
            return True
        else:
            return False

    def enqueue(self,value):
        if self.isFull():
            return 'the queue is full '
        else:
            if self.top +1 ==self.maxsize:
                self.top =0
            else:
                self.top +=1
                if self.start ==-1:
                    self.start =0
                self.items[self.top] =value
                return 'the element is inserted at the end of queue'
    

    def dequeue(self):
        if self.isEmpty():
            return 'the queue is empty '
        else:
            firstElement =self.items[self.start]
            start =self.start
            if self.start ==self.top:
                self.start =-1
                self.top =-1
            elif self.start +1 ==self.maxsize:
                self.start =0
            else:
                self.start +=1
            self.items[start]=None
            return firstElement


    def peek(self):
        if self.isEmpty():
            return 'the queue is empty'
        else:
            return self.items[self.start]


    def delete(self):
        self.items=self.maxsize*[None]
        self.top=-1
        self.start =-1

customQueue =Queue(s3)
customQueue.enqueu]e(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)
print(customQueue)
print(customQueue.peek())
print(customQueue.dequeue())
customQueue.delete()
print(customQueue)