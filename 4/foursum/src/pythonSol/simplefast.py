from __future__ import print_function
from algs4.fundamentals import binary_search
import sys

N = int(sys.stdin.readline())
vals = list(map(int, sys.stdin.readlines()))

class FourSumFast:
    is_sum_zero = False
    @staticmethod
    def count(vals, N):
        is_sum_zero = False
    
        dictionary = {}
        for a in vals:
            for b in vals:
                dictionary[a+b] = [a, b]
                if -(a+b) in dictionary: 
                    [c, d] = dictionary[-(a+b)]
                    return [a, b, c, d]
        return None
        
        ''' count = 0
        is_sum_zero = False
        vals.sort()
        
        for i in range(0, N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    if binary_search.index_of(vals, -vals[i]-vals[j]-vals[k]) > k:
                        count += 1
        if count > 0:
            is_sum_zero = True
        print(is_sum_zero) '''

            

print(FourSumFast.count(vals, N))

