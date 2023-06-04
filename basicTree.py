class TreeNode:
    def __init__(self,data,children=[]):
        self.data =data
        self.children =children
    def __str__(self,level=0):
        ret =" "*level + str(self.data) + "\n"
        for child in self.children:
            ret +=child. __str__(level+1)
        return ret
    def addchild(self,TreeNode):
        self.children.append(TreeNode)
tree =TreeNode('drinks',[])
cold =TreeNode('cold',[])
hot =TreeNode('hot',[])
tree.addchild(cold)
tree.addchild(hot)
print(tree)
tea= TreeNode('tea',[])
coffee=TreeNode('coffee',[])
tea =TreeNode('tea',[])
coffee =TreeNode('coffee',[])
cola =TreeNode('cola',[])
fanta =TreeNode('fanta',[])
thumsup =TreeNode('thumsup',[])

cold.addchild(cola)
cold.addchild(fanta)
cold.addchild(thumsup)
hot.addchild(tea)
hot.addchild(coffee)
print(tree)