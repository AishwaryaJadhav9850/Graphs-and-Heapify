from operator import itemgetter

class Graph:
    graph = {}

    def buildGraph(self, u, v,k):
        if u in self.graph:
            self.graph[u].append([v,k])
        else:
            self.graph[u] = [[v,k]]
        if v in self.graph:
            self.graph[v].append([u,k])
        else:
            self.graph[v] = [[u,k]]

    def printGraph(self):
        for i, j in self.graph.items():
            print(i, " -> ", j)

    def BFS(self):  # O(V+E) Time Complexity
        result = {}  # Implemented using QUEUE
        queue = []
        i, j = self.graph.popitem()
        result[i] = 0
        for i in j:
            queue.append([i, 1])
            result[i] = 1
        while queue:
            p = queue.pop(0)
            v = self.graph[p[0]]
            for i in v:
                if i not in result:
                    result[i] = p[1] + 1
                    queue.append([i, p[1] + 1])
        print(result)

    def DFS(self):  # Implemented using STACK
        result = []  # O(V+E) Time Complexity
        stack = []
        k = list(self.graph.keys())[0]
        result.append(k)
        v = self.graph[k]
        for i in v:
            stack.append(i)
        while stack:
            p = stack.pop(-1)
            if p not in result:
                result.append(p)
                v = self.graph[p]
                for i in v:
                    stack.append(i)

        print("\nDFS ", result)

    def prims(self):
        visited = []
        not_visited = list(self.graph.keys())
        d = {}
        for element in self.graph.keys():
            d[element] = -1
        d[list(self.graph.keys())[0]]=0
        while (not_visited):
            val = 999999999999999
            for i,v in d.items():
                if v != -1 and v <= val and i not in visited:
                    val = v
                    vali = i
            visited.append(vali)
            not_visited.remove(vali)
            for neighbours in self.graph[vali]:
                if (neighbours[0] not in visited) and ((d[neighbours[0]] == -1) or (d[neighbours[0]] > neighbours[1])):
                    d[neighbours[0]] = neighbours[1]

        print("\nNodes and their Minimun path:", d)
        print("Minimum spanning Tree: ",sum(d.values()))

    def kruskal(self):
        visited = []
        list_vertices = []
        for element in list(self.graph.keys()):
            if element not in visited:
                visited.append(element)
            for neighbours in self.graph[element]:
                if neighbours[0] not in visited:
                    list_vertices.append([element, neighbours[0], neighbours[1]])
        print("List_vertices:", list_vertices)
        sorted_list = sorted(list_vertices, key=itemgetter(2))
        #print("Sorted list:", sorted_list)

        visited = []
        total = 0
        for i in sorted_list:
           # print(i)
            if i[0] not in visited and i[1] not in visited:
                visited.append(i[0])
                visited.append(i[1])
                total += i[2]
            elif i[0] not in visited and i[1] in visited:
                visited.append(i[0])
                total += i[2]
            elif i[0] in visited and i[1] not in visited:
                visited.append(i[1])
                total += i[2]
        print("MST value in Kruskal Algorithm:", total)
if __name__ == '__main__':
    p = Graph()

    p.buildGraph("a", "d", 4)
    p.buildGraph("a", "b", 2)
    p.buildGraph("a", "f", 5)
    p.buildGraph("d", "b", 1)
    p.buildGraph("f", "b", 8)
    p.buildGraph("f", "g", 1)
    p.buildGraph("d", "e", 2)
    p.buildGraph("b", "e", 3)
    p.buildGraph("b", "c", 7)
    p.buildGraph("b", "g", 4)
    p.buildGraph("c", "e", 10)
    p.buildGraph("c", "g", 6)
    """    
    p.buildGraph("a", "b", 5)
    p.buildGraph("a", "d", 4)
    p.buildGraph("b", "d", 2)
    p.buildGraph("b", "c", 3)
    p.buildGraph("c", "d", 6)
    """

    print("Graph and their Weights:")
    p.printGraph()
    p.prims()
    p.kruskal()




