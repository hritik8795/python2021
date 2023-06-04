class LinkedList:
    def __init__(self,value):
        self.val =val
        self.next =None
    def add(self,val):
        if self.next ==None:
            self.next =LinkedList(val)
        else:
            self.next.add(val)
    def __str__(self):
        return "({val})".format(val =self.val)+str(self.next)

class binary:
    def __init__(self,val):
        self.val =val
        self.left =None
        self.right =None

def depth(tree):
    if tree ==None:
        return 0
    if tree.left ==None and tree.right =None:
        return 1
    else:
        depthleft =1+depth(tree.left)