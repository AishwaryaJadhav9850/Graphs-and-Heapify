class Graph:
    graph={}

    def buildGraph(self,u,v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u]=[v]
        if v in self.graph:
            self.graph[v].append(u)
        else:
            self.graph[v]=[u]

    def printGraph(self):
        for i,j in self.graph.items():
            print(i," -> ",j)

    def BFS(self): # O(V+E) Time Complexity
        result={} # Implemented using QUEUE
        queue=[]
        i = list(self.graph.keys())[0]
        j = self.graph[i]
        result[i] = 0
        for i in j:
            queue.append([i,1])
            result[i] = 1
        while queue:
            p=queue.pop(0)
            v=self.graph[p[0]]
            for i in v:
                if i not in result:
                    result[i] = p[1]+1
                    queue.append([i,p[1]+1])
        print("\nBFS ",result)

    def DFS(self): # Implemented using STACK
        result = [] # O(V+E) Time Complexity
        stack = []
        k=list(self.graph.keys())[0]
        result.append(k)
        v=self.graph[k]
        for i in v:
            stack.append(i)
        while stack:
            p=stack.pop(-1)
            if p not in result:
                result.append(p)
                v = self.graph[p]
                for i in v:
                    stack.append(i)

        print("\nDFS ",result)



if __name__ == '__main__':
    p=Graph()
    p.buildGraph("a","c")
    p.buildGraph("a","b")
    p.buildGraph("c","e")
    p.buildGraph("b","e")
    p.buildGraph("b","d")
    p.buildGraph("d","e")
    p.buildGraph("d","f")
    p.buildGraph("e","f")
    p.printGraph()
    p.BFS()
    p.DFS()




