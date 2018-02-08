import sys
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
        self._event = 0
        self._notGiant = False
        self._total = n
        self._parent = list(range(n))
        self._isolated = [1]*n
        self._size = [1]*n
        self._countIsolated = n
        self._isIsolated = True
        self._connected = False
   
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
        
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return
        
        #Checks whether or not there's a giant component. If there is, print the 
        #amount of unions made when it's created.
        while not self._notGiant:
            if self._event > self._total/2:
                self._notGiant = True
                print(self._event)
            else:
                    break

        # make root of smaller rank point to root of larger rank
        if self._size[root_p] < self._size[root_q]:
            small, large = root_p, root_q
        else:
            small, large = root_q, root_p
            
        
        self._parent[small] = large
        self._size[large] += self._size[small]
      
        self._count -= 1
        
        #Checks whether a component is isolated or not
        if self._isolated[p] == 1:
            self._isolated[p] = 0
            self._countIsolated -= 1
            
        if self._isolated[q] == 1:
            self._isolated[q] = 0
            self._countIsolated -= 1
        
        

    def find(self, p):
        """
        Returns the component identifier for the component containing site p.

        :param p: the integer representing one site
        :return: the component identifier for the component containing site p
        """
        self._validate(p)
        
        while p != self._parent[p]:
            self._event += 1
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

    def isNotIsolated(self):
        """
        Returns the amount of unions made before the amount of isolated sites is 0.

        If > 0, returns sufficient message.
        """
        while self._isIsolated: 
            if 1 in self._isolated:
                #print("There's still isolated sites")
                break
            else:
                self._isIsolated = False
                print(self._event)
        return(self._event)
    
    def isConnected(self):
        """ 
        Returns True if there's one connected component. 
        Returns False if there's several components.
        """
        if self._count == 1:
            self._connected = True
        #print(self._event)
        return self._event
        
    #def isEvent(self):
        #if not self.connected():
         #   self._event += 1
        #else: 
        #    self._event += 1
