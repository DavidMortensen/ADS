import sys
from algs4.stdlib import stdio
from MyUnionFind import WeightedQuickUnionUF

class UFW:
    if __name__ == '__main__':
        sites = stdio.readInt()
        uf = WeightedQuickUnionUF(sites)
        print(uf._count)
        uf.isNotIsolated()
        
        while not stdio.isEmpty():
            s1 = stdio.readInt()
            s2 = stdio.readInt()
            uf.union(s1,s2)
        #print(uf._count, 'final number of components')
        #print(uf.connected(0,1))
        print(uf.isConnected())
        

