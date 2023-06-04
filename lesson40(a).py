#here give a tree and we hve to find whether path exitss s->e
class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict ={}
        self.gdict =gdict
    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)

    def checkroute(self,startNode,endNode):
        visited =[startNode]
        queue =[startNode]
        path =False
        while queue:
            devertex =queue.pop(0)
            for adjacentvertex in self.gdict[devertex]:
                if adjacentvertex not in visited:
                    if adjacentvertex ==endNode:
                        path =True
                        break
                    else:
                        visited.append(adjacentvertex)
                        queue.append(adjacentvertex)
        return path
customDict ={"a":["c","d","b"],
            "b":["j"],
            "c":["g"],
            "d":[""],
            "e":["f","a"],
            "f":["i"],
            "g":["d","h"],
            "h":[],
            "i":[],
            "j":[],
                               }
g =Graph(customDict)
print(g.checkroute("a","j"))