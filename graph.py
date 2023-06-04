class Graph:
    def __init__(self,gdict =None):
        if gdict is None:
            gdict ={}
        self.gdict =gdict

    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)
    def bfs(self,vertex):
        visited =[vertex]
        Queue =[vertex]

        while Queue:
            devertex =Queue.pop(0)
            print(devertex)

            for adjacentVertex in self.gdict[devertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    Queue.append(adjacentVertex)

    def dfs(self,vertex):
        visited =[vertex]
        stack =[vertex]

        while stack:
            popVertex =stack.pop()
            print(popVertex)
            for adjacentVertex in self.gdict[popVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)


customDict ={"a" :["a","b"],
            "b" :["a","d","e"],
            "c" :["a","e"],
            "d" :["b","e","f"],
            "e" :["d","f"],
            "f" :["d","e"]
                }
graph =Graph(customDict)
#graph.addEdge("e","c")
print(graph.gdict)
graph.bfs("b")
graph.dfs("a")