import sys
from random import randint
from algs4.stdlib import stdio
from algs4.stdlib import stdstats
from MyUnionFind import WeightedQuickUnionUF

class UFW:
    x = 10
    t = 10
    giant_list = []
    connected_list = []
    vertices_list = []
    for i in range(0,t-1):
        if __name__ == '__main__':
            #sites = stdio.readInt()
            uf = WeightedQuickUnionUF(x)
            
            while uf.events_for_fully_connected() == None:
                s1 = randint(0, x-1)
                s2 = randint(0, x-1)
    #Just calling all of our methods.
                uf.union(s1,s2)
                uf.check_for_isolated_vertices()
                uf.events_for_giant_component(uf._biggest_component_size)
                uf.events_for_fully_connected()
                

    #Printing the returned values.
            giant_list.append(uf.events_for_giant_component(uf._biggest_component_size))
            vertices_list.append(uf.check_for_isolated_vertices())
            connected_list.append(uf.events_for_fully_connected())
            
    #print(len(connected_list))
   
        # mean for giant 
    mean_giant = stdstats.mean(giant_list), 
    # standard deviation for giant 
    stddev_giant = stdstats.stddev(giant_list)

    # mean for turned isolated
    mean_iso = stdstats.mean(vertices_list) 
    # standard deviation for isoalted
    stddev_iso = stdstats.stddev(vertices_list) 

    # mean for turned conencted
    mean_con = stdstats.mean(connected_list)
    # standard deviation for turned connected
    stddev_con = stdstats.stddev(connected_list)

    print("Here are the results for giant: ",  "Mean for giant: ", mean_giant, "Standard deviation for giant: ", stddev_giant)
    print("Here are the results for isolated: ",  "Mean for isolated: ", mean_iso, "Standard deviation for isolated: ", stddev_iso)
    print("Here are the results for connected: ",  "Mean for connected: ", mean_con, "Standard deviation for connected: ", stddev_con)
