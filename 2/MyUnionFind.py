import sys
import statistics
from algs4.stdlib import stdio

class WeightedQuickUnionUF:


    """
    This is an implementation of the union-find data structure - see module documentation for
    more info.

    This implementation uses weighted quick union by size (without path compression). 
    Initializing a data structure with n sites takes linear time. Afterwards, the union, find, 
    and connected operations take logarithmic time (in the worst case) and the count operation 
    takes constant time. For alternate implementations of the same API, see UF, QuickFindUF, 
    and QuickUnionUF.

    For additional documentation, see Section 1.5 of Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne.
    """


    def __init__(self, n):
        """
        Initializes an empty union-find data structure with n sites,
        0 through n-1. Each site is initially in its own component.

        :param n: the number of sites
        """
        self._count = n
        self._event_counter = 0
        self._vertices_counter = 1
        self._is_giant = False
        self._biggest_component_size = 0
        self._total = n
        self._parent = list(range(n))
        self._isolated = [1]*n
        self._size = [1]*n
        self._count_isolated = n
        self._is_isolated = True
        self._is_events_before_giant_returned = False
        self._events_before_giant = 0


    def _validate(self, p):
        # validate that p is a valid index
        n = len(self._parent)
        if p < 0 or p >= n:
            raise ValueError('index {} is not between 0 and {}'.format(p, n))


    def union(self, p, q):
        """
        Merges the component containing site p with the
        component containing site q.

        :param p: the integer representing one site
        :param q: the integer representing the other site
        """
        self._event_counter += 1

        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return
        
        # make root of smaller rank point to root of larger rank
        if self._size[root_p] < self._size[root_q]:
            small, large = root_p, root_q
        else:
            small, large = root_q, root_p    
        
        self._parent[small] = large
        self._size[large] += self._size[small]
        self._biggest_component_size = self._size[large]
        self._count -= 1
        
        
        #Checks whether a component is isolated or not by looking at the index of the current vertex, 
        #and comparing it to the list self._isolated at the same index. If the value is 1, the vertex is 
        #isolated, if the value is 0, it's connected to another vertex. 
        if self._isolated[p] == 1:
            self._isolated[p] = 0
            self._count_isolated -= 1
            
        if self._isolated[q] == 1:
            self._isolated[q] = 0
            self._count_isolated -= 1


    def find(self, p):
        """
        Returns the component identifier for the component containing site p.

        :param p: the integer representing one site
        :return: the component identifier for the component containing site p
        """
        self._validate(p)

        while p != self._parent[p]:
            p = self._parent[p]
            
        return p


    def connected(self, p, q):
        """
        Returns true if the two sites are in the same component.

        :param p: the integer representing one site
        :param q: the integer representing the other site
        :return: true if the two sites p and q are in the same component; false otherwise
        """
        return self.find(p) == self.find(q)


    def count(self):
        return self._count


    def check_for_isolated_vertices(self):
        """
        Checks whether or not there are still any isolated vertices in list self._isolated.
        When there's no isolated vertices, it returns the amount of events it has taken.
        """
        while self._is_isolated: 
            if 1 in self._isolated:
                self._vertices_counter += 1
                break
            else:
                return(self._vertices_counter)
                self._is_isolated = False


    def events_for_fully_connected(self):
        """ 
        Checks whether or not it is a fully connected component. 
        If the component is fully connected, it returns the amount of events it has taken
        """
        if self._count == 1:
            return(self._event_counter)
        #else:
            #self._events_counter += 1


    def events_for_giant_component(self, p):
        """
        This checks when there's a giant component, which is defined by =>n/2. When a giant
        component is created, it returns the amount of events it has taken.
        """
        n = 0
        if not self._is_giant:
             if p >= self._total/2:
                self._events_before_giant = self._event_counter
                self._is_giant = True
                return
                
                
                
        elif not self._is_events_before_giant_returned:
            return(self._events_before_giant)
            self._is_events_before_giant_returned = True
        