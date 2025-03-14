class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        #handle edge case
        if x < 0 or x > len(self.parent): return None
        if self.parent[x] != x: 
            #find parent recursively
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX is None or rootY is None: #  use is None when handling values with 0 
            return
        # make sure modifing the size
        if self.size[rootX] < self.size[rootY]:
            self.parent[rootX] = rootY
            self.size[rootY] += self.size[rootX]
        else:
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]
    
    def get_root(self):
        return [self.find(i) for i in range(len(self.parent))]


# drivers code
ds = DisjointSet(5)
ds.union(0,1)
ds.union(2,3)
ds.union(0,4)

print(ds.get_root())


