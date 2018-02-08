import sys
from algs4.stdlib import stdio
from MyUnionFind import WeightedQuickUnionUF

class UFW:
    if __name__ == '__main__':
        sites = stdio.readInt()
        uf = WeightedQuickUnionUF(sites)
        while not stdio.isEmpty():
            s1 = stdio.readInt()
            s2 = stdio.readInt()
            uf.union(s1,s2)
            for site in sites:
                if uf.isNotIsolated():
                    print('Isolated')
                else: 
                    print('Not Isolated')
        
        print('It is:', uf.connected(0,1), ' that 0 and 1 is connected')
        
        

