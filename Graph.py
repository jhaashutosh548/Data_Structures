# adjancency matrix
class grapham:
    def __init__(self,size):
        self.size = size
        self.graph = []
        self.vertex = []
    
    def add_vertex(self,x):
        if x in self.vertex:
            pass
        else:
            self.vertex.append(x)
            temp = []
            for i in range(self.size):
                temp.append(0)
            self.graph.append(temp)
    
    def add_edge(self, v1 , v2, e):
        i1 = self.vertex.index(v1)
        i2 = self.vertex.index(v2)
        self.graph[i1][i2] = e
        self.graph[i2][i1] = e
    
    def rm_edge(self, v1 , v2):
        i1 = self.vertex.index(v1)
        i2 = self.vertex.index(v2)
        self.graph[i1][i2] = 0

    def printing(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.vertex[i],"---",self.graph[i][j],"---",self.vertex[j])
    
g = grapham(4)
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_edge(1,2,1)
g.add_edge(1,3,1)
g.add_edge(1,4,1)
g.add_edge(2,3,1)
g.printing()
print(g.graph)



#bfs operation

graph = {
    1 : [2,3,4],
    2 : [1,3],
    3 : [2,1],
    4 : [1]
}

v = []
q = []

def bfs(v,q,x):
    v.append(x)
    q.append(x)

    while q:
        s = q.pop(0)
        print(s, end = ' ')
        for i in graph[s]:
            if i not in v:
                v.append(i)
                q.append(i)

print(graph)
bfs(v,q,3)
v=[]
def dfs(v,g,x):
    v.append(x)
    for i in graph[x]:
        if i not in v:
            dfs(v,g,i)
    print(v)

dfs(v,g,3)




