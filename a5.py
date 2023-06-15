
class node():
    def __init__(self,cap,i):
        self.cap=cap
        self.i=i
class Maxheap:
 
    def __init__(self):
    
        self.data = []
    def insert(self, key,value):
        n=node(key,value)
        self.data.append(n)
        self.upheap( len(self) - 1)

    def extractmax(self):
        if len(self.data)!=0:
            self.swap( len(self) - 1, 0)
            root = self.data.pop()
            self.downheap(0)
        else:
            root="Heap is empty"
        return root
    def __len__(self):
        return len(self.data)
    def swap(self,i, j):
       self.data[i], self.data[j] = self.data[j], self.data[i]
    def upheap(self, index):
        ri = (index - 1) // 2
        if ri < 0:
            return
        if self.data[index].cap > self.data[ri].cap:
            self.swap( index,ri)
            self.upheap( ri)
    def downheap(self, index):
        ci = 2 * index + 1
        if ci >= len(self.data):
            return
        if ci + 1 < len(self.data) and self.data[ci].cap< self.data[ci + 1].cap:
            ci += 1
        if self.data[ci].cap > self.data[index].cap:
            self.swap( ci, index)
            self.downheap( ci)
def path(parent,  target,src):
	L=[target]
	while target!=src:
		L.append(parent[target])	
		target=parent[target]
	L.reverse()
	return L	
def convert(m,Graph):
	g,M={},Graph
	for i in range(m):
		g[i]=[]
	for i in range(len(M)):
		g[M[i][0]].append((M[i][2],M[i][1]))
		g[M[i][1]].append((M[i][2],M[i][0]))
	return g

def findMaxCapacity(m,Graph,src,target):
    max_cap,parent,g_new=[-10**12]*m,[0]*m,convert(m,Graph)
    hip=Maxheap()
    hip.insert(0,src)
    max_cap[src]=10**12
    while True:
        if len(hip)<=0:
            break
        else:
            temp=hip.extractmax()
            current_src=temp.i
            for v in g_new[current_src]:
                weight=max(max_cap[v[1]],min(max_cap[current_src], v[0]))
                
                if weight>max_cap[v[1]]:
                    max_cap[v[1]],parent[v[1]]=weight,current_src
                    hip.insert(weight,v[1])
    l=path(parent,target,src)
    return(max_cap[target],l)
