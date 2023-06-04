#make platestack class for initialize the stack and set the capacity
class Platestack():
    def __init__(self,capacity):
        self.capacity =capacity
        self.stacks =[]


#now cal str function for printing the stack
    def __str__(self):
        return self.stacks
#now start to pushing the element with push function
    def push(self,item):
        #in the next line i check the plates is greater than 0 and less than capacity
        if len(self.stacks)>0 and (len(self.stacks[-1]))<self.capacity:
            self.stacks[-1].append([item])
        else:
            self.stacks.append([item])
    def pop(self):
        #pop the element from the self.stack to self .stacks[-1]
        while len(self.stacks) and len(self.stacks[-1])==0:
            self.stacks.pop()
        #self.stack is empty
        if len(self.stacks)==0:
            return None
        else:
            return self.stacks[-1].pop()
#question me descibe esko karne ko 
    def pop_at(self,stackNumber):
        if len(self.stacks[stackNumber])>0:
            return self.stacks[stackNumber].pop()
        else:
            return None
customStack =Platestack(2)
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack.pop())
print(customStack.pop_at(1))