import sys
class Graph:
    def __init__(self ,vertexNum,edges,Nodes):
        self.edges =edges
        self.nodes =nodes
        self.vertexNum =vertexNum
        self.mst =[]
    def printSolution(self):
        print("edge:weight")
        for S,D,W in self.mst:
            print("%s->%s:%s"%(S,D,W))

    def primsAlgo(self):
        visited =[0]*self.vertexNum
        edgeNum =0
        visited[0] =True
        while edgeNum<self.vertexNum-1:
            min =sys.maxsize
            for i in range[self.vertexNum]:
                if visited[i]:
                    for j in range(self.vertexNum):
                        if ((not visited[j]) and self.edges[i][j]):
                            if min>self.edges[i][j]:
                                min =self.edges[i][j]
                                S=i
                                D =j

            self.mst.append([self.nodes[S],self.nodes[D],self.edges[S][D]])
            visited[D] =True
            edgeNum +=1

        self.printSolution()

edges =[[0,10,20,0,0],
        [10,0,30,5,0],
        [20,0,30,0,15,6],
        [0,5,15,0,8],
        [0,0,6,8,0],
        ]
nodes =["A","B","C","D","E"]
g.Graph(5,edges,nodes)
g.primsAlgo()
