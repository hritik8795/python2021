class stack:
    def __init__(self,maxsize):
        self.maxsize =maxsize
        self.list =[]

    def __str__(self):
        value=self.list.reverse()
        values =[str(x)for x in self.list]
        return '\n'.join(values)

    #isEmpty
    def isEmpty(self):
        if self.list ==[]:
            return True
        else:
            return False
    #isFULL
    def isFULL(self):
        if len(self.list)==self.maxsize:
            return True
        else:
            return False
    #pushw
    def push(self,value):
        if self.isFULL():
            return "the stack is full"
        else:    
            self.list.append(value)
            return "th list is successfully created"

    def pop(self):
        if self.isEmpty():
            return "the stack has no element"
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "the stack has no element"
        else:
            return self.list[len(self.list)-1]    

    def delete(self):
        self.list =None


customStack =stack(4)
customStack.isEmpty()
customStack.isFULL()
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
customStack.push(6)
customStack.pop()
print(customStack.peek())
print(customStack)
print(customStack.delete())


        


