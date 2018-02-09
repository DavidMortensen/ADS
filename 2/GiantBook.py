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
#Just calling all of our methods.
            uf.union(s1,s2)
            uf.check_for_isolated_vertices()
            uf.events_for_giant_component(uf._biggest_component_size)
            uf.events_for_fully_connected()

#Printing the returned values.
        print(
            uf._total, 
            uf.check_for_isolated_vertices(), 
            uf.events_for_giant_component(uf._biggest_component_size),
            uf.events_for_fully_connected()
            )
