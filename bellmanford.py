class Graph:
    def __init__(self,vertices):
        self.v =vertices
        self.graph =[]
        self.nodes =[]

    def add_edge(self,S,D,W):
        self.graph.append([S,D,W])
    
    def addNode(self,value):
        self.nodes.append(value)
    def print_solution(self,dist):
        print("vertex distance from source ")
        for key,value in dist.items():
            print(' '+key,':  ',value)
    def bellmanford(self,src):
        dist ={i:float('INF')for i in self.nodes }
        dist[src] =0

        for i in range(self.v-1):
            for S,D,W in self.graph:
                if dist[S] !=float("INF") and dist[S] + W < dist[D]:
                    dist[D]=dist[S]+W
        for S,D,W in self.graph:
            if dist[S] != float("INF") and dist[S] + W < dist[D]:
                print("graph contain negative cycle")
                return
            self.print_solution(dist)

g =Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.add_edge("A","C",6)
g.add_edge("A","D",6)
g.add_edge("B","A",3)
g.add_edge("C","D",1)
g.add_edge("D","C",2)
g.add_edge("D","B",1)
g.add_edge("E","B",4)
g.add_edge("E","D",2)

g.bellmanford("E")