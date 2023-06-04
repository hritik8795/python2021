class stack:
    def __init__(self):
        self.list =[]
    def __str__(self):
        values =self.list.reverse()
        values =[str(x) for x in self.list]
        return '\n'.join(values)

#is empty
    def isEmpty(self):
        if self.list ==[]:
            return True
        else:
            return False
    
    def push(self,value):
        self.list.append(value)
        return "the elementis inserted succeessfully"
    #for pop
    def pop(self):
        if self.isEmpty():
            return "there is no element for pop"
        else:
            return self.list.pop()

    #peek
    def peek(self):
        if self.isEmpty():
            return "ther is no element "
        else:
            return self.list[len(self.list)-1]

customStack =stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
customStack.pop()
print(customStack.peek())
print(customStack)

print(customStack.isEmpty())
