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
    n = 10**6
    t = 1
    giant_list, connected_list, vertices_list = [], [], []

    for i in range(0,t):
        print('Runthrough #', i+1)
        uf = WeightedQuickUnionUF(n)

        # run script until we have a fully connected component
        while uf.events_for_fully_connected() == None:
            s1 = randint(0, n-1)
            s2 = randint(0, n-1)
            uf.union(s1,s2)
            giant = uf.events_for_giant_component()
            isolated = uf.check_for_isolated_vertices()
            connected = uf.events_for_fully_connected()
            if uf._isolated_components % 10000 == 0:
                print(uf._isolated_components)

        giant_list.append(giant)
        vertices_list.append(isolated)
        connected_list.append(connected)

       
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
        