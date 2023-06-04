import Disjoint as dst
class Graph:
    def __init__(self,vertices):
        self.v =vertices
        self.graph =[]
        self.nodes =[]
        self.mst =[]

    def addEdge(self,S,D,W):
        self.graph.append([S,D,W])
    def addNode(self,value):
        self.nodes.append(value)

    def printSolution(self,S,D,W):
        for S,D,W in self.mst:
            print("%s-%s:%s"%(S,D,W))

    def kruskalAllgo(self):
        i,e =0,0
        ds =dst.Disjoint(self.nodes)
        self.graph =sorted(self.graph,key =lambda item:item[2])
        while e<self.v-1:
            S,D,W=self.graph[i]
            i +=1
            x =ds.find(S)
            y=ds.find(D)
            if x != y:
                e +=1
                self.mst.append([S,D,W])
                ds.union(x,y)
        self.printSolution(S,D,W)

g =Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addEdge("A","B",5)
g.addEdge("A","C",13)
g.addEdge("A","E",15)
g.addEdge("B","A",5)
g.addEdge("B","C",10)
g.addEdge("B","D",8)
g.addEdge("C","A",13)
g.addEdge("C","B",10)
g.addEdge("C","E",20)
g.addEdge("D","B",8)
g.addEdge("A","B",6)
g.addEdge("E","A",15)
g.addEdge("E","C",20)
g.kruskalAllgo()