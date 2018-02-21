from __future__ import print_function
import sys

N = int(sys.stdin.readline())
vals = list(map(int, sys.stdin.readlines()))

for i in range(0, N):
    # your code goes here and uses the following
    for j in range(0, N):
        for k in range(0, N):
            for l in range(0, N):
                if vals[i]+vals[j]+vals[k]+vals[l] == 0:
                    print(i,j,k,l,file=sys.stderr)
                    print(True)
                    sys.exit()
print(False)
