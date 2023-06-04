class AnimalShelter():
    def __init__(self):
        self.dogs =[]
        self.cats =[]
    def enqueue(self,animal,type):
        if type =='Cat':
            self.cats.append(animal)
        else:
            self.dogs.append(animal)
    def dequeuecat(self):
        if len(self.cats)==0:
            return None
        else:
            cat =self.cats.pop(0)
            return cat
    def dequeuedogs(self):
        if len(self.dogs)==0:
            return None
        else:
            dogs =self.dogs.pop(0)
            return dogs
    
    def dequeueAny(self):
        if len(self.cats)==0:
            result =self.dogs.pop(0)
        else:
            result =self.cats.pop(0)
        return result
customQueue =AnimalShelter()
customQueue.enqueue('Cat1','Cat')
customQueue.enqueue('Cat2','Cat')
customQueue.enqueue('dog1','dog')
customQueue.enqueue('Cat3','Cat')
customQueue.enqueue('dog2','dog')
print(customQueue.dequeuedogs())
print(customQueue.dequeuedogs())
print(customQueue.dequeuecat())
print(customQueue.dequeuecat())
print(customQueue.dequeueAny())
print(customQueue.dequeueAny())