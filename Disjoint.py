class Disjoint:
    def __init__(self,vertices):
        self.vertices =vertices
        self.parents ={}
        for v in vertices:
            self.parents[v]=v
        self.rank =dict.fromkeys(vertices,0)

    def find(self,item):
        if self.parents[item] ==item:
            return item
        else:
            return self.find(self.parents[item])

    def union(self,x,y):
        xroot =self.find(x)
        yroot =self.find(y)
        if self.rank[xroot]<self.rank[yroot]:
            self.parents[xroot] =yroot
        elif self.rank[yroot]>self.rank[yroot]:
            self.parents[yroot] =xroot
        else:
            self.parents[yroot] =xroot
            self.rank[xroot] +=1
vertices =["A","B","C","D","E"]
ds =Disjoint(vertices)
ds.union("B","D")
ds.union("B","C")
print(ds.find("B"))