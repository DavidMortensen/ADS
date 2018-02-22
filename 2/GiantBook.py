import sys
from random import randint
from algs4.stdlib import stdio, stdstats
from MyUnionFind import WeightedQuickUnionUF

class UFW:
    """
    This is our Unit Find class, based upon the  Weighted Unit Find from uf.py. 
    n is the amount of nodes we want to create.
    t is the amount of runs we want to do.
    """
    n = 10**5
    events = 0
    is_giant = False
    is_isolated = True
    t = 1
    giant_list, connected_list, vertices_list = [], [], []

    for i in range(0,t):
        uf = WeightedQuickUnionUF(n)
        # run script until we have a fully connected component
        while uf.count() > 1:
            s1 = randint(0, n-1)
            s2 = randint(0, n-1)
            
            events += 1
            uf.union(s1,s2)
            
            if uf.count() == 1:
                fully_connected = events

            while not is_giant:
                if uf.largest_component() >= n/2:
                    giant_component = events
                    is_giant = True
                else: 
                    break

            while is_isolated:
                if uf._isolated_components == 0:
                    isolated = events
                    is_isolated = False
                else:
                    break
        # print(  sites, 
        #         isolated,
        #         giant_component,
        #         fully_connected)
        giant_list.append(giant_component)
        vertices_list.append(isolated)
        connected_list.append(fully_connected)


    if t > 1:
        # mean and stddev for giant 
        mean_giant = stdstats.mean(giant_list)
        stddev_giant = stdstats.stddev(giant_list)

        # mean and stddev for isolated vertices
        mean_iso = stdstats.mean(vertices_list) 
        stddev_iso = stdstats.stddev(vertices_list) 

        # mean and stddev for fully connected
        mean_con = stdstats.mean(connected_list)
        stddev_con = stdstats.stddev(connected_list)
        
        print("Mean of events for giant: ", round(mean_giant, 4), "Stddev of events for giant: ", round(stddev_giant, 4))
        print("Mean of events for no isolated: ", round(mean_iso, 4), "Stddev of events for no isolated: ", round(stddev_iso,4 ))
        print("Mean of events for connected: ", round(mean_con, 4), "Stddev of events for connected: ", round(stddev_con,4 ))

    elif t == 1:
        print('Events for giant: ', giant_list)
        print('Events for no isolated vertices: ', vertices_list)
        print('Events for a fully connected component: ', connected_list)

    else:
        raise ValueError('Variable "t" needs to be a positive integer.')
  