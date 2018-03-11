def _merge(a, aux, lo, mid, hi):
    # copy to aux[]
    for k in range(lo, hi+1):
        aux[k] = a[k]
        
    # merge back to a[]
    i, j = lo, mid+1
    for k in range(lo, hi+1):
        if i > mid:
            a[k] = aux[j]
            j += 1
        elif j > hi:
            a[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            a[k] = aux[j]
            j += 1
        else:
            a[k] = aux[i]
            i += 1


def get_run(a, s):
    # while our input index is below last index, and while the value of input 
    # index is below next index value, increment s.
    while s < len(a)-1 and a[s] <= a[s+1]:
        s += 1
    return min(s, len(a)-1)

def sort(a, count):
    lo, n, aux = 0, len(a), [None] * len(a)
    while lo < n:
        first = get_run(a, lo)              # first run a[lo:first+1]
        second = get_run(a, first + 1)      # second run a[first+1:second+1]
        
        # check whether or not two runs are the same, if so, they are either
        # one long run, or it's a standalone odd numbered run, in which case we break the loop.
        if first == second:
            if lo == 0:
                return
            else:
                break
        
        _merge(a, aux, lo, first, second)
        lo = second + 1
    print(a)
    sort(a, count+1)

import sys
from algs4.stdlib import stdio

# Reads in a sequence of strings from standard input or a file 
# supplied as argument to the program; runsorts them; 
# and prints them to standard output in ascending order.
if __name__ == '__main__':
    if len(sys.argv) > 1:
        try: 
            sys.stdin = open(sys.argv[1])
        except IOError:
            print("File not found, using standard input instead")
    
    a = stdio.readAllStrings()
    print(a)
    sort(a, 1)
    print(a)
    for elem in a:
        print(elem)
    
