from algs4.stdlib import stdio
from priority_queue import MaxPQ, Node
import math
import sys

pq = MaxPQ()

states = stdio.readInt()                                            # assign the amount of states
total_seats = stdio.readInt()                                       # assign the amount of seats
allocated_seats = states
remaining_seats = total_seats -allocated_seats
 

while not stdio.isEmpty():                                          # make sure our file still has values 
    
    state = str(stdio.readLine()).strip('\n')                       # assign statename and population count 
    population = int(stdio.readLine())
    priority = population / math.sqrt(1*(1+1))
    
    initial_seat = 1                                                # initialize 1 seat per state
    current_node = Node(state, priority, population, initial_seat)
    pq.insert(current_node)
    

while allocated_seats < total_seats:                                # run untill we have no more seats  
    item = pq.del_max()                                             # extract highest prioritized item in the queue
    s = item.seats
    p = item.population
    item.seats += 1
    allocated_seats += 1
    constant = math.sqrt(item.seats*(item.seats+1))                 # calculate constant that is used for division
    item.priority = p / constant                                    # store new quota for current item
    pq.insert(item)

pq.show()


