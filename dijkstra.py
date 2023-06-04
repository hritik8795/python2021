from collections import defaultdict
class Graph:
    def __init__(self):
        self.nodes =set()
        self.edges =defaultdict(list)
        self.distances ={}
    def addNode(self,value):
        self.nodes.add(value)

    def addEdge(self,fromNode,toNode,distances):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode,toNode)] =distances

def dijkstra(graph,initial):
    visited ={initial:0}
    path =defaultdict(list)
    nodes =set(graph.nodes)

    while nodes:
        minNode =None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode =node
                elif visited[node]<visited[minNode]:
                    minNode =node
        if minNode is None:
            break
        nodes.remove(minNode)
        currentWeight =visited[minNode]

        for edge in graph.edges[minNode]:
            weight =currentWeight +graph.distances[(minNode,edge)]
            if edge not in visited or weight <visited[edge]:
                visited[edge] =weight
                path[edge].append(minNode)

    return visited,path
customgraph =Graph ()
customgraph.addNode("A")
customgraph.addNode("B")
customgraph.addNode("C")
customgraph.addNode("D")
customgraph.addNode("E")
customgraph.addNode("F")
customgraph.addNode("G")
customgraph.addEdge("A","B",2)
customgraph.addEdge("A","C",5)
customgraph.addEdge("B","C",6)
customgraph.addEdge("B","D",1)
customgraph.addEdge("B","E",3)
customgraph.addEdge("C","F",8)
customgraph.addEdge("D","E",4)
customgraph.addEdge("E","G",9)
customgraph.addEdge("F","G",7)
print(dijkstra(customgraph,"A"))